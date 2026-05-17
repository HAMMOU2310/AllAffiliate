import os

# بنية الموقع الكاملة
products = ["shedplans", "metabolic-fix", "brain-training", "woodworking-mastery", "keto-diet"]

def create_real_site():
    # 1. إنشاء مجلد المتجر الرئيسي
    if not os.path.exists('store'):
        os.makedirs('store')
        print("✅ تم إنشاء مجلد /store/")

    # 2. إنشاء المجلدات الفرعية والملفات لكل منتج
    for p in products:
        path = f"store/{p}"
        if not os.path.exists(path):
            os.makedirs(path)
            # إنشاء ملف index.html لكل منتج ليكون "موقعاً حقيقياً"
            with open(f"{path}/index.html", "w", encoding="utf-8") as f:
                f.write(f"<html><body><h1>Product Page: {p}</h1><p>Loading full AI content...</p></body></html>")
            print(f"✅ تم إنشاء مجلد المنتج: {path}")

    print("\n🚀 مبروك! الآن أصبح لديك 'موقع حقيقي' بهيكل مجلدات مستقلة.")
    print("الخطوة القادمة: سأعطيك أمر Gemini لملء هذه المجلدات فقط بالبيانات.")

if __name__ == "__main__":
    create_real_site()