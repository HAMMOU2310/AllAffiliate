# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

# --- إعدادات النظام ---
AFFILIATE_ID = "fastbuy7"
DB_FILE = "products.json"

# --- جدار الحماية الشرعي (Shariah Compliance Firewall) ---
BLOCKED = ["casino", "gamble", "porn", "loan", "interest", "astrology", "get rich quick"]

def get_alternative_product(category):
    """[منطق التوجيه التلقائي]: البحث عن منتج بديل مشابه عند حظر المنتج الأصلي"""
    alternatives = {
        "Wealth": "cb_investment_education", 
        "Health": "cb_fitness_training",
        "Spirituality": "cb_mental_wellbeing"
    }
    return alternatives.get(category, "cb_general_health")

def process_product(prod):
    """تطبيق منطق جدار الحماية + JSON Metadata"""
    # 1. فحص المحتوى
    full_text = (prod['title'] + " " + prod['description']).lower()
    if any(word in full_text for word in BLOCKED):
        print(f"🚫 [حظر]: {prod['title']} | يتم التوجيه للمنتج البديل...")
        prod['id'] = get_alternative_product(prod['category']) # استبدال بالبديل
        prod['status'] = "redirected"
    
    # 2. بناء كتلة الميتا (المرحلة الثانية)
    prod['metadata'] = {
        "refund_rate": prod.get('refund_rate', "10%"),
        "risk_level": "High" if prod.get('refund_rate', "0") > "20%" else "Low",
        "usdc_conversion_ready": True,
        "shariah_compliant": True if prod.get('status') != "redirected" else "Re-routed"
    }
    
    # 3. إعداد المحتوى المضاد (Antagonist Content)
    prod['who_is_it_not_for'] = "Not for those seeking overnight results without effort."
    return prod

# --- التنفيذ ---
# هذا الكود سيُدمج في الـ Workflow ليقوم بفلترة المنتجات يومياً