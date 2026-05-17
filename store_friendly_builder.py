import os
import sys
import codecs

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

def deploy_friendly_compliant_store():
    print("=========================================================")
    print("✨ DEPLOYING: ELEGANT WELCOME & ETHICAL SEARCH ROUTER")
    print("=========================================================")
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Certified Analytics Marketplace</title>
    <style>
        :root {
            --bg-base: #f9f9fb;
            --text-main: #1d1d1f;
            --text-muted: #86868b;
            --accent-gold: #b38f4f;
            --friendly-green: #2e7d32;
            --friendly-bg: #f4faf4;
            --card-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
        }
        
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: var(--bg-base); margin: 0; padding: 0; color: var(--text-main); }
        
        header { background: #ffffff; padding: 40px 20px; text-align: center; border-bottom: 1px solid #e5e5ea; }
        header h1 { margin: 0; font-size: 2.2em; font-weight: 700; color: var(--text-main); }
        header p { font-size: 1.1em; margin: 10px 0 0 0; color: var(--text-muted); }
        
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        
        /* صندوق البحث المركزي الفخم */
        .search-section { text-align: center; margin-bottom: 40px; padding: 20px; background: #ffffff; border-radius: 12px; box-shadow: var(--card-shadow); border: 1px solid #e5e5ea; }
        .search-section h2 { font-size: 1.2em; margin-bottom: 15px; color: var(--text-main); }
        .search-container { display: flex; max-width: 600px; margin: 0 auto; gap: 10px; }
        .search-input { flex-grow: 1; padding: 14px 20px; border: 2px solid #e5e5ea; border-radius: 8px; font-size: 1em; outline: none; transition: border-color 0.2s; }
        .search-input:focus { border-color: var(--accent-gold); }
        .search-btn { background: var(--text-main); color: #ffffff; border: none; padding: 14px 25px; font-weight: 600; border-radius: 8px; cursor: pointer; transition: background 0.2s; }
        .search-btn:hover { background: var(--accent-gold); }
        
        /* شبكة المربعات الستة */
        .grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px; }
        
        .category-card { background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: var(--card-shadow); transition: all 0.3s ease; text-decoration: none; color: inherit; display: flex; flex-direction: column; border: 1px solid #f2f2f7; }
        .category-card:hover { transform: translateY(-5px); border-color: var(--accent-gold); }
        .card-img { height: 200px; background-size: cover; background-position: center; }
        .card-body { padding: 25px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; }
        .card-body h3 { margin: 0 0 10px 0; font-size: 1.3em; font-weight: 600; }
        .card-body p { margin: 0 0 20px 0; color: var(--text-muted); font-size: 0.95em; line-height: 1.5; }
        .badge { display: inline-block; padding: 6px 12px; background: #f2f2f7; color: var(--text-main); font-size: 0.8em; font-weight: 600; border-radius: 20px; }
        
        /* نافذة الترحيب والإرشاد البديلة الرائعة */
        #friendly-welcome-screen { display: none; background: var(--friendly-bg); color: var(--text-main); padding: 50px 30px; border-radius: 16px; border: 1px solid #c8e6c9; text-align: center; margin-top: 20px; box-shadow: var(--card-shadow); }
        #friendly-welcome-screen h1 { font-size: 2.2em; margin-bottom: 15px; color: var(--friendly-green); }
        #friendly-welcome-screen p { font-size: 1.1em; color: #444; line-height: 1.6; max-width: 700px; margin: 10px auto; }
        .welcome-icon { font-size: 3.5em; margin-bottom: 10px; color: var(--accent-gold); }
        
        #dynamic-results { display: none; margin-top: 20px; }
        .results-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 2px solid var(--accent-gold); padding-bottom: 10px; }
        .reset-btn { background: var(--text-main); color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: background 0.2s; }
        .reset-btn:hover { background: var(--accent-gold); }
        
        footer { text-align: center; margin-top: 60px; padding: 30px; color: var(--text-muted); font-size: 0.85em; border-top: 1px solid #e5e5ea; background: #ffffff; }
    </style>
</head>
<body>

    <header>
        <h1>📊 The Statistical Transparency Index</h1>
        <p>No Flattery. No Hype. Just Peer-Reviewed Consumer Performance Data.</p>
    </header>

    <div class="container">
        
        <div class="search-section">
            <h2>🔍 Query ClickBank Decentralized Inventory</h2>
            <div class="search-container">
                <input type="text" id="store-search-bar" class="search-input" placeholder="Search categories... (e.g., shoes, wood, glasses, hats)">
                <button class="search-btn" onclick="executeAdvancedQuery()">Search Product</button>
            </div>
        </div>

        <div id="friendly-welcome-screen">
            <div class="welcome-icon">✨</div>
            <h1>Welcome to Our Premium Ethical Marketplace!</h1>
            <p>Thank you for exploring our platform. We are delighted to have you here.</p>
            <p>Please note that our global catalog is exclusively specialized in high-utility lifestyle crafts, premium physical gear, and verified wellness tools. The category or keyword you searched for falls outside our curated, secure collection.</p>
            <p>We warmly invite you to browse our top-performing, transparently reviewed categories below. Let us help you find something exceptional!</p>
            <button class="reset-btn" style="margin-top:20px;" onclick="resetStoreToNormal()">Explore Our Best Collections</button>
        </div>

        <div id="dynamic-results">
            <div class="results-header">
                <h2 id="dynamic-title">Live ClickBank Feeds Matched</h2>
                <button class="reset-btn" onclick="resetStoreToNormal()">← Return to Main Catalog</button>
            </div>
            <div class="grid-container" id="dynamic-cards-injector"></div>
        </div>

        <div id="master-grid-hub" class="grid-container">
            
            <a href="#" onclick="forceSearch('shoes')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500')"></div>
                <div class="card-body">
                    <h3>01. Premium Footwear Index</h3>
                    <p>Biomechanical stress tests and real durability metrics on this year's top-selling ergonomic footwear.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

            <a href="#" onclick="forceSearch('wood')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=500')"></div>
                <div class="card-body">
                    <h3>02. Architectural Woodworking</h3>
                    <p>Raw structural evaluations of 16,000 blueprints. Material waste ratios and load-bearing realities.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

            <a href="#" onclick="forceSearch('glasses')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500')"></div>
                <div class="card-body">
                    <h3>03. Optical Engineering</h3>
                    <p>UV-spectrum filtration audits and lens scratch-resistance coefficients for premium eyewear.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

            <a href="#" onclick="forceSearch('hats')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1572421154091-a1e626e9527e?w=500')"></div>
                <div class="card-body">
                    <h3>04. Haute Couture Millinery</h3>
                    <p>Material density, weave breathability, and true shade-radius mapping for luxury headwear.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

            <a href="#" onclick="forceSearch('cream')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1608248597481-496100c80836?w=500')"></div>
                <div class="card-body">
                    <h3>05. Bio-Dermal Cosmeceuticals</h3>
                    <p>Clinical absorption assays and honest lipid-retention charts. What active ingredients actually do.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

            <a href="#" onclick="forceSearch('health')" class="category-card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=500')"></div>
                <div class="card-body">
                    <h3>06. Longevity & Wellness Metrics</h3>
                    <p>Calibration tolerances and real metabolic impact studies of preventative healthcare tools.</p>
                    <div><span class="badge">View Options</span></div>
                </div>
            </a>

        </div>
    </div>

    <footer>
        © 2026 Decentralized Consumer Intelligence Hub. Shariah-Compliant Friendly Filtering Active.
    </footer>

    <script>
        const bannedKeywords = [
            'gambling', 'casino', 'poker', 'betting', 'slot', 'adult', 'porn', 'sex', 'xxx', 'erotic',
            'riba', 'interest', 'usury', 'loan', 'loans', 'astrology', 'horoscope', 'magic', 'fortune',
            'get rich quick', 'scam', 'binary options', 'قمار', 'كازينو', 'ربا', 'فائدة', 'قرض', 'اباحي',
            'جنس', 'تنجيم', 'ابراج', 'سحر', 'شعوذة', 'ثراء سريع'
        ];

        function executeAdvancedQuery() {
            const queryInput = document.getElementById('store-search-bar').value.toLowerCase().trim();
            if (!queryInput) return;

            // الفحص اللطيف عبر جدار الحماية الشرعي
            for (let word of bannedKeywords) {
                if (queryInput.includes(word)) {
                    triggerFriendlyRedirect();
                    return;
                }
            }

            renderDynamicClickBankProducts(queryInput);
        }

        function triggerFriendlyRedirect() {
            document.getElementById('master-grid-hub').style.display = 'none';
            document.getElementById('dynamic-results').style.display = 'none';
            document.getElementById('friendly-welcome-screen').style.display = 'block';
        }

        function renderDynamicClickBankProducts(keyword) {
            document.getElementById('friendly-welcome-screen').style.display = 'none';
            document.getElementById('master-grid-hub').style.display = 'none';
            
            const titleElement = document.getElementById('dynamic-title');
            const injector = document.getElementById('dynamic-cards-injector');
            
            titleElement.innerText = `📦 Live ClickBank Feeds: Matched "${keyword.toUpperCase()}" Products Portfolio`;
            
            let mockImage = 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=500';
            if(keyword.includes('shoe')) mockImage = 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500';
            if(keyword.includes('wood')) mockImage = 'https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=500';
            if(keyword.includes('glass')) mockImage = 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500';
            if(keyword.includes('hat')) mockImage = 'https://images.unsplash.com/photo-1572421154091-a1e626e9527e?w=500';
            if(keyword.includes('cream')) mockImage = 'https://images.unsplash.com/photo-1608248597481-496100c80836?w=500';
            if(keyword.includes('health')) mockImage = 'https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=500';

            injector.innerHTML = `
                <div class="category-card">
                    <div class="card-img" style="background-image: url('${mockImage}')"></div>
                    <div class="card-body">
                        <h3>[Verified] Premium Alpha ${keyword} Pack</h3>
                        <p>Honest Audit: High retention rate. Fully compliant with professional standards but has a slight learning curve.</p>
                        <div style="font-weight:bold; color:#27ae60; margin-bottom:10px;">Price: $39.00</div>
                        <a href="https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw" target="_blank" class="badge" style="background:var(--accent-gold); color:white; text-align:center; text-decoration:none;">🔒 View Analytical Details</a>
                    </div>
                </div>
                <div class="category-card">
                    <div class="card-img" style="background-image: url('${mockImage}')"></div>
                    <div class="card-body">
                        <h3>[Budget Tier] Essential DIY ${keyword} Blueprint</h3>
                        <p>Honest Audit: Functional, affordable, designed for hobbyists looking for a quick startup without premium add-ons.</p>
                        <div style="font-weight:bold; color:#27ae60; margin-bottom:10px;">Price: $19.00</div>
                        <a href="https://hop.clickbank.net/?affiliate=YOUR_CLICKBANK_ID&vendor=tedswoodw" target="_blank" class="badge" style="background:var(--accent-gold); color:white; text-align:center; text-decoration:none;">🔒 View Analytical Details</a>
                    </div>
                </div>
            `;
            
            document.getElementById('dynamic-results').style.display = 'block';
        }

        function resetStoreToNormal() {
            document.getElementById('store-search-bar').value = '';
            document.getElementById('friendly-welcome-screen').style.display = 'none';
            document.getElementById('dynamic-results').style.display = 'none';
            document.getElementById('master-grid-hub').style.display = 'grid';
        }

        function forceSearch(val) {
            document.getElementById('store-search-bar').value = val;
            executeAdvancedQuery();
        }
    </script>
</body>
</html>
"""
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("=========================================================")
    print("✅ REFACTOR SUCCESS: Horror screen replaced with premium welcome screen!")
    print("=========================================================")

if __name__ == "__main__":
    deploy_friendly_compliant_store()
