# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

AFFILIATE_ID = "fastbuy7"
DB_FILE = "products.json"

def fetch_trending_products():
    """
    محاكاة لجلب المنتجات الرابحة من كليك بانك بنظام النيشات الستة الرئيسية.
    يمكنك لاحقاً ربطها بـ API الخاص بكليك بانك إن أردت.
    """
    # عينة من أفضل المنتجات مبيعاً حالياً في كليك بانك
    return [
        {"id": "cb_alpilean", "vendor": "alpilean", "title": "Alpilean - Weight Loss", "category": "Health & Fitness", "description": "The premier alpine secret for healthy weight loss.", "price": "$59"},
        {"id": "cb_javaburn", "vendor": "javaburn", "title": "Java Burn - Coffee Slimming", "category": "Health & Fitness", "description": "The world's first patent-pending formula to boost metabolism.", "price": "$49"},
        {"id": "cb_puravive", "vendor": "puravive", "title": "Puravive - Exotic Dissolve", "category": "Weight Loss", "description": "Natural exotic ingredients targeting low brown adipose tissue.", "price": "$39"},
        {"id": "cb_livpure", "vendor": "livpure", "title": "Liv Pure - Liver Optimization", "category": "Health", "description": "Purify your liver and accelerate fat burning naturally.", "price": "$69"},
        {"id": "cb_sugardefender", "vendor": "sugardef", "title": "Sugar Defender - Blood Sugar", "category": "Wellness", "description": "Advanced bio-engineered formula for glucose support.", "price": "$49"},
        {"id": "cb_denticore", "vendor": "denticore", "title": "DentiCore - Oral Health", "category": "Dental", "description": "Deep oxygenation process supporting healthy teeth and gums.", "price": "$59"}
    ]

def run_smart_archive():
    print("⏳ بدأت عملية الأرشفة الذكية وتحديث المنتجات...")
    
    # 1. جلب البيانات الجديدة
    new_prods = fetch_trending_products()
    
    # 2. قراءة الأرشيف الحالي
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                db = json.load(f)
            except json.JSONDecodeError:
                db = {"products": []}
    else:
        db = {"products": []}
        
    current_archive = {p['id']: p for p in db.get('products', [])}
    
    # 3. دمج البيانات (الأرشفة الذكية)
    for prod in new_prods:
        p_id = prod['id']
        # صناعة رابط الأفلييت الخاص بك تلقائياً بالمعرف fastbuy7
        prod['link'] = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor={prod['vendor']}"
        prod['date_added'] = current_archive.get(p_id, {}).get('date_added', datetime.now().strftime("%Y-%m-%d"))
        prod['last_seen'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # التحديث أو الإضافة دون حذف القديم
        current_archive[p_id] = prod

    # حفظ الأرشيف الكامل والمحدث
    db['products'] = list(current_archive.values())
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
        
    print(f"✅ تم التحديث! إجمالي المنتجات المحفوظة في الأرشيف الدائم: {len(db['products'])}")

if __name__ == "__main__":
    run_smart_archive()