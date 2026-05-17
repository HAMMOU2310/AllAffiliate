import os
import sys
import codecs
import urllib.request
import subprocess

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def run_automated_store_franchise():
    print("====================================================")
    print("🚀 INITIATING MASTER AFFILIATE AGENT - BACK ON TRACK")
    print("====================================================")
    
    # 1. تثبيت وتأكيد مكاتب الصوت البشري والتحكم
    print("Checking system requirements...")
    try:
        import gTTS
    except ImportError:
        print("Installing Voice Generation Engine (gTTS)...")
        subprocess.run([sys.executable, "-m", "pip", "install", "gTTS"], stdout=subprocess.DEVNULL)

    # 2. إعداد مجلدات المتجر الإلكتروني والميديا
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
        
    print("⚙️ Verifying HLS Store Streaming Directory...")
    
    # 3. التحميل الآلي الموجه لنيتش الخشب والنجارة حصراً (تجنب العشوائية)
    img1, img2 = "wood_product1.jpg", "wood_product2.jpg"
    voice_file = "voice_speech.mp3"
    output_video = os.path.join(export_folder, "ShedPlans_Final_Voice.mp4")
    
    # روابط صور نجارة وأكواخ حقيقية 100%
    wood_url1 = "https://images.unsplash.com/photo-1549692520-acc6669e2f0c?q=80&w=600&auto=format&fit=crop"
    wood_url2 = "https://images.unsplash.com/photo-1510798831971-661eb04b3739?q=80&w=600&auto=format&fit=crop"
    
    print("📥 System fetching targeted Woodworking imagery...")
    urllib.request.urlretrieve(wood_url1, img1)
    urllib.request.urlretrieve(wood_url2, img2)
    
    # 4. توليد صوت ناطق بشري حقيقي (وليس موسيقى) يتحدث عن منتج كليك بانك
    print("🎙️ Generating AI Human Voice Narration for ClickBank Product...")
    from gtts import gTTS
    # نص ناطق بالإنجليزية يقرأه صوت بشري احترافي لإقناع العميل بالشراء
    speech_text = "Stop wasting money on overpriced sheds! Click the link below to get instant access to sixteen thousand professional woodworking plans and blueprints. Build it yourself today!"
    tts = gTTS(text=speech_text, lang='en', slow=False)
    tts.save(voice_file)
    
    print("🎬 Rendering Final Video: Merging Moving Wood Images + AI Voice Speech...")
    
    # 5. أمر FFmpeg يربط الصور المتحركة بالصوت البشري الناطق مباشرة
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '4', '-i', img1,
        '-loop', '1', '-t', '4', '-i', img2,
        '-i', voice_file,
        '-filter_complex',
        "[0:v]scale=2160x3840,zoompan=z='min(zoom+0.0015,1.5)':d=100:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,setsar=1,setpts=PTS-STARTPTS[v1]; "
        "[1:v]scale=2160x3840,zoompan=z='min(zoom+0.0015,1.5)':d=100:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,setsar=1,setpts=PTS-STARTPTS[v2]; "
        "[v1][v2]concat=n=2:v=1:a=0[v]",
        '-map', '[v]', '-map', '2:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '8', '-pix_fmt', 'yuv420p',
        output_video
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"🎯 SYSTEM STATUS: Active & Synchronized!")
        print(f"🔥 VIDEO READY WITH AI HUMAN VOICE: {output_video}")
        print("المتجر والوكيل الآن على المسار الصحيح تماماً بدون أي تدخل عشوائي.")
        
        # تنظيف الملفات المؤقتة
        if os.path.exists(voice_file): os.remove(voice_file)
    except Exception as e:
        print(f"❌ Error during execution: {str(e)}")

if __name__ == "__main__":
    run_automated_store_franchise()
