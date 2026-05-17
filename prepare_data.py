# -*- coding: utf-8 -*-
import json, os
from deep_translator import GoogleTranslator

PRODUCTS_FILE = "products.json"
LANGS = [
    "af", "am", "ar", "az", "bg", "bn", "bs", "ca", "cs", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "ga", "gu", "he", "hi", "hr", "hu", "id", "is", "it", "ja", "kn", "ko", "lt", "lv", "ml", "mr", "ms", "nb", "nl", "pl", "pt", "ro", "ru", "sk", "sl", "sv", "sw", "ta", "te", "th", "tr", "uk", "ur", "vi", "zh-CN"
]

def load_products():
    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

def main():
    products = load_products()
    for p in products:
        print(f"Translating {p['name']}...")
        p['descriptions'] = {}
        # Keep Arabic as source
        source_desc = p['desc']
        for lang in LANGS:
            if lang == 'ar':
                p['descriptions'][lang] = source_desc
                continue
            try:
                p['descriptions'][lang] = GoogleTranslator(source='ar', target=lang).translate(source_desc)
                print(f"  [{lang}] Done")
            except Exception as e:
                print(f"  [{lang}] Failed: {e}")
                p['descriptions'][lang] = source_desc
    save_products(products)
    print("Done!")

if __name__ == "__main__":
    main()
