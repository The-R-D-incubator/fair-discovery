import os
import datetime
import random

# --- REVENUE STACK ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
NORD_URL = "YOUR_NORD_LINK_HERE" # Add your new Nord link
AURORA_URL = "https://www.aurora-repair.com"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

def generate_header(title, keyword):
    """Generates SEO/GEO header with unique meta and tracking."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    # GEO-targeted meta description for AI and Google
    meta_desc = f"Technical analysis and 2026 procurement guide for {keyword} systems. Industrial ROI, lifecycle maintenance, and security protocols verified."
    
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <meta name="last-modified" content="{today}">
    <title>{title} | Technical Report 2026</title>
    
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
        body {{ font-family: 'Segoe UI', Roboto, sans-serif; margin: 0; background: var(--light); color: #333; line-height: 1.6; }}
        .navbar {{ background: var(--dark); padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: white; position: sticky; top: 0; z-index: 1000; }}
        .navbar a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 900px; margin: 20px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .hero-img {{ width: 100%; height: 350px; background: #222; border-radius: 8px; margin-bottom: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
        .hero-img img {{ width: 100%; height: 100%; object-fit: cover; opacity: 0.7; }}
        .update-tag {{ font-size: 12px; color: #888; text-transform: uppercase; letter-spacing: 1px; }}
        h1 {{ color: var(--dark); font-size: 2.2rem; line-height: 1.2; margin-top: 5px; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ background: #fff; border: 1px solid #eee; padding: 20px; border-radius: 12px; transition: 0.3s; border-top: 4px solid var(--primary); }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .cta-box {{ background: var(--primary); color: white; padding: 40px; border-radius: 15px; text-align: center; margin-top: 40px; }}
        .btn-main {{ display: inline-block; background: white; color: var(--primary); padding: 15px 35px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 20px; }}
        @media (max-width: 600px) {{ .ad-grid {{ grid-template-columns: 1fr; }} }}
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
    
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        today_date = datetime.date.today().strftime("%B %d, %Y")
        # Dynamic image logic - pulls a professional tech image based on keyword
        image_url = f"https://source.unsplash.com/800x400/?{k.replace(' ', ',')},industrial"
        
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                {generate_header(f"{k} Guide 2026", k)}
            </head>
            <body>
                {generate_navbar()}
                <div class="container">
                    <span class="update-tag">Verified Industry Report: {today_date}</span>
                    <div class="hero-img"><img src="{image_url}" alt="{k} Industrial Analysis"></div>
                    <h1>The 2026 Professional Guide to {k} Systems</h1>
                    <p>As industrial standards converge in 2026, the <strong>{k}</strong> ecosystem has evolved to prioritize decentralized data integrity and energy-efficient hardware handshakes. Our technical board has reviewed the latest {k} specifications to ensure high-uptime performance in the South African and EU sectors.</p>
                    
                    <div class="ad-grid">
                        <div class="ad-card" onclick="trackAffiliateClick('Amazon-{k}')">
                            <span style="color:var(--primary); font-size: 11px; font-weight:bold;">HARDWARE</span>
                            <h4>Procure Verified {k}</h4>
                            <p>Direct access to ISO-certified hardware components for precision operations.</p>
                            <a href="#" style="color:var(--primary); font-weight:bold; text-decoration:none;">Check Specs &rarr;</a>
                        </div>
                        <div class="ad-card" onclick="trackAffiliateClick('Security-{k}')">
                            <span style="color:var(--primary); font-size: 11px; font-weight:bold;">ENCRYPTION</span>
                            <h4>Network Integrity</h4>
                            <p>Secure your {k} diagnostic tunnels with 256-bit AES protection.</p>
                            <a href="{SURFSHARK_URL}" style="color:var(--primary); font-weight:bold; text-decoration:none;">Secure Link &rarr;</a>
                        </div>
                    </div>

                    <div class="cta-box">
                        <h3>Advanced {k} Lifecycle Support</h3>
                        <p>For custom calibration, remote diagnostics, and hardware repair of industrial {k} systems.</p>
                        <a href="{AURORA_URL}" class="btn-main">Contact Aurora Repair</a>
                    </div>
                </div>
                <footer style="text-align:center; padding:40px; font-size:12px; color:#999;">
                    &copy; 2026 Fair Discovery | Global Industrial Metrics
                </footer>
            </body>
            </html>
            """)

# [Your massive 'all_portals' list goes here]
