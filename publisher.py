import subprocess
import os
import sys
import codecs
import time
import ctypes

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def run_publishing_sequence():
    print("--- STARTING DIRECT CHROME AGENT (NO DRIVER NEEDED) ---")
    
    username = os.getlogin()
    user_data_path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data"
    target_url = "https://business.facebook.com/latest/reels_composer"
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    
    cmd = [
        chrome_path,
        target_url,
        f"--user-data-dir={user_data_path}",
        "--profile-directory=Default",
        "--disable-blink-features=AutomationControlled",
        "--no-first-run"
    ]
    
    try:
        print("Launching Chrome and opening Facebook Reels Composer...")
        subprocess.Popen(cmd)
        
        # الانتظار حتى تفتح الصفحة بالكامل (زدنا الوقت ليتناسب مع سرعة الإنترنت عندك)
        print("Waiting 20 seconds for the upload page to load completely...")
        time.sleep(20)
        
        # نص المنشور الإعلاني ورابط كليك بانك الخاص بك (الصدق الجذري)
        post_text = "Build your dream shed today with 16,000 professional plans! Get instant access here: https://your-clickbank-link.com"
        
        print(f"Agent Ready to inject text and select video from your desktop folder.")
        print("--- Next Phase: Automation of Clicks and Monetization Toggles ---")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    run_publishing_sequence()
