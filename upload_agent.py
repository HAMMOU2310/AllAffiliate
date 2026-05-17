import pyautogui
import pyperclip
import time
import sys
import codecs

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def auto_upload_video():
    print("--- 🤖 AGENT: AUTO-UPLOAD SEQUENCE INITIATED ---")
    print("التعليمات:")
    print("1. اذهب فوراً إلى متصفح كروم المفتوح على صفحة الفيسبوك.")
    print("2. اضغط بيدك على زر 'إضافة فيديو' (Add Video).")
    print("3. اترك الماوس والكيبورد تماماً! الوكيل سيتولى الباقي.")
    print("--------------------------------------------------")
    
    # عد تنازلي لـ 15 ثانية لتجهيز نفسك
    for i in range(15, 0, -1):
        print(f"Agent taking over in {i} seconds...")
        time.sleep(1)
        
    print("\n--- AGENT IS NOW TYPING ---")
    
    # 1. إدخال مسار الفيديو في نافذة الويندوز والضغط على Enter
    video_path = r"C:\Users\hamm\Desktop\Social_Videos_Export\ShedPlans_Raw.mp4"
    pyperclip.copy(video_path) # نسخ المسار
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'v') # لصق المسار
    time.sleep(1)
    pyautogui.press('enter') # تأكيد الرفع
    
    print("Video selected! Waiting 15 seconds for Facebook to process...")
    time.sleep(15)
    
    # 2. الانتقال لحقل النص وكتابة الوصف (استخدام زر Tab للوصول لحقل الوصف)
    # ملاحظة: في فيسبوك، عادة بعد رفع الفيديو يمكن الوصول لحقل النص بضغطة Tab
    pyautogui.press('tab', presses=2, interval=0.5) 
    
    promo_text = "Build your dream shed today! 16,000 Woodworking Plans 🛠️ Get access here: https://your-clickbank-link.com"
    pyperclip.copy(promo_text)
    pyautogui.hotkey('ctrl', 'v')
    
    print("SUCCESS: Text injected. Review the post on your screen!")

if __name__ == "__main__":
    auto_upload_video()
