import os
import json
import sys

# ضمان أن الطباعة تستخدم UTF-8 لتجنب أخطاء الترميز في الويندوز
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

PROJECT_CONFIG = {
    "store_path": "store",
    "products": [
        {"id": "shedplans", "category": "diy", "name": "Shed Plans & Blueprints"},
        {"id": "metabolic-fix", "category": "health", "name": "Metabolic Fix System"}
    ],
    "languages_count": 50
}

def sync_engine():
    print("--- Starting AI Build Engine ---")
    
    for product in PROJECT_CONFIG["products"]:
        # استخدام المسارات الصحيحة حسب نظام التشغيل
        path = os.path.join(PROJECT_CONFIG["store_path"], product["category"], product["id"])
        index_file = os.path.join(path, "index.html")
        
        if os.path.exists(index_file):
            # استخدام نصوص بسيطة للطباعة لتجنب مشاكل charmap
            print(f"SUCCESS: Product Found -> {product['name']}")
        else:
            print(f"WARNING: Missing folder at -> {path}")

if __name__ == "__main__":
    sync_engine()
    print("--- Build Complete: System Ready ---")
