import os

html_clean_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Ultimate Woodworking Mega Store</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f5f2eb; margin: 0; padding: 0; color: #333; }
        header { background-color: #5c3a21; color: white; padding: 30px 20px; text-align: center; border-bottom: 5px solid #8B5A2B; }
        header h1 { margin: 0; font-size: 2.8em; }
        header p { margin: 5px 0 0 0; font-size: 1.2em; color: #ddd; }
        .store-container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; margin-top: 20px; }
        .product-card { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 6px solid #8B5A2B; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s; }
        .product-card:hover { transform: translateY(-5px); }
        .product-card h2 { color: #5c3a21; font-size: 1.5em; margin-top: 0; }
        .product-card p { color: #666; font-size: 1.05em; line-height: 1.5; }
        .buy-btn { display: block; text-align: center; background-color: #ff9900; color: white; padding: 12px; font-size: 1.2em; text-decoration: none; border-radius: 6px; font-weight: bold; margin-top: 15px; box-shadow: 0 3px 8px rgba(255,153,0,0.3); }
        .buy-btn:hover { background-color: #e68a00; }
        footer { text-align: center; margin: 40px 0 20px 0; color: #999; font-size: 0.9em; border-top: 1px solid #ddd; padding-top: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>🛠️ Premium Woodworking Blueprints Directory</h1>
        <p>Your one-stop digital shop for professional, easy-to-follow woodwork plans</p>
    </header>
    <div class="store-container">
        <div class="products-grid">
            <div class="product-card">
                <h2>Ultimate 16,000 Shed & Cabin Plans</h2>
                <p>Complete blueprints for outdoor sheds, cabins, and home extensions.</p>
                <a href="https://hop.clickbank.net/?affiliate=hamm&vendor=tedswoodw" target="_blank" class="buy-btn">👉 Get Access & Blueprints</a>
            </div>
            <div class="product-card">
                <h2>Premium Home Furniture Blueprints</h2>
                <p>Step-by-step guides for building custom tables, chairs, beds, and indoor crafts.</p>
                <a href="https://hop.clickbank.net/?affiliate=hamm&vendor=tedswoodw" target="_blank" class="buy-btn">👉 Get Access & Blueprints</a>
            </div>
            <div class="product-card">
                <h2>Intricate Wood Toys & Garden Crafts</h2>
                <p>Fun and easy projects for wooden toys, green houses, and artistic garden decorations.</p>
                <a href="https://hop.clickbank.net/?affiliate=hamm&vendor=tedswoodw" target="_blank" class="buy-btn">👉 Get Access & Blueprints</a>
            </div>
        </div>
        <footer>© 2026 Woodworking Franchise Affiliate Store. All Rights Reserved.</footer>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_clean_content)

print("🎯 [SUCCESS] Store encoding fixed with crystal-clear Emojis!")
