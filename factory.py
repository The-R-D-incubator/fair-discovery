import os

# --- REVENUE STACK ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"
ADSENSE_ID = "ca-pub-3215536871572990"  # Your AdSense ID integrated
GA_ID = "G-C6Z3VMB0ND"

def generate_header(title, is_hub=False):
    """Generates the SEO/GEO header with AdSense and Analytics."""
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Technical Analysis 2026</title>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
      function trackAffiliateClick(label) {{
        gtag('event', 'click', {{ 'event_category': 'Affiliate', 'event_label': label }});
      }}
    </script>
    <style>
        :root {{ --primary: #00d18a; --dark: #1a2a3a; --light: #f4f7f6; }}
        body {{ font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; margin: 0; background: var(--light); color: #333; line-height: 1.6; }}
        .navbar {{ background: var(--dark); padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: white; position: sticky; top: 0; z-index: 1000; }}
        .navbar a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 900px; margin: 20px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .hero-img {{ width: 100%; height: 300px; background: #ddd; border-radius: 8px; margin-bottom: 20px; object-fit: cover; display: flex; align-items: center; justify-content: center; color: #666; font-style: italic; }}
        h1 {{ color: var(--dark); font-size: 2.2rem; line-height: 1.2; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ background: #fff; border: 1px solid #eee; padding: 20px; border-radius: 12px; transition: 0.3s; }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .cta-box {{ background: var(--primary); color: white; padding: 40px; border-radius: 15px; text-align: center; margin-top: 40px; }}
        .btn-main {{ display: inline-block; background: white; color: var(--primary); padding: 15px 35px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
        @media (max-width: 600px) {{ body {{ padding: 10px; }} .ad-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    """

def generate_navbar():
    return f"""
    <nav class="navbar">
        <a href="https://fairdiscovery.org">FAIR DISCOVERY</a>
        <div>
            <a href="{AURORA_URL}" style="margin-left:20px;">Support</a>
            <a href="{SURFSHARK_URL}" style="margin-left:20px;">Security</a>
        </div>
    </nav>
    """

def build_elite_portal(folder_name, title, keywords):
    root_affiliates = os.path.join(os.getcwd(), "affiliates")
    base_path = os.path.join(root_affiliates, folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # ARTICLE PAGES
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        catchy_title = f"The 2026 Guide to Professional {k} Systems"
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                {generate_header(k)}
            </head>
            <body>
                {generate_navbar()}
                <div class="container">
                    <div class="hero-img">Visual Analysis: Industrial {k} Integration 2026</div>
                    <h1>{catchy_title}</h1>
                    <p>In the rapidly evolving landscape of 2026, <strong>{k}</strong> hardware has become a cornerstone of industrial efficiency. Our technical audit suggests that current market leaders are prioritizing energy-efficient handshakes and IoT-ready diagnostics to meet the rigorous demands of the South African and EU markets.</p>
                    
                    <div class="ad-grid">
                        <div class="ad-card" onclick="trackAffiliateClick('Amazon-{k}')">
                            <span style="color:var(--primary); font-weight:bold;">COMPONENTS</span>
                            <h4>Verified {k} Hardware</h4>
                            <p>Global shipping and ISO-certified reliability for professional ops.</p>
                            <a href="#" style="color:var(--primary); text-decoration:none;">View Pricing &rarr;</a>
                        </div>
                        <div class="ad-card">
                            <span style="color:var(--primary); font-weight:bold;">SECURITY</span>
                            <h4>Encryption Protocols</h4>
                            <p>Secure your {k} data stream with 256-bit military-grade tunnels.</p>
                            <a href="{SURFSHARK_URL}" style="color:var(--primary); text-decoration:none;">Get Secured &rarr;</a>
                        </div>
                    </div>

                    <div class="cta-box">
                        <h2>Need Precision {k} Setup?</h2>
                        <p>Aurora Repair provides specialized onsite calibration and lifecycle maintenance for all industrial {k} systems.</p>
                        <a href="{AURORA_URL}" class="btn-main">Contact Aurora Repair</a>
                    </div>
                </div>
                <footer style="text-align:center; padding:40px; font-size:12px; color:#999;">
                    &copy; 2026 Fair Discovery | Global Technical Reports
                </footer>
            </body>
            </html>
            """)

# [Rest of your all_portals list and __main__ call here]
