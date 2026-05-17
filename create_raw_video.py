import subprocess
import os
import sys
import codecs
import urllib.request

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def create_video_with_real_audio():
    print("--- 🎙️ GENERATING VIDEO WITH REAL AUDIO ---")
    
    img1 = "image1.jpg"
    img2 = "image2.jpg"
    audio_file = "background_music.mp3"
    
    # رابط لملف صوتي حقيقي ومسموع (موسيقى هادئة وخفيفة خالية من الحقوق)
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    
    try:
        if not os.path.exists(img1) or not os.path.exists(img2):
            print("❌ الصور غير موجودة! يرجى تشغيل السكريبت السابق أولاً.")
            return
            
        print("Downloading real background audio track (Lightweight)...")
        urllib.request.urlretrieve(audio_url, audio_file)
        print("✅ Audio downloaded successfully!")
        
    except Exception as e:
        print(f"❌ Audio Download Error: {str(e)}")
        return

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    output_video = os.path.join(export_folder, "ShedPlans_Raw.mp4")

    print("Mixing moving images with real audio track using FFmpeg...")
    
    # استبدال المسار الصامت بملف الصوت الحقيقي background_music.mp3
    cmd = [
        'ffmpeg', '-y',
        '-loop', '1', '-t', '3', '-i', img1,
        '-loop', '1', '-t', '3', '-i', img2,
        '-i', audio_file,
        '-filter_complex',
        "[0:v]scale=2160x3840,zoompan=z='min(zoom+0.0015,1.5)':d=75:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,setsar=1,setpts=PTS-STARTPTS[v1]; "
        "[1:v]scale=2160x3840,zoompan=z='min(zoom+0.0015,1.5)':d=75:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920,setsar=1,setpts=PTS-STARTPTS[v2]; "
        "[v1][v2]concat=n=2:v=1:a=0[v]",
        '-map', '[v]', '-map', '2:a',
        '-c:v', 'libx264', '-c:a', 'aac', '-t', '6', '-pix_fmt', 'yuv420p',
        output_video
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"🎉 SUCCESS: Video with REAL AUDIO generated at: {output_video}")
        
        # تنظيف ملف الصوت المؤقت لتوفير المساحة
        if os.path.exists(audio_file):
            os.remove(audio_file)
            
    except Exception as e:
        print(f"❌ FFmpeg Error: {str(e)}")

if __name__ == "__main__":
    create_video_with_real_audio()
