# -*- coding: utf-8 -*-
import json, os, asyncio, requests, subprocess, shutil
from datetime import datetime
from edge_tts import Communicate
from deep_translator import GoogleTranslator

UNSPLASH_ACCESS_KEY = "ZNKbMqE40eQ-8iNV6VSNYXJfqlsLYcR8C-nEWbjHZhk"
VIDEOS_FOLDER = r"C:\Users\hamm\Desktop\فيديوهات التواصل"
PRODUCTS_FILE = "products.json"

CLICKBANK_PRODUCT = {
    "id": "shedplans",
    "name": "Shed Plans & Blueprints",
    "desc": "خطط كاملة خطوة بخطوة لبناء سقيفة الأحلام، تستهدف هواة النجارة والأشغال اليدوية. ليست مناسبة لمن يريد سقيفة جاهزة خلال يومين.",
    "price": "$37",
    "link": "https://hop.clickbank.net/?affiliate=allaaffili&vendor=shedplans",
    "refund_rate": "منخفضة",
    "category": "DIY"
}

LANGUAGES = [
    ("ar", "ar-EG-SalmaNeural"),
    ("en", "en-US-JennyNeural"),
    ("fr", "fr-FR-DeniseNeural"),
    ("es", "es-ES-ElviraNeural"),
    ("de", "de-DE-KatjaNeural"),
    ("hi", "hi-IN-SwaraNeural"),
    ("pt", "pt-BR-FranciscaNeural"),
    ("ru", "ru-RU-SvetlanaNeural"),
    ("ja", "ja-JP-NanamiNeural"),
    ("ko", "ko-KR-SunHiNeural"),
    ("zh-CN", "zh-CN-XiaoxiaoNeural"),
    ("tr", "tr-TR-EmelNeural")
]

def save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [CLICKBANK_PRODUCT]

def get_image_url(keyword="shed plans"):
    try:
        url = f"https://api.unsplash.com/photos/random?query={keyword}&client_id={UNSPLASH_ACCESS_KEY}"
        return requests.get(url, timeout=60).json()["urls"]["regular"]
    except:
        return None

async def generate_tts(text, voice, filename):
    for attempt in range(3):
        try:
            comm = Communicate(text, voice)
            await comm.save(filename)
            return True
        except:
            await asyncio.sleep(3)
    return False

def translate_text(text, target_lang):
    if target_lang == "ar":
        return text
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except:
        return text

def create_video(image_url, audio_path, output_path):
    if not image_url or not os.path.exists(audio_path):
        return False
    img_file = f"temp_{os.path.basename(output_path)}.jpg"
    try:
        with open(img_file, "wb") as f:
            f.write(requests.get(image_url, timeout=60).content)
    except:
        return False
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "sine=frequency=220:duration=10", "-af", "volume=0.05", "-c:a", "aac", "bg_music.m4a"], capture_output=True)
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", img_file,
        "-i", audio_path,
        "-i", "bg_music.m4a",
        "-filter_complex",
        "[2:a]volume=0.15[bg];[1:a][bg]amix=inputs=2:duration=shortest[aout];[0:v]drawtext=text='AllAffiliate':fontcolor=white@0.6:fontsize=24:x=w-tw-20:y=h-th-20[v]",
        "-map", "[v]", "-map", "[aout]",
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest", output_path
    ]
    subprocess.run(cmd, capture_output=True)
    for f in [img_file, "bg_music.m4a"]:
        if os.path.exists(f):
            os.remove(f)
    return os.path.exists(output_path) and os.path.getsize(output_path) > 1000

async def build_product_page(product):
    safe_id = product.get("id", "product")
    page_dir = f"store/{safe_id}"
    os.makedirs(page_dir, exist_ok=True)

    image_url = get_image_url(product.get("id", "shed"))
    if not image_url:
        print(f"[X] فشل جلب الصورة: {product['name']}")
        return

    print(f"[>] بناء: {product['name']}...")
    master_content = "#EXTM3U\n"

    for lang, voice in LANGUAGES:
        translated_desc = translate_text(product.get("desc", ""), lang)
        cta = product.get("link", "#")
        text = f"{translated_desc} {cta}"
        audio_f = f"{page_dir}/audio_{lang}.mp3"
        if await generate_tts(text, voice, audio_f):
            output_f = f"{page_dir}/video_{lang}.mp4"
            if create_video(image_url, audio_f, output_f):
                master_content += f'#EXT-X-STREAM-INF:BANDWIDTH=800000,AUDIO="{lang}"\nvideo_{lang}.mp4\n'
            os.remove(audio_f)

    with open(f"{page_dir}/master.m3u8", "w", encoding="utf-8") as f:
        f.write(master_content)

    refund_note = f"نسبة الاسترداد: {product.get('refund_rate', 'غير متوفر')}"
    html = f"""<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{product['name']} - AllAffiliate</title>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #1a1a2e; color: #eee; line-height: 1.8; text-align: right; }}
    .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
    .header {{ text-align: center; padding: 40px 20px; background: linear-gradient(135deg, #16213e, #0f3460); border-radius: 20px; margin-bottom: 30px; }}
    .header h1 {{ font-size: 2.2em; color: #e94560; margin-bottom: 10px; }}
    .video-container {{ background: #000; border-radius: 20px; overflow: hidden; margin-bottom: 30px; }}
    video {{ width: 100%; display: block; }}
    .info-box {{ background: #16213e; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
    .warning-box {{ background: #2d132c; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #e94560; }}
    .cta {{ text-align: center; margin: 30px 0; }}
    .btn {{ display: inline-block; background: #e94560; color: #fff; padding: 18px 50px; font-size: 1.3em; border-radius: 50px; text-decoration: none; font-weight: bold; }}
    .btn:hover {{ background: #c23152; }}
    .footer {{ text-align: center; padding: 20px; color: #888; font-size: 0.9em; }}
</style></head>
<body>
    <div class="container">
        <div class="header">
            <h1>{product['name']}</h1>
        </div>
        <div class="video-container">
            <video controls autoplay muted>
                <source src="master.m3u8" type="application/x-mpegURL">
                متصفحك لا يدعم الفيديو متعدد اللغات.
            </video>
        </div>
        <div class="info-box">
            <h2>السعر</h2>
            <p>{product.get('price', 'غير متوفر')}</p>
            <p style="color: #4ecca3;">{refund_note}</p>
        </div>
        <div class="warning-box">
            <h3>لمن هذا المنتج غير مناسب؟</h3>
            <p>لا يناسب من يريد حلاً جاهزاً دون عمل، أو من لا يحب قراءة المخططات.</p>
        </div>
        <div class="cta">
            <a href="{product.get('link', '#')}" class="btn" target="_blank">احصل على المنتج الآن</a>
        </div>
        <div class="footer">
            <p>AllAffiliate - روابط تسويق بالعمولة.</p>
            <p><a href="../../../home.html" style="color:#e94560;">العودة للمتجر</a></p>
        </div>
    </div>
</body></html>"""
    with open(f"{page_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] {product['name']}")

def build_homepage(products):
    cards = ""
    for p in products:
        safe_id = p.get("id", "product")
        cards += f"""
        <div style="background:#16213e; padding:20px; border-radius:15px; margin:15px; width:280px; display:inline-block; vertical-align:top;">
            <h3 style="color:#e94560;">{p['name']}</h3>
            <p style="color:#ccc;">{p.get('desc', '')[:100]}...</p>
            <p style="color:#4ecca3;">{p.get('price', '')}</p>
            <p style="color:#ff6b6b;">{p.get('refund_rate', '')}</p>
            <a href="store/{safe_id}/index.html" style="display:block; background:#e94560; color:white; padding:12px; border-radius:25px; text-align:center; text-decoration:none; margin-top:10px;">عرض المنتج</a>
        </div>"""
    html = f"""<!DOCTYPE html><html dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>متجر AllAffiliate</title>
<style>
    body {{ background: #1a1a2e; color: #eee; font-family: 'Segoe UI', Tahoma, sans-serif; text-align: center; }}
    h1 {{ color: #e94560; padding: 30px; }}
    .products-grid {{ display: flex; flex-wrap: wrap; justify-content: center; max-width: 1200px; margin: 0 auto; }}
</style></head>
<body>
    <h1>متجر AllAffiliate</h1>
    <p style="color:#ccc;">دبلجة تلقائية بـ 12 لغة. ربح بالعمولة والمشاهدات.</p>
    <div class="products-grid">{cards}</div>
    <p style="color:#888; padding:20px;">آخر تحديث: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
</body></html>"""
    with open("home.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] الصفحة الرئيسية")

async def main():
    products = load_products()
    save_products(products)
    print(f"عدد المنتجات: {len(products)}")
    for product in products:
        await build_product_page(product)
    build_homepage(products)
    for product in products:
        safe_id = product.get("id", "product")
        src_video = f"store/{safe_id}/video_ar.mp4"
        if os.path.exists(src_video):
            shutil.copy(src_video, os.path.join(VIDEOS_FOLDER, f"{safe_id}.mp4"))
    print("تم بنجاح!")

asyncio.run(main())
