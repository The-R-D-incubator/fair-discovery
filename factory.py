import os
import datetime
import random

# --- CONFIGURATION ---
BASE_URL = "https://fairdiscovery.org"
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
AURORA_URL = "https://www.aurora-repair.com"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

def generate_header(title, keyword):
    """Generates SEO header with unique Meta and Tracking."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    meta_desc = f"Technical analysis and 2026 procurement guide for {keyword} systems. Industrial ROI, security protocols, and maintenance verified."
    
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
    </script>
    <style>
        :root {{ --primary: #00d18a; --dark: #1a2a3a; --light: #f4f7f6; }}
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: var(--light); line-height: 1.6; color: #333; }}
        .navbar {{ background: var(--dark); padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: white; position: sticky; top: 0; z-index: 1000; }}
        .navbar a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 900px; margin: 20px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .hero-img {{ width: 100%; height: 300px; background: #222; border-radius: 8px; margin-bottom: 20px; overflow: hidden; }}
        .hero-img img {{ width: 100%; height: 100%; object-fit: cover; opacity: 0.7; }}
        h1 {{ color: var(--dark); font-size: 2.2rem; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ border: 1px solid #eee; padding: 20px; border-radius: 12px; border-top: 4px solid var(--primary); }}
        .cta-box {{ background: var(--primary); color: white; padding: 40px; border-radius: 15px; text-align: center; }}
        .btn-main {{ display: inline-block; background: white; color: var(--primary); padding: 12px 25px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 15px; }}
    </style>
    """

def generate_navbar():
    return f"""
    <nav class="navbar">
        <a href="{BASE_URL}">FAIR DISCOVERY</a>
        <div><a href="{AURORA_URL}">Support</a> <a href="{SURFSHARK_URL}" style="margin-left:20px;">Security</a></div>
    </nav>"""

def build_elite_portal(folder, title, keywords):
    """Builds the actual HTML pages."""
    base_path = os.path.join(os.getcwd(), "affiliates", folder)
    os.makedirs(base_path, exist_ok=True)
    
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        img_url = f"https://source.unsplash.com/800x400/?{k.replace(' ', ',')},tech"
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>{generate_header(k, k)}</head>
            <body>
                {generate_navbar()}
                <div class="container">
                    <div class="hero-img"><img src="{img_url}" alt="{k}"></div>
                    <h1>Engineering Guide: {k} (2026)</h1>
                    <p>Verified technical analysis for {k} infrastructure integration.</p>
                    <div class="ad-grid">
                        <div class="ad-card"><h4>Hardware</h4><p>Verified {k} equipment.</p><a href="#">View Specs</a></div>
                        <div class="ad-card"><h4>Security</h4><p>Encrypted data tunnels.</p><a href="{SURFSHARK_URL}">Secure Now</a></div>
                    </div>
                    <div class="cta-box"><h3>Support</h3><p>Calibration for {k} systems.</p><a href="{AURORA_URL}" class="btn-main">Contact Aurora</a></div>
                </div>
            </body></html>""")

def generate_sitemap():
    """Builds a fresh sitemap.xml in the root directory."""
    print("🛰️ Generating Sitemap...")
    urls = [f"<url><loc>{BASE_URL}/</loc><priority>1.0</priority></url>"]
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    affiliates_dir = os.path.join(os.getcwd(), "affiliates")
    for root, _, files in os.walk(affiliates_dir):
        for file in files:
            if file.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(root, file), os.getcwd()).replace(os.sep, '/')
                urls.append(f"<url><loc>{BASE_URL}/{rel_path}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")

    sitemap_xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(urls)}</urlset>'
    with open("sitemap.xml", "w") as f:
        f.write(sitemap_xml)
    print(f"✅ Sitemap complete: {len(urls)} links mapped.")

if __name__ == "__main__":
    # Example portal - Add your full list here
    portals = [("auto-tech", "Automotive", ["OBD2 Scanner", "ECU Tuner"])] 
    for f, t, k in portals:
        build_elite_portal(f, t, k)
    generate_sitemap()
