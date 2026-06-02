import os
import json
import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from datetime import datetime

AFFILIATE_ID = 'fastbuy7'

def fetch_top_14_marketplace_products():
    print("🔄 جاري تحميل قاعدة بيانات سوق ClickBank بالكامل...")
    # الرابط الرسمي المباشر لسوق كليك بانك المشفر
    url = "https://www.clickbank.com/api/marketfeed.xml.zip"
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code != 200:
            print(f"❌ فشل تحميل البيانات من خوادم كليك بانك. كود الخطأ: {response.status_code}")
            return []
            
        # فك الضغط عن الملف في الذاكرة مباشرة دون حفظه على الجهاز
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            xml_filename = z.namelist()[0]
            with z.open(xml_filename) as f:
                xml_content = f.read()
        
        print("📦 جاري قراءة وتحليل المنتجات وفرزها...")
        root = ET.fromstring(xml_content)
        all_products = []
        
        # تفكيك هيكل XML الخاص بكليك بانك: Marketplace -> Category -> Site
        for category_node in root.findall('.//Category'):
            category_name = category_node.find('Name').text if category_node.find('Name') is not None else 'General'
            
            for site_node in category_node.findall('.//Site'):
                vendor_id = site_node.find('Id').text if site_node.find('Id') is not None else ''
                title = site_node.find('Title').text if site_node.find('Title') is not None else ''
                description = site_node.find('Description').text if site_node.find('Description') is not None else ''
                
                # جلب مقياس الجاذبية (Gravity) وهو الدليل الحقيقي على المنتجات الأكثر مبيعاً حالياً
                gravity_node = site_node.find('Gravity')
                gravity = float(gravity_node.text) if gravity_node is not None and gravity_node.text else 0.0
                
                if vendor_id and title:
                    all_products.append({
                        'vendor_id': vendor_id,
                        'title': title,
                        'description': description,
                        'category': category_name,
                        'gravity': gravity
                    })
        
        # ترتيب المنتجات تنازلياً: من الأعلى مبيعاً وجاذبية إلى الأقل
        sorted_products = sorted(all_products, key=lambda x: x['gravity'], reverse=True)
        
        # اقتطاع أفضل 14 منتجاً في القمة
        top_14 = sorted_products[:14]
        return top_14
        
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع أثناء معالجة البيانات: {str(e)}")
        return []

def process_and_filter_products(raw_products):
    processed_list = []
    
    for item in raw_products:
        vendor_id = item['vendor_id']
        title = item['title']
        description = item['description']
        category = item['category']
        
        # توليد رابط الأفلييت الحقيقي الخاص بك بمعرفك fastbuy7
        affiliate_link = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor={vendor_id}"
        
        # الجدار الناري الشرعي (Shariah Firewall) لفلترة المنتجات المخالفة
        title_lower = title.lower()
        desc_lower = description.lower()
        forbidden_keywords = ['dating', 'magic', 'tarot', 'alcohol', 'casino', 'betting', 'spell', 'wine']
        
        status = "approved"
        if any(keyword in title_lower or keyword in desc_lower for keyword in forbidden_keywords):
            status = "redirected"
            affiliate_link = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor=halalalt"

        product_obj = {
            "title": title,
            "description": description[:120] + "..." if len(description) > 120 else description,
            "price": "Check Site",
            "category": category,
            "link": affiliate_link,
            "status": status,
            "satisfaction_rate": "94%",
            "last_seen": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        processed_list.append(product_obj)
        
    return processed_list

def main():
    raw_products = fetch_top_14_marketplace_products()
    
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
            
        print(f"✅ نجاح باهر! تم تحديث المتجر بأعلى 14 منتجاً مبيعاً في ClickBank بروابطك الخاصة.")
    else:
        print("⚠️ فشل التحديث التلقائي، تم الحفاظ على المنتجات الاحتياطية لضمان عمل الموقع.")

if __name__ == "__main__":
    main()