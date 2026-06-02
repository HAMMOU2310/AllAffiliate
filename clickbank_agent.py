# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

# --- إعدادات النظام وعقل الأفلييت ---
AFFILIATE_ID = "fastbuy7"
DB_FILE = "products.json"

# --- جدار الحماية الشرعي (Shariah Compliance Firewall) ---
BLOCKED = ["casino", "gamble", "porn", "loan", "interest", "astrology", "get rich quick", "poker", "betting"]

def get_alternative_product(category):
    """[منطق التوجيه التلقائي]: البحث عن منتج بديل مشابه عند حظر المنتج الأصلي"""
    alternatives = {
        "Wealth": "cb_investment_education", 
        "Health": "cb_fitness_training",
        "Spirituality": "cb_mental_wellbeing"
    }
    return alternatives.get(category, "cb_general_health")

def fetch_trending_products():
    """محاكاة وتوليد المنتجات الرابحة الـ 14 واختبار جدار الحماية الشرعي لتوفير بيانات متناسقة 100%"""
    return [
        {
            "id": "cb_alpilean", 
            "vendor": "alpilean", 
            "title": "Alpilean - Ice Weight Loss", 
            "category": "Health", 
            "description": "Exotic alpine secret for healthy weight loss. Helps optimize metabolism.", 
            "price": "$59", 
            "refund_rate": "8%",
            "satisfaction_rate": "92%"
        },
        {
            "id": "cb_casino_master", 
            "vendor": "casinotip", 
            "title": "Casino Betting Secrets", 
            "category": "Wealth", 
            "description": "Learn how to gamble and win big at the poker casino table instantly.", 
            "price": "$99", 
            "refund_rate": "45%",
            "satisfaction_rate": "55%"
        },
        {
            "id": "cb_javaburn", 
            "vendor": "javaburn", 
            "title": "Java Burn - Coffee Formula", 
            "category": "Health", 
            "description": "A natural formula to combine with your daily coffee. It is effective but shipping can be slow.", 
            "price": "$49", 
            "refund_rate": "11%",
            "satisfaction_rate": "89%"
        },
        {
            "id": "cb_denticore", 
            "vendor": "denticore", 
            "title": "DentiCore - Advanced Oral Care", 
            "category": "Health", 
            "description": "Supports healthy teeth and gums. Safe ingredients, results require up to 30 days of consistent usage.", 
            "price": "$69", 
            "refund_rate": "6%",
            "satisfaction_rate": "94%"
        },
        {
            "id": "cb_puravive",
            "vendor": "puravive",
            "title": "Puravive - Exotic Dissolve",
            "category": "Weight Loss",
            "description": "Natural exotic ingredients targeting low brown adipose tissue for fat burning.",
            "price": "$39",
            "refund_rate": "5%",
            "satisfaction_rate": "95%"
        },
        {
            "id": "cb_livpure",
            "vendor": "livpure",
            "title": "Liv Pure - Liver Optimization",
            "category": "Health",
            "description": "Purify your liver and accelerate fat burning naturally and safely.",
            "price": "$69",
            "refund_rate": "9%",
            "satisfaction_rate": "91%"
        },
        {
            "id": "cb_sugardefender",
            "vendor": "sugardef",
            "title": "Sugar Defender - Blood Sugar",
            "category": "Wellness",
            "description": "Advanced bio-engineered formula for optimal glucose and daily energy support.",
            "price": "$49",
            "refund_rate": "7%",
            "satisfaction_rate": "93%"
        },
        {
            "id": "cb_prodentim",
            "vendor": "prodentim",
            "title": "ProDentim - Oral Probiotics",
            "category": "Health",
            "description": "Doctor-formulated mix of 3.5 billion probiotics designed for gum and teeth health.",
            "price": "$69",
            "refund_rate": "4%",
            "satisfaction_rate": "96%"
        },
        {
            "id": "cb_sightcare",
            "vendor": "sightcare",
            "title": "Sight Care - Vision Support",
            "category": "Wellness",
            "description": "Supports healthy eye tissue and maintains strong night vision naturally.",
            "price": "$49",
            "refund_rate": "8%",
            "satisfaction_rate": "92%"
        },
        {
            "id": "cb_glucotrust",
            "vendor": "glucotrust",
            "title": "GlucoTrust - Sleep & Sugar",
            "category": "Wellness",
            "description": "Promotes healthy blood sugar levels while supporting deep, restful sleep.",
            "price": "$69",
            "refund_rate": "10%",
            "satisfaction_rate": "90%"
        },
        {
            "id": "cb_leanbiome",
            "vendor": "leanbiome",
            "title": "LeanBiome - Clear Gut",
            "category": "Weight Loss",
            "description": "Formulated with elite green select phytosome to clear the gut pathways.",
            "price": "$59",
            "refund_rate": "6%",
            "satisfaction_rate": "94%"
        },
        {
            "id": "cb_cortexi",
            "vendor": "cortexi",
            "title": "Cortexi - Hearing & Focus",
            "category": "Health",
            "description": "Provides 360-degree hearing support and mental sharpness with natural drops.",
            "price": "$49",
            "refund_rate": "5%",
            "satisfaction_rate": "95%"
        },
        {
            "id": "cb_betabeat",
            "vendor": "betabeat",
            "title": "BetaBeat - Energy Formula",
            "category": "Wellness",
            "description": "Highly effective energy and blood sugar support using pure plant extracts.",
            "price": "$49",
            "refund_rate": "12%",
            "satisfaction_rate": "88%"
        },
        {
            "id": "cb_metanail",
            "vendor": "metanail",
            "title": "MetaNail - Serum Pro",
            "category": "Health",
            "description": "Advanced complex designed to support healthy nails and beautiful feet.",
            "price": "$59",
            "refund_rate": "3%",
            "satisfaction_rate": "97%"
        }
    ]

def run_smart_agent():
    print("⏳ بدأت عملية جدار الحماية الشرعي والأرشفة الذكية...")
    raw_products = fetch_trending_products()
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                db = json.load(f)
            except json.JSONDecodeError:
                db = {"products": []}
    else:
        db = {"products": []}
        
    current_archive = {p['id']: p for p in db.get('products', [])}
    
    for prod in raw_products:
        full_text = (prod['title'] + " " + prod['description']).lower()
        
        # 1. تطبيق جدار الحماية الشرعي والتوجيه التلقائي للمنتج البديل الحلال
        if any(word in full_text for word in BLOCKED):
            print(f"🚫 [حظر شرعي]: تم اكتشاف منتج مخالف '{prod['title']}'. يتم تحويله تلقائياً لمنتج بديل حلال...")
            prod['id'] = get_alternative_product(prod['category'])
            prod['title'] = "Alternative Halal Wealth & Investment Guide"
            prod['description'] = "A fully compliant ethical financial literacy and investment program. Safe and certified."
            prod['vendor'] = "cleanwealth"
            prod['price'] = "$47"
            prod['refund_rate'] = "4%"
            prod['satisfaction_rate'] = "96%"
            prod['status'] = "redirected"
        else:
            prod['status'] = "compliant"
            
        p_id = prod['id']
        
        # 2. بناء كتلة الميتا داتا الذكية + وحدة USDC المالية
        prod['metadata'] = {
            "target_language": "ar",
            "refund_rate": prod.get('refund_rate', "10%"),
            "risk_level": "High" if int(prod.get('refund_rate', "0%").replace('%','')) > 20 else "Low",
            "recommended_posting_time": "19:00 GMT",
            "usdc_aggregation_recommendation": "Hold earnings until $500, then automatically swap to USDC via Affise/Heleket",
            "usdc_conversion_ready": True,
            "shariah_compliant": "Yes" if prod['status'] == "compliant" else "Re-routed to Safe Alternative"
        }
        
        # 3. دمج التحليلات المتقدمة: المحتوى المضاد، الندرة العكسية، وقسم الفلترة التلقائية
        prod['who_is_it_for'] = "For individuals dedicated to long-term results with realistic expectations."
        prod['who_is_it_not_for'] = "Not for those looking for magical instant results, overnight fixes, or illegal gains."
        prod['reverse_scarcity'] = f"{prod.get('satisfaction_rate', '90%')} are completely satisfied, but {prod.get('refund_rate', '10%')} complained about shipping times or strictly required effort."
        
        # ربط الروابط بالمعرف الخاص بك وتثبيت التوقيت والأرشفة الذكية الدائمة
        prod['link'] = f"https://hop.clickbank.net/?affiliate={AFFILIATE_ID}&vendor={prod['vendor']}"
        prod['date_added'] = current_archive.get(p_id, {}).get('date_added', datetime.now().strftime("%Y-%m-%d"))
        prod['last_seen'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        current_archive[p_id] = prod
        print(f"✅ [تمت الأرشفة]: {prod['title']}")

    db['products'] = list(current_archive.values())
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    print(f"🎯 اكتملت العملية بنجاح! إجمالي الأرشيف الدائم: {len(db['products'])} منتج.")

if __name__ == "__main__":
    run_smart_agent()