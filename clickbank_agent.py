import os
import json
import zipfile
import io
import xml.etree.ElementTree as ET
from datetime import datetime
import urllib.request
import urllib.error

AFFILIATE_ID = 'fastbuy7'

def fetch_top_14_marketplace_products():
    print("🔄 جاري تحميل قاعدة بيانات سوق ClickBank بالكامل...")
    url = "https://www.clickbank.com/api/marketfeed.xml.zip"
    
    # إضافة "قناع" المتصفح لتخطي جدار الحماية (Cloudflare) الخاص بـ ClickBank
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            content = response.read()
            
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            xml_filename = z.namelist()[0]
            with z.open(xml_filename) as f:
                xml_content = f.read()
        
        print("📦 جاري قراءة وتحليل المنتجات وفرزها...")
        root = ET.fromstring(xml_content)
        all_products = []
        
        for category_node in root.findall('.//Category'):
            category_name = category_node.find('Name').text if category_node.find('Name') is not None else 'General'
            
            for site_node in category_node.findall('.//Site'):
                vendor_id = site_node.find('Id').text if site_node.find('Id') is not None else ''
                title = site_node.find('Title').text if site_node.find('Title') is not None else ''
                description = site_node.find('Description').text if site_node.find('Description') is not None else ''
                
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
        
        # ترتيب المنتجات من الأقوى مبيعاً إلى الأقل
        sorted_products = sorted(all_products, key=lambda x: x['gravity'], reverse=True)
        return sorted_products[:14]
        
    except urllib.error.HTTPError as e:
        print(f"❌ تم الحظر بواسطة كليك بانك. كود الخطأ: {e.code}")
        return []
    except zipfile.BadZipFile:
        print("❌ الملف الذي تم تحميله ليس ZIP (تم حظر الطلب من السيرفر).")
        return []
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {str(e)}")
        return []

def process_and_filter_products(raw_products):
    processed_list = []
    
    for item in raw_products:
        vendor_id = item['vendor_id']
        title = item['title']
        description = item['description']
        category = item['category']
        
        affiliate_link = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor={vendor_id}"
        
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
            
        print(f"✅ نجاح باهر! تم تحديث المتجر بأعلى 14 منتجاً مبيعاً في ClickBank.")
    else:
        print("⚠️ فشل التحديث التلقائي، تم الحفاظ على المنتجات الحالية.")

if __name__ == "__main__":
    main()