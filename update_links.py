import os

# ضع روابطك هنا (استبدل الروابط الوهمية بروابطك الحقيقية لاحقاً)
LINKS = {
    "shedplans": "https://www.clickbank.com/example-shed-plans",
    "metabolic-fix": "https://www.clickbank.com/example-metabolic"
}

def inject_links():
    base_path = "store"
    # البحث في المجلدات عن ملفات index.html
    for root, dirs, files in os.walk(base_path):
        if "index.html" in files:
            file_path = os.path.join(root, "index.html")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # تحديد المنتج بناءً على اسم المجلد
            for prod_id, link in LINKS.items():
                if prod_id in root:
                    # استبدال علامة # أو الرابط القديم بالرابط الجديد
                    new_content = content.replace('href="#"', f'href="{link}"')
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated link for: {prod_id}")

if __name__ == "__main__":
    inject_links()
