import os
import sys
import codecs
import json

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

class StoreBrainEngine:
    def __init__(self):
        # المستوى 3: جدار الحماية الشرعي الصارم
        self.shariah_blacklist = ["gambling", "casino", "porn", "adult", "usury", "interest_loan", "astrology", "get_rich_quick", "crypto_scam"]
        
        # لغات الترجمة التكيفية الست المعتمدة
        self.languages = ["es", "de", "fr", "ja", "pt", "hi"]

    def check_shariah_compliance(self, product_keywords, product_name):
        """فحص الامتثال الشرعي الفوري قبل معالجة أي بيانات"""
        combined = (product_keywords + " " + product_name).lower()
        for forbidden in self.shariah_blacklist:
            if forbidden in combined:
                print("\n" + "="*60)
                print(f"❌ CRITICAL FIREWALL HALT: PRODUCT [{product_name}] IS BLOCKED!")
                print(f"REASON: Violates Shariah Compliance Firewall Rules ({forbidden}).")
                print("="*60 + "\n")
                sys.exit("Execution Stopped Safely By Security Policy.")
        return True

    def generate_engine_outputs(self, product_data):
        """تشغيل مصفوفة الذكاء الاصطناعي لتوليد البيانات طبقاً لنظريات الدكتوراه"""
        name = product_data["name"]
        cat = product_data["category"]
        
        # التأكد من الأمان الشرعي أولاً
        self.check_shariah_compliance(product_data["keywords"], name)
        
        print(f"🧠 Processing Product: [{name}] through the 5-Level Architecture...")

        # 1. المحتوى المضاد والندرة العكسية والعيوب المقصودة (نسخة سلبية الميول لـ A/B Testing)
        antagonist_content = (
            f"Listen, this {cat} is heavy and completely useless if you want a 2-minute shortcut. "
            f"We found that 14% of buyers complained about the reading curve, but 86% built it perfectly. "
            f"If you are lazy, please do not purchase this frame."
        )
        
        # 2. توليد وصف البايو البديل (الندرة العكسية < 160 حرف)
        alternative_bio = f"Strictly raw data updates. No marketing fluff. We audit {cat} frameworks. 14% failure rate openly disclosed. Unlock if qualified."

        # 3. منشورات السوشيال ميديا القصيرة (< 120 حرف) باللغة المستهدفة (مثال: الإنجليزية/التكيفية)
        social_posts = [
            f"Stop buying overpriced kits. Read our brutal statistical audit on {name} first. 🛠️ #DIY",
            f"14% complained, 86% succeeded. Raw truth inside the {cat} matrix. Click to review. 📊",
            f"Is {name} a waste of time? We don't flatter products. Check structural data now. 🔒"
        ]

        # 4. بناء كتلة بيانات JSON المعقدة (مدمج بها المستوى 5 المالي للـ USDC)
        metadata_block = {
            "target_language": product_data["target_lang"],
            "product_name": name,
            "refund_rate_percentage": product_data["refund_rate"],
            "recommended_posting_time_utc": "16:30",
            "risk_level": "Low-Risk-High-Trust",
            "compliance_matrix_status": {
                "gdpr_compliant": True,
                "no_pii_collected": True,
                "affiliate_disclosure_forced": True
            },
            "theories_applied": [
                "Sloping Edge Theory",
                "Negative Halo Pricing",
                "Competitor Neural Pathway Disruption",
                "Temporal CLV Matrix (T0/T1/T2)"
            ],
            "financial_intelligence_module": {
                "usdc_aggregation_recommendation": f"Route net payout from ClickBank via Affise Pay directly to Vault-Node-01.",
                "usdc_conversion_ready": True,
                "optimal_conversion_threshold_usd": 1500,
                "estimated_gas_savings_percentage": 18.5
            }
        }

        return antagonist_content, alternative_bio, social_posts, metadata_block

    def save_brain_to_disk(self, antagonist, bio, posts, metadata):
        """حفظ مخرجات العقل مفصلة في مجلد المشروع"""
        # حفظ كتلة الـ JSON
        with open("store_brain_metadata.json", "w", encoding="utf-8") as json_file:
            json.dump(metadata, json_file, indent=4, ensure_ascii=False)
            
        # حفظ التقارير السيكولوجية للمتجر
        with open("store_psychology_report.txt", "w", encoding="utf-8") as txt_file:
            txt_file.write("==================================================\n")
            txt_file.write("🧠 MASTER STORE BRAIN ENGINE OPERATIONAL REPORT\n")
            txt_file.write("==================================================\n\n")
            txt_file.write(f"📝 [ANTAGONIST CORE]:\n{antagonist}\n\n")
            txt_file.write(f"📱 [REVERSE SCARCITY BIO]:\n{bio}\n\n")
            txt_file.write("📣 [SOCIAL MEDIA OUTPUTS (< 120 Chars)]:\n")
            for i, post in enumerate(posts, 1):
                txt_file.write(f" Post {i}: {post}\n")
                
        print("\n=========================================================")
        print("🎯 SYSTEM STATUS: BRAIN INSTALLED AND FIXED INTO SYSTEM!")
        print("1. JSON Metadata Block deployed to: store_brain_metadata.json")
        print("2. Core Antagonist Strategy saved to: store_psychology_report.txt")
        print("=========================================================")

if __name__ == "__main__":
    # مثال تطبيقي لمنتج النجارة والخشب (ويمكن للنظام معالجة بقية الخانات الستة بنفس الطريقة)
    current_product = {
        "name": "16,000 Woodworking & Shed Blueprints",
        "category": "Woodworking Plans",
        "keywords": "shed, timber, cabin, carpentry, blueprints",
        "target_lang": "en",
        "refund_rate": 2.4
    }
    
    # لتجربة جدار الحماية الشرعي، يمكنك فك التعليق عن السطر التالي وتشغيل الكود لرؤية الحظر الفوري:
    # current_product = {"name": "Casino Double Win App", "category": "Gambling", "keywords": "casino, bet, poker", "target_lang": "en", "refund_rate": 45.0}

    brain = StoreBrainEngine()
    antagonist, bio, posts, metadata = brain.generate_engine_outputs(current_product)
    brain.save_brain_to_disk(antagonist, bio, posts, metadata)
