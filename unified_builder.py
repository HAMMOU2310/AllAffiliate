import os
import sys
import codecs
import subprocess
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def run_advanced_franchise_pipeline():
    print("=========================================================")
    print("🚀 STARTING THE UNIFIED AGENT & STORE BUILDING PIPELINE")
    print("=========================================================")
    
    # الخطوة 1: التنظيف الجذري للمجلد لمنع التداخل أو الكاش القديم
    stale_files = ["image1.jpg", "image2.jpg", "wood_product1.jpg", "wood_product2.jpg", 
                   "voice_speech.mp3", "background_music.mp3", "voice_narration.mp3"]
    print("🧹 Step 1: Performing strict directory cleanup...")
    for f in stale_files:
        if os.path.exists(f):
            try:
                os.remove(f)
            except:
                pass
    print("✅ Cleanup complete. Directory is clean and ready.")

    # الخطوة 2: تأمين وتثبيت المكتبات البرمجية اللازمة
    print("📦 Step 2: Verifying and installing advanced Python requirements...")
    for lib in ["gTTS", "pyperclip"]:
        subprocess.run([sys.executable, "-m", "pip", "install", lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    from gtts import gTTS
    import pyperclip

    # الخطوة 3: تحميل صور نجارة وأكواخ حقيقية ومضمونة 100%
    print("📥 Step 3: Fetching high-converting woodworking and shed assets...")
    img1, img2 = "wood_premium_1.jpg", "wood_premium_2.jpg"
    url1 = "https://images.unsplash.com/photo-1549692520-acc6669e2f0c?w=1080&q=80"
    url2 = "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1080&q=80"
    
    try:
        urllib.request.urlretrieve(url1, img1)
        urllib.request.urlretrieve(url2, img2)
        print("✅ High-quality woodworking images downloaded successfully.")
    except Exception as e:
        print(f"❌ Image Download Failed: {str(e)}")
        return

    # الخطوة 4: توليد الصوت البشري التسويقي الاحترافي بالذكاء الاصطناعي
    print("🎙️ Step 4: Synthesizing AI Human Voiceover Narration (English)...")
    voice_output = "voice_narration.mp3"
    promo_script = "Want to build your dream wooden shed without spending a fortune? Stop buying overpriced kits! Click the link below to get instant access to sixteen thousand professional woodworking plans, step-by-step blueprints, and material lists. Start building today!"
    
    tts = gTTS(text=promo_script, lang='en', slow=False)
    tts.save(voice_output)
    print("✅ AI Voiceover narration generated and saved.")

    # الخطوة 5: المعالجة الهندسية الصارمة وإنتاج الفيديو النهائي بـ FFmpeg
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    final_video = os.path.join(export_folder, "ShedPlans_Final_Voice.mp4")
    
    print("🎬 Step 5: Rendering cinematic Reels video via strict geometry filters...")
    # الفلتر يفرض أبعاد 1080x1920 ويقوم بعمل Crop وتوحيد الـ SAR إجبارياً لمنع خطأ الدمج نهائياً
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '4', '-i', img1,
        '-loop', '1', '-t', '4', '-i', img2,
        '-i', voice_output,
        '-filter_complex',
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v1]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v2]; "
        "[v1][v2]concat=n=2:v=1:a=0[v]",
        '-map', '[v]', '-map', '2:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '8', '-pix_fmt', 'yuv420p',
        final_video
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"🎉 VIDEO CAPTURE SUCCESSFUL! Video generated at: {final_video}")
    except Exception as e:
        print(f"❌ FFmpeg Render Error: {str(e)}")
        return

    # الخطوة 6: بناء وتوليد واجهة المتجر الإلكتروني الاحترافي (index.html)
    print("🌐 Step 6: Deploying local Smart Store frontend (index.html)...")
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Woodworking Plans Store</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f1ea; margin: 0; padding: 0; text-align: center; color: #333; }
        .container { max-width: 800px; margin: 50px auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 8px solid #8B5A2B; }
        h1 { color: #8B5A2B; font-size: 2.5em; margin-bottom: 10px; }
        p { font-size: 1.2em; line-height: 1.6; color: #666; }
        .features { margin: 30px 0; text-align: left; background: #faf8f5; padding: 20px; border-radius: 8px; border-left: 5px solid #8B5A2B; }
        .features ul { list-style-type: '✓ '; padding-left: 20px; font-size: 1.1em; color: #444; }
        .features li { margin-bottom: 10px; }
        .cta-btn { display: inline-block; background-color: #ff9900; color: white; font-size: 1.5em; padding: 15px 40px; text-decoration: none; border-radius: 50px; font-weight: bold; box-shadow: 0 4px 10px rgba(255,153,0,0.4); transition: transform 0.2s; margin-top: 20px; }
        .cta-btn:hover { transform: scale(1.05); background-color: #e68a00; }
        footer { margin-top: 40px; font-size: 0.9em; color: #999; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛠️ 16,000 Woodworking Plans & Blueprints</h1>
        <p>Start building amazing projects easily! Get instant access to the world's largest collection of step-by-step woodworking guides, material lists, and detailed schematics.</p>
        
        <div class="features">
            <h3>What You Get Inside:</h3>
            <ul>
                <li>16,000 Professional, Clean Blueprints.</li>
                <li>Complete Material & Tools Lists (No waste!).</li>
                <li>Step-by-Step Instructions suitable for beginners & pros.</li>
                <li>Lifetime updates and 3D CAD modeling views.</li>
            </ul>
        </div>
        
        <a href="https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw" target="_blank" class="cta-btn">👉 GET INSTANT ACCESS NOW</a>
        
        <footer>© 2026 Affiliate Mega Store. All Rights Reserved.</footer>
    </div>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    print("✅ Smart Store interface generated successfully as 'index.html'.")

    # الخطوة 7: تجهيز نص الفيسبوك وحقنه في كليب بورد النظام
    facebook_caption = "Build your dream wooden shed easily! 🛠️ Get instant access to 16,000 professional woodworking plans, step-by-step blueprints, and material lists. Click here to download yours today 👉 https://your-domain-or-store-link.com"
    pyperclip.copy(facebook_caption)
    print("\n=========================================================")
    print("🎯 ALL STEPS COMPLETED SUCCESSFULLY!")
    print("1. Your Cinematic Video with AI VOICE is ready at: Desktop\\Social_Videos_Export\\ShedPlans_Final_Voice.mp4")
    print("2. Your Store Front is live in the folder as: index.html")
    print("3. Facebook Promotion Text is already COPIED to your Clipboard! Just press Ctrl+V to paste it.")
    print("=========================================================")

if __name__ == "__main__":
    run_advanced_franchise_pipeline()
