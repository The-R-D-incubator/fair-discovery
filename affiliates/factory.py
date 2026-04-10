import os

# --- REVENUE & COMPLIANCE KEYS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"

def build_pro_portal(folder_name, title, keywords):
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # CSS for Professionalism & Responsiveness
    pro_css = """
    :root { --primary: #00d18a; --secondary: #0055ff; --dark: #1a1a1a; --light: #f9f9f9; }
    body { font-family: 'Inter', system-ui, sans-serif; margin: 0; color: var(--dark); line-height: 1.6; background: #fff; }
    .container { max-width: 1100px; margin: auto; padding: 20px; }
    header { background: var(--dark); color: white; padding: 60px 20px; text-align: center; }
    .card { background: var(--light); border-radius: 12px; padding: 30px; margin: 20px 0; border: 1px solid #eee; }
    .btn { display: inline-block; padding: 12px 25px; border-radius: 6px; text-decoration: none; font-weight: bold; transition: 0.3s; }
    .btn-main { background: var(--primary); color: white; }
    .btn-surf { background: var(--secondary); color: white; }
    .cookie-banner { position: fixed; bottom: 0; width: 100%; background: #222; color: white; padding: 15px; display: none; z-index: 1000; text-align: center; font-size: 13px; }
    @media (max-width: 768px) { header { padding: 30px 15px; } h1 { font-size: 24px; } }
    """

    # Cookie Consent Script (GDPR/POPIA)
    cookie_js = """
    function acceptCookies() {
        localStorage.setItem('cookiesAccepted', 'true');
        document.getElementById('cookie-banner').style.display = 'none';
    }
    window.onload = function() {
        if(!localStorage.getItem('cookiesAccepted')) {
            document.getElementById('cookie-banner').style.display = 'block';
        }
    }
    """

    # 1. GENERATE INDEX PAGE
    with open(f"{base_path}/index.html", "w") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Global Tech Resource</title>
            <style>{pro_css}</style>
        </head>
        <body>
            <header>
                <h1>{title}</h1>
                <p>Global Solutions for UK, EU, USA, Canada, and South Africa</p>
            </header>
            <div class="container">
                <h2>Industry Analysis & Hardware Procurement</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    {"".join([f'<div class="card"><h3>{k}</h3><a href="{k.lower().replace(" ", "-")}.html" class="btn btn-main">Read Analysis</a></div>' for k in keywords])}
                </div>
            </div>
            <div id="cookie-banner" class="cookie-banner">
                This site uses cookies to optimize your experience in compliance with GDPR and POPIA. 
                <button onclick="acceptCookies()" style="margin-left:15px; padding:5px 15px; cursor:pointer;">Accept</button>
            </div>
            <script>{cookie_js}</script>
        </body>
        </html>
        """)

    # 2. GENERATE ARTICLE PAGES (Detailed & Semantic)
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        with open(f"{base_path}/{filename}", "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Best {k} 2026 | Technical Review</title>
                <style>{pro_css}</style>
            </head>
            <body>
                <nav style="padding:20px; border-bottom:1px solid #eee;"><a href="index.html" style="color:var(--primary); text-decoration:none; font-weight:bold;">&larr; {title} Home</a></nav>
                <div class="container">
                    <small style="text-transform:uppercase; color:#888;">Hardware Lab Report • April 2026</small>
                    <h1>The Global Standard for {k}</h1>
                    <p>Whether you are operating a B2B enterprise in London or a home workshop in Cape Town, selecting the right {k} is critical for operational uptime.</p>
                    
                    <div class="card" style="border-left: 5px solid var(--secondary);">
                        <h3>🛡️ Enterprise Security Notice</h3>
                        <p>We recommend all {k} data be routed through a secure tunnel. 
                        <strong>Surfshark VPN</strong> is our top choice for EU and SA compliance.</p>
                        <a href="{SURFSHARK_URL}" class="btn btn-surf">Get Secure Discount →</a>
                    </div>

                    <div id="amzn-assoc-ad-fd-network"></div>
                    <script type="text/javascript">
                        amzn_assoc_tracking_id = "{AMAZON_TAG}";
                        amzn_assoc_ad_mode = "search";
                        amzn_assoc_ad_type = "smart";
                        amzn_assoc_marketplace = "amazon";
                        amzn_assoc_region = "US";
                        amzn_assoc_title = "Procure Verified {k} Hardware";
                        amzn_assoc_default_search_phrase = "{k}"; 
                        amzn_assoc_linkid = "fd_pro_search";
                    </script>
                    <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>

                    <div class="card" style="background: #fffbe6; border-color: #ffe58f;">
                        <h3>💰 Resource Optimization</h3>
                        <p>Join the "Mercenary" program: Get a $5 bonus to help cover your data costs.</p>
                        <a href="{HONEYGAIN_URL}" style="color:#d48806; font-weight:bold;">Claim $5 Honeygain Bonus →</a>
                    </div>
                </div>
                <footer style="background:#f4f4f4; padding:40px; text-align:center; font-size:12px;">
                    &copy; 2026 Fair Discovery Network. GDPR & POPIA Compliant. 
                    Targeting UK, EU, USA, CAN, & SA.
                </footer>
            </body>
            </html>
            """)

if __name__ == "__main__":
    # The Full 100-Site Sprint (Batch 1: High Tech & Energy)
    build_pro_portal("solar-enterprise", "B2B Energy Solutions", ["Hybrid Inverter 5kW", "LiFePO4 Battery Stack", "Commercial Solar Panels"])
    build_pro_portal("auto-diagnostics", "Vehicle Fleet Tools", ["OBD2 Professional Scanner", "Heavy Duty ECU Tuner", "Fleet GPS Tracker"])
    build_pro_portal("remote-comms", "Satellite & Global WiFi", ["Starlink High Performance Kit", "Starlink Pipe Mount", "Mesh WiFi 6E System"])
    # Add your next 97 sites here...
    print("🚀 100-Portal 'Professional' Engine Online.")
