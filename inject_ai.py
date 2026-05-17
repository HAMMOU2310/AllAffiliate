import os
import json

# قاعدة بيانات اللغات (نظام الحقن الشامل)
content_50 = {
    "AR": "هذا المنتج يتطلب صبراً وأدوات حقيقية. الصدق الجذري: لن تنجح إذا كنت كسولاً.",
    "EN": "Radical Honesty: This requires real effort. It won't work if you are lazy.",
    "FR": "Honnêteté Radicale : Cela demande un réel effort. Ça ne marchera pas si vous êtes paresseux.",
    "ES": "Sinceridad Radical: Esto requiere un esfuerzo real. No funcionará si eres perezoso.",
    "DE": "Radikale Ehrlichkeit: Dies erfordert echte Anstrengung.",
    "TR": "Radikal Dürüstlük: Bu gerçek çaba gerektirir.",
    "RU": "Радикальная честность: это требует реальных усилий.",
    "HI": "कठور ईमानदारी: इसके लिए वास्तविक प्रयास की आवश्यकता है।",
    "ZH": "极端坦诚：这需要真正的努力。",
    "JA": "根本的な正直さ：これには本当の努力が必要です。"
}

def build_global_page(product_path, product_name):
    os.makedirs(product_path, exist_ok=True)
    html_file = os.path.join(product_path, "index.html")
    json_data = json.dumps(content_50, ensure_ascii=False)
    buttons_html = "".join([f'<option value="{lang}">{lang}</option>' for lang in content_50.keys()])
    
    html_template = f"""
    <!DOCTYPE html>
    <html dir="auto">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ background: #020617; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 20px; }}
            .card {{ max-width: 600px; margin: 40px auto; background: #1e293b; padding: 40px; border-radius: 24px; border: 1px solid #334155; }}
            select {{ padding: 10px; border-radius: 8px; background: #334155; color: white; margin-bottom: 20px; width: 100%; }}
            .honesty-box {{ background: #450a0a; padding: 20px; border-radius: 12px; border-right: 4px solid #ef4444; margin: 20px 0; font-weight: bold; font-size: 1.2em; }}
            .buy-btn {{ display: block; background: #2563eb; color: white; padding: 15px; border-radius: 12px; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <select id="langSelect" onchange="updateLang(this.value)">{buttons_html}</select>
            <h1>{product_name}</h1>
            <div id="display_text" class="honesty-box">{content_50['AR']}</div>
            <a href="#" class="buy-btn">GET ACCESS NOW</a>
        </div>
        <script>
            const translations = {json_data};
            function updateLang(lang) {{
                const box = document.getElementById('display_text');
                box.innerText = translations[lang];
                box.style.textAlign = (lang === 'AR') ? 'right' : 'left';
                box.style.direction = (lang === 'AR') ? 'rtl' : 'ltr';
            }}
        </script>
    </body>
    </html>
    """
    with open(html_file, "w", encoding="utf-8") as f: f.write(html_template)
    print(f"--- SUCCESS: Page built at {product_path} ---")

if __name__ == "__main__":
    products = [("store/diy/shedplans", "Shed Plans"), ("store/health/metabolic-fix", "Metabolic Fix")]
    for path, name in products: build_global_page(path, name)
