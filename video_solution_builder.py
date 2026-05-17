import os
import sys
import codecs
import subprocess
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def build_perfect_solution_video():
    print("=========================================================")
    print("🎬 EXPERT VIDEO ENGINE v2: CONFESSION + SOLUTION PHASES")
    print("=========================================================")
    
    # التنظيف الجذري للملفات المؤقتة
    for f in ["w1.jpg", "w2.jpg", "w3.jpg", "w4.jpg", "solution_voice.mp3"]:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass
            
    subprocess.run([sys.executable, "-m", "pip", "install", "gTTS"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from gtts import gTTS

    # جلب 4 صور عالية الجودة لورش نجارة حقيقية لتغطية مدة النص الطويل
    images = {"w1.jpg": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1080&q=80",
              "w2.jpg": "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=1080&q=80",
              "w3.jpg": "https://images.unsplash.com/photo-1426927308491-6380b6a9936f?w=1080&q=80",
              "w4.jpg": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1080&q=80"}
              
    print("📥 Downloading premium cinematic assets...")
    for name, url in images.items():
        try: urllib.request.urlretrieve(url, name)
        except Exception as e: print(f"❌ Failed to download {name}: {str(e)}"); return

    # صياغة النص السيكولوجي الكامل: الاعتراف بالخداع ثم تقديم الحل القاطع والتوضيح
    print("🎙️ Synthesizing Advanced Voiceover (Confession -> Explanation -> Solution)...")
    voice_file = "solution_voice.mp3"
    extended_script = (
        "Let's be completely honest. Most online woodworking plans are pure garbage. "
        "They are designed by amateurs to waste your expensive lumber, leaving you with confusing blueprints and zero guidance. "
        "But here is the real solution. We spent months auditing sixteen thousand professional schematics to extract the ultimate, "
        "foolproof blueprints. Every single plan now includes exact material lists, sharp 3D CAD angles, and step by step instructions "
        "that eliminate all guesswork. No more frustration, just master craftsmanship. Click the link below to lock in your verified access immediately."
    )
    
    tts = gTTS(text=extended_script, lang='en', slow=False)
    tts.save(voice_file)
    print("✅ Advanced AI Voiceover compiled successfully.")

    # الإخراج النهائي بـ FFmpeg بأبعاد ريلز الرأسية 1080x1920
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder): os.makedirs(export_folder)
    final_output = os.path.join(export_folder, "Woodworking_Perfect_Solution.mp4")
    
    print("⚡ Rendering vertical layout master via structural hardware scale filters...")
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '6', '-i', 'w1.jpg',
        '-loop', '1', '-t', '6', '-i', 'w2.jpg',
        '-loop', '1', '-t', '6', '-i', 'w3.jpg',
        '-loop', '1', '-t', '6', '-i', 'w4.jpg',
        '-i', voice_file,
        '-filter_complex',
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v1]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v2]; "
        "[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v3]; "
        "[3:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v4]; "
        "[v1][v2][v3][v4]concat=n=4:v=1:a=0[v]",
        '-map', '[v]', '-map', '4:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '24', '-pix_fmt', 'yuv420p',
        final_output
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("\n=========================================================")
        print(f"🎉 VIDEO UPGRADE SUCCESSFUL!")
        print(f"📁 Open your Desktop, Mapped Video at: {final_output}")
        print("=========================================================")
        # تنظيف ملف الصوت المؤقت لتوفير المساحة
        if os.path.exists(voice_file): os.remove(voice_file)
    except Exception as e:
        print(f"❌ FFmpeg Engine Error: {str(e)}")

if __name__ == "__main__":
    build_perfect_solution_video()
