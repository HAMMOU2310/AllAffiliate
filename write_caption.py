import pyautogui
import pyperclip
import time
import sys
import codecs

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def just_type_caption():
    print("--- 🤖 AGENT: WRITING CAPTION ---")
    print("أمامك 5 ثوانٍ: تأكد من النقر بالماوس داخل مربع نص الوصف على المتصفح!")
    
    for i in range(5, 0, -1):
        print(f"Writing in {i}...")
        time.sleep(1)
    
    # النص الجذاب مع الرابط (تأكد من استبدال الرابط برابط كليك بانك الحقيقي لاحقاً)
    promo_text = "Build your dream shed today! 16,000 Woodworking Plans 🛠️ Get instant blueprints here: https://your-clickbank-link.com"
    
    pyperclip.copy(promo_text)
    pyautogui.hotkey('ctrl', 'v')
    print("SUCCESS: Text injected into the browser!")

if __name__ == "__main__":
    just_type_caption()
