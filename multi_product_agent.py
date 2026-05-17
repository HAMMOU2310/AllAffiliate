import os
import sys
import codecs
import subprocess
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def build_multi_product_empire():
    print("=========================================================")
    print("🤖 RUNNING MULTI-PRODUCT MATRIX & GRID STORE ENGINE")
    print("=========================================================")
    
    # تأمين المكتبات
    for lib in ["gTTS", "pyperclip"]:
        subprocess.run([sys.executable, "-m", "pip", "install", lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from gtts import gTTS
    
    # 1. مصفوفة المنتجات (The Product Dictionary Matrix)
    # تحتوي على المنتجات، الكلمات المفتاحية للصور، والنصوص الصوتية المخصصة لكل منتج
    products_matrix = [
        {
            "id": "shed_plans",
            "title": "Ultimate 16,000 Shed & Cabin Plans",
            "desc": "Complete blueprints for outdoor sheds, cabins, and home extensions.",
            "img_urls": [
                "https://images.unsplash.com/photo-1549692520-acc6669e2f0c?w=1080&q=80",
                "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1080&q=80"
            ],
            "voice_text": "Want to build your dream wooden shed easily? Stop buying overpriced kits! Get instant access to sixteen thousand professional shed plans and blueprints today.",
            "vendor_link": "https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw"
        },
        {
            "id": "home_furniture",
            "title": "Premium Home Furniture Blueprints",
            "desc": "Step-by-step guides for building custom tables, chairs, beds, and indoor crafts.",
            "img_urls": [
                "https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=1080&q=80",
                "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?w=1080&q=80"
            ],
            "voice_text": "Stop spending thousands on luxury furniture. Build your own high-quality tables, chairs, and beds with professional step-by-step woodworking blueprints.",
            "vendor_link": "https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw"
        },
        {
            "id": "wood_crafts",
            "title": "Intricate Wood Toys & Garden Crafts",
            "desc": "Fun and easy projects for wooden toys, green houses, and artistic garden decorations.",
            "img_urls": [
                "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1080&q=80",
                "https://images.unsplash.com/photo-1606744824163-985d376605aa?w=1080&q=80"
            ],
            "voice_text": "Discover the joy of small scale woodworking. Create beautiful wooden toys and stunning garden crafts with these simple, beginner friendly blueprints.",
            "vendor_link": "https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw"
        }
    ]
    
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    # 2. حلقة التكرار الآلية (Looping Through the Matrix)
    print(f"🔄 Found {len(products_matrix)} target products in the matrix. Starting processing loop...")
    
    for index, prod in enumerate(products_matrix):
        print(f"\n📦 Processing Product [{index + 1}/{len(products_matrix)}]: {prod['title']}")
        
        # تسميات الملفات الخاصة بكل منتج لمنع الاختلاط
        img1_path = f"temp_{prod['id']}_1.jpg"
        img2_path = f"temp_{prod['id']}_2.jpg"
        voice_path = f"temp_{prod['id']}_voice.mp3"
        video_output = os.path.join(export_folder, f"Video_Product_{prod['id']}.mp4")
        
        # تحميل الصور تلقائياً لهذا المنتج
        try:
            print(f"  📥 Fetching unique images for {prod['id']}...")
            urllib.request.urlretrieve(prod['img_urls'][0], img1_path)
            urllib.request.urlretrieve(prod['img_urls'][1], img2_path)
        except Exception as e:
            print(f"  ❌ Skipping {prod['id']} due to image download failure: {str(e)}")
            continue
            
        # توليد الصوت البشري المخصص للمنتج
        print(f"  🎙️ Synthesizing custom AI voice narration...")
        tts = gTTS(text=prod['voice_text'], lang='en', slow=False)
        tts.save(voice_path)
        
        # تشكيل الفيديو بـ FFmpeg وتوحيد الأبعاد الصارم
        print(f"  🎬 Rendering final vertical video reel...")
        cmd = [
            'ffmpeg', '-y',
            '-loop', '1', '-t', '4', '-i', img1_path,
            '-loop', '1', '-t', '4', '-i', img2_path,
            '-i', voice_path,
            '-filter_complex',
            "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v1]; "
            "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v2]; "
            "[v1][v2]concat=n=2:v=1:a=0[v]",
            '-map', '[v]', '-map', '2:a',
            '-c:v', 'libx264', '-c:a', 'aac', '-t', '8', '-pix_fmt', 'yuv420p',
            video_output
        ]
        
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  ✅ SUCCESS: Generated {video_output}")
        
        # تنظيف ملفات المنتج المؤقتة فوراً
        for temp_f in [img1_path, img2_path, voice_path]:
            if os.path.exists(temp_f): os.remove(temp_f)

    # 3. خطوة البناء المتقدم للمتجر الشبكي (Deploying Multi-Product Frontend Grid)
    print("\n🌐 Step 3: Upgrading 'index.html' to an Advanced Multi-Product Catalog Grid...")
    
    grid_html_cards = ""
    for prod in products_matrix:
        grid_html_cards += f"""
        <div class="product-card">
            <h2>{prod['title']}</h2>
            <p>{prod['desc']}</p>
            <a href="{prod['vendor_link']}" target="_blank" class="buy-btn">👉 Get Access & Blueprints</a>
        </div>
        """
        
    full_store_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Ultimate Woodworking Mega Store</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #f5f2eb; margin: 0; padding: 0; color: #333; }}
        header {{ background-color: #5c3a21; color: white; padding: 30px 20px; text-align: center; border-bottom: 5px solid #8B5A2B; }}
        header h1 {{ margin: 0; font-size: 2.8em; }}
        header p {{ margin: 5px 0 0 0; font-size: 1.2em; color: #ddd; }}
        .store-container {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; }}
        .products-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; margin-top: 20px; }}
        .product-card {{ background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 6px solid #8B5A2B; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s; }}
        .product-card:hover {{ transform: translateY(-5px); }}
        .product-card h2 {{ color: #5c3a21; font-size: 1.5em; margin-top: 0; }}
        .product-card p {{ color: #666; font-size: 1.05em; line-height: 1.5; }}
        .buy-btn {{ display: block; text-align: center; background-color: #ff9900; color: white; padding: 12px; font-size: 1.2em; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 15px; box-shadow: 0 3px 8px rgba(255,153,0,0.3); }}
        .buy-btn:hover {{ background-color: #e68a00; }}
        footer {{ text-align: center; margin: 6px 0; color: #999; font-size: 0.9em; border-top: 1px solid #ddd; padding-top: 20px; }}
    </style>
</head>
<body>
    <header>
        <h1>🛠️ Premium Woodworking Blueprints Directory</h1>
        <p>Your one-stop digital shop for professional, easy-to-follow woodwork plans</p>
    </header>
    <div class="store-container">
        <div class="products-grid">
            {grid_html_cards}
        </div>
        <footer>© 2026 Woodworking Franchise Affiliate Store. All Rights Reserved.</footer>
    </div>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as html_file:
        html_file.write(full_store_html)
        
    print("✅ Success: 'index.html' updated with responsive 3-product display matrix.")
    print("\n=========================================================")
    print("🎯 SYSTEM STATE: 100% COMPLETE & MULTI-PRODUCT DEPLOYED!")
    print(f"1. Check your Desktop folder 'Social_Videos_Export' to see your 3 distinct videos.")
    print("2. Open 'index.html' to see your beautiful multi-product mega store.")
    print("=========================================================")

if __name__ == "__main__":
    build_multi_product_empire()
