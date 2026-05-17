import os
import subprocess
import json

def get_product_data():
    # جلب بيانات المنتج من الملف الذي أنشأه Fetcher
    try:
        with open("current_products.json", "r", encoding="utf-8") as f:
            return json.load(f)[0] # نأخذ أول منتج كعينة (Shed Plans)
    except:
        return {"id": "shedplans", "name": "Shed Plans", "text": "Radical Honesty: It requires real work!"}

def create_raw_video():
    print("--- 🎬 AI Video Studio is warming up ---")
    
    # 1. تحديد المسارات
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    export_folder = os.path.join(desktop, 'Social_Videos_Export')
    if not os.path.exists(export_folder): os.makedirs(export_folder)
    
    product = get_product_data()
    output_file = os.path.join(export_folder, f"{product['id']}_raw.mp4")
    
    # 2. أمر FFmpeg السينمائي:
    # سيقوم بصناعة فيديو مدته 10 ثوانٍ بخلفية تدرجية متحركة ونص احترافي
    # ملاحظة: هذا الكود يخلق فيديو تقني سريع، سنضيف الصور الحقيقية في الخطوة القادمة
    cmd = [
        'ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x1e293b:s=1080x1920:d=10',
        '-vf', f"drawtext=text='{product['name']}':fontcolor=white:fontsize=80:x=(w-text_w)/2:y=(h-text_h)/2-200, " +
               f"drawtext=text='{product['text']}':fontcolor=yellow:fontsize=50:x=(w-text_w)/2:y=(h-text_h)/2+200, " +
               "fade=in:st=0:d=1, fade=out:st=9:d=1",
        '-c:v', 'libx264', '-t', '10', '-pix_fmt', 'yuv420p', output_file
    ]
    
    print(f"Creating raw video for: {product['name']}...")
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"SUCCESS: Raw video saved to {output_file}")
    except Exception as e:
        print(f"ERROR creating video: {e}")

if __name__ == "__main__":
    create_raw_video()
