import os
import sys
import codecs
import subprocess
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def build_antagonist_media():
    print("=========================================================")
    print("🎬 EXPERT MODE: GENERATING ANTAGONIST CONTENT VIDEO")
    print("=========================================================")
    
    # 1. تنظيف شامل فوري للميديا القديمة
    stale_media = ["wood_premium_1.jpg", "wood_premium_2.jpg", "antagonist_voice.mp3"]
    for f in stale_media:
        if os.path.exists(f):
            try: os.remove(f)
            except: pass
            
    # 2. تأمين المكاتب
    subprocess.run([sys.executable, "-m", "pip", "install", "gTTS"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from gtts import gTTS

    # 3. جلب صور نجارة حقيقية وراشدة 100% (أدوات وورشة عمل واقعية)
    img1, img2 = "wood_premium_1.jpg", "wood_premium_2.jpg"
    url1 = "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1080&q=80" # ورشة عمل وأدوات نجارة
    url2 = "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=1080&q=80" # خشب مصنع بدقة
    
    print("📥 Fetching raw, realistic workshop assets...")
    try:
        urllib.request.urlretrieve(url1, img1)
        urllib.request.urlretrieve(url2, img2)
        print("✅ Production assets locked.")
    except Exception as e:
        print(f"❌ Asset Fetch Error: {str(e)}")
        return

    # 4. صياغة النص السيكولوجي المضاد بالصوت البشري
    print("🎙️ Synthesizing Honest/Antagonist Voiceover Audio...")
    voice_file = "antagonist_voice.mp3"
    
    # نص الصدمة والندرة العكسية
    antagonist_script = (
        "Let's be completely honest. Most online woodworking plans are garbage. "
        "They waste your lumber, and have confusing blueprints. We audited sixteen thousand plans. "
        "They are not perfect, but statistically, they have the lowest error rate in the industry. "
        "Access is strictly limited due to high bandwidth. Click below to verify data if you are serious."
    )
    
    tts = gTTS(text=antagonist_script, lang='en', slow=False)
    tts.save(voice_file)
    print("✅ AI Voiceover compiled.")

    # 5. الدمج النهائي والمعالجة الهندسية بـ FFmpeg
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
        
    final_output = os.path.join(export_folder, "Woodworking_Antagonist_Final.mp4")
    
    print("⚡ Rendering vertical 1080x1920 video master layout...")
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '5', '-i', img1,
        '-loop', '1', '-t', '5', '-i', img2,
        '-i', voice_file,
        '-filter_complex',
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v1]; "
        "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v2]; "
        "[v1][v2]concat=n=2:v=1:a=0[v]",
        '-map', '[v]', '-map', '2:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '10', '-pix_fmt', 'yuv420p',
        final_output
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("\n=========================================================")
        print(f"🎉 PRODUCTION SUCCESS: Video completely generated without errors!")
        print(f"📁 Video Path: {final_output}")
        print("=========================================================")
        
        # تنظيف الملف الصوتي المؤقت
        if os.path.exists(voice_file): os.remove(voice_file)
    except Exception as e:
        print(f"❌ FFmpeg Processing Error: {str(e)}")

if __name__ == "__main__":
    build_antagonist_media()
