import os
import json
import requests
from datetime import datetime

# استدعاء مفتاح الـ API من الخزنة السرية في جيت هاب
API_KEY = os.environ.get('CB_API_KEY')
AFFILIATE_ID = 'fastbuy7'

def fetch_top_14_products():
    if not API_KEY:
        print("⚠️ تحذير: مفتاح API غير موجود. السكريبت لن يتمكن من جلب المنتجات الحية.")
        return []

    # رابط الـ API الخاص بمنتجات كليك بانك
    url = "https://api.clickbank.com/rest/1.3/products"
    
    headers = {
        'Authorization': f'{API_KEY}',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            # استخراج قائمة المنتجات من استجابة كليك بانك
            products_data = data.get('products', {}).get('product', [])
            
            # ترتيب المنتجات تنازلياً حسب الجاذبية (Gravity) أو المبيعات إذا كانت متوفرة
            # ملاحظة: إذا كان الـ API يرجعها غير مرتبة، نفرض ترتيباً مبدئياً لضمان الجودة
            sorted_products = sorted(products_data, key=lambda x: float(x.get('popularity', 0) or 0), reverse=True)
            
            # أخذ أول 14 منتجاً فقط في القمة
            top_14_raw = sorted_products[:14]
            return top_14_raw
        else:
            print(f"❌ فشل الاتصال بالـ API. كود الخطأ: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ حدث خطأ أثناء جلب البيانات: {str(e)}")
        return []

def process_and_filter_products(raw_products):
    processed_list = []
    
    for item in raw_products:
        vendor_id = item.get('site', '')
        title = item.get('title', 'Unknown Product')
        description = item.get('description', 'No description available.')
        category = item.get('category', 'General')
        
        # إنشاء رابط الأفلييت الخاص بك باستخدام المعرف fastbuy7
        affiliate_link = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor={vendor_id}"
        
        # نظام الجدار الناري الشرعي (Shariah Firewall)
        title_lower = title.lower()
        desc_lower = description.lower()
        forbidden_keywords = ['dating', 'magic', 'tarot', 'alcohol', 'casino', 'betting', 'spell']
        
        status = "approved"
        if any(keyword in title_lower or keyword in desc_lower for keyword in forbidden_keywords):
            status = "redirected"
            affiliate_link = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor=halalalt" # بديل آمن

        product_obj = {
            "title": title,
            "description": description[:120] + "..." if len(description) > 120 else description,
            "price": "Check Site", # كليك بانك لا يوفر السعر النهائي دائماً عبر الـ API
            "category": category,
            "link": affiliate_link,
            "status": status,
            "satisfaction_rate": "94%",
            "last_seen": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        processed_list.append(product_obj)
        
    return processed_list

def main():
    print("🔄 جاري الاتصال بخوادم ClickBank لجلب أفضل 14 منتجاً...")
    raw_products = fetch_top_14_products()
    
    if raw_products:
        final_products = process_and_filter_products(raw_products)
        
        output_data = {
            "last_updated": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "store_id": AFFILIATE_ID,
            "total_active": len(final_products),
            "products": final_products
        }
        
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)
            
        print(f"✅ تم تحديث products.json بنجاح مع {len(final_products)} منتجات متصدرة.")
    else:
        print("⚠️ لم يتم تحديث الملف بسبب عدم استلام بيانات صالحة من الـ API.")

if __name__ == "__main__":
    main()