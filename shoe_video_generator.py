import os
import sys
import codecs
import subprocess
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def build_shoe_antagonist_video():
    print("=========================================================")
    print("👟 FOOTWEAR VIDEO ENGINE: CONFESSION & BIOMECHANICAL BIAS")
    print("=========================================================")
    
    # 1. تنظيف شامل للملفات المؤقتة
    for f in ["s1.jpg", "s2.jpg", "s3.jpg", "s4.jpg", "shoe_voice.mp3"]:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass
            
    # 2. تأمين مكتبة الصوت
    subprocess.run([sys.executable, "-m", "pip", "install", "gTTS"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from gtts import gTTS

    # 3. جلب صور أحذية رياضية ديناميكية وعالية الجودة (Premium Footwear & Testing)
    images = {
        "s1.jpg": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=1080&q=80", # حذاء أحمر رياضي قوي
        "s2.jpg": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=1080&q=80", # حذاء رياضي من زاوية ديناميكية
        "s3.jpg": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=1080&q=80", # تفاصيل نعل الحذاء والمتانة
        "s4.jpg": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=1080&q=80"  # حذاء عصري مريح
    }
              
    print("📥 Fetching raw, high-durability footwear assets...")
    for name, url in images.items():
        try: urllib.request.urlretrieve(url, name)
        except Exception as e: print(f"❌ Asset Error {name}: {str(e)}"); return

    # 4. صياغة النص السيكولوجي المضاد للأحذية (صدمة -> توضيح -> الحل)
    print("🎙️ Synthesizing Honest Footwear Voiceover Audio...")
    voice_file = "shoe_voice.mp3"
    shoe_script = (
        "Let's be completely honest. Most over-hyped sneakers are an absolute scam. "
        "They look flashy in ads, but they use cheap synthetic foam that destroys your arches and wears out in weeks. "
        "We ran independent biomechanical stress tests on the market's top footwear. "
        "The truth is, you don't need a three-hundred dollar logo. You need verified impact absorption and real orthopedic structure. "
        "We mapped the data to find the ultimate ergonomic design that saves your feet and your wallet. "
        "Click below to review our certified analytics before making your next purchase."
    )
    
    tts = gTTS(text=shoe_script, lang='en', slow=False)
    tts.save(voice_file)
    print("✅ Footwear AI Voiceover compiled.")

    # 5. الدمج النهائي والمعالجة الهندسية بـ FFmpeg مقاس 1080x1920
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder): os.makedirs(export_folder)
    final_output = os.path.join(export_folder, "Footwear_Antagonist_Perfect.mp4")
    
    print("⚡ Rendering vertical layout for Reels / TikTok...")
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '6', '-i', 's1.jpg',
        '-loop', '1', '-t', '5', '-i', 's2.jpg',
        '-loop', '1', '-t', '5', '-i', 's3.jpg',
        '-loop', '1', '-t', '6', '-i', 's4.jpg',
        '-i', voice_file,
        '-filter_complex',
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v1]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v2]; "
        "[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v3]; "
        "[3:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v4]; "
        "[v1][v2][v3][v4]concat=n=4:v=1:a=0[v]",
        '-map', '[v]', '-map', '4:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '22', '-pix_fmt', 'yuv420p',
        final_output
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("\n=========================================================")
        print(f"🎉 SHOE VIDEO PRODUCTION SUCCESS!")
        print(f"📁 Target Output Location: {final_output}")
        print("=========================================================")
        # تنظيف ملف الصوت المؤقت
        if os.path.exists(voice_file): os.remove(voice_file)
    except Exception as e:
        print(f"❌ FFmpeg Shoe Engine Error: {str(e)}")

if __name__ == "__main__":
    build_shoe_antagonist_video()
