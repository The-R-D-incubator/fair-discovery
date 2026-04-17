import os
import datetime
import random

# --- 1. REVENUE & TRACKING STACK ---
CONFIG = {
    "BASE_URL": "https://fairdiscovery.org",
    "AMAZON_TAG": "fairdiscovery-20",
    "SURFSHARK_URL": "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160",
    "HONEYGAIN_URL": "https://join.honeygain.com/PRINY5083C",
    "AURORA_URL": "https://www.aurora-repair.com",
    "ADSENSE_ID": "ca-pub-3215536871572990",
    "GA_ID": "G-C6Z3VMB0ND",
    "LIMIT": 1000  # Hard stop for this domain
}

# --- 2. DYNAMIC CONTENT GENERATORS ---
def get_dynamic_image(keyword):
    """Rotates image sources to ensure 'Rich Media' compliance."""
    sources = [
        f"https://source.unsplash.com/800x450/?{keyword.replace(' ', ',')},industrial",
        f"https://loremflickr.com/800/450/{keyword.replace(' ', ',')},tech",
        f"https://picsum.photos/seed/{keyword.replace(' ', '')}/800/450"
    ]
    return random.choice(sources)

def generate_header(keyword):
    today = datetime.date.today().strftime("%Y-%m-%d")
    meta_desc = f"Technical analysis and 2026 procurement guide for {keyword} systems. Verified industrial ROI and security protocols."
    
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_desc}">
    <meta name="last-modified" content="{today}">
    <title>{keyword} | Technical Analysis 2026</title>
    
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={CONFIG['ADSENSE_ID']}" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={CONFIG['GA_ID']}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{CONFIG['GA_ID']}');
      function trackAffClick(l){{gtag('event','click',{{'event_category':'Affiliate','event_label':l}});}}
    </script>

    <style>
        :root {{ --primary: #00d18a; --dark: #1a2a3a; --light: #f4f7f6; }}
        body {{ font-family: 'Segoe UI', system-ui, sans-serif; margin: 0; background: var(--light); color: #333; line-height: 1.6; }}
        .navbar {{ background: var(--dark); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .navbar a {{ color: white; text-decoration: none; font-weight: 700; font-size: 0.9rem; }}
        .container {{ max-width: 850px; margin: 2rem auto; padding: 2rem; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }}
        .hero {{ width: 100%; height: 350px; border-radius: 10px; overflow: hidden; margin-bottom: 2rem; background: #222; }}
        .hero img {{ width: 100%; height: 100%; object-fit: cover; opacity: 0.8; }}
        h1 {{ color: var(--dark); font-size: 2.2rem; line-height: 1.2; margin-top: 0; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0; }}
        .ad-card {{ border: 1px solid #eee; padding: 1.5rem; border-radius: 10px; border-top: 4px solid var(--primary); transition: 0.3s; cursor: pointer; }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.08); }}
        .cta-box {{ background: var(--primary); color: white; padding: 3rem; border-radius: 15px; text-align: center; margin-top: 3rem; }}
        .btn {{ display: inline-block; background: white; color: var(--primary); padding: 0.8rem 2rem; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 1rem; }}
        footer {{ text-align: center; padding: 3rem; font-size: 0.75rem; color: #aaa; }}
    </style>
    """

def generate_navbar():
    return f"""
    <nav class="navbar">
        <a href="{CONFIG['BASE_URL']}">FAIR DISCOVERY</a>
        <div>
            <a href="{CONFIG['AURORA_URL']}" style="margin-left:1.5rem;">SUPPORT</a>
            <a href="{CONFIG['SURFSHARK_URL']}" style="margin-left:1.5rem;">SECURITY</a>
        </div>
    </nav>
    """

# --- 3. CORE BUILDER ---
def build_page(folder, keyword):
    """Generates a single rich-content HTML page."""
    rel_folder = os.path.join("affiliates", folder)
    os.makedirs(rel_folder, exist_ok=True)
    filename = f"{keyword.lower().replace(' ', '-')}.html"
    
    with open(os.path.join(rel_folder, filename), "w") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>{generate_header(keyword)}</head>
        <body>
            {generate_navbar()}
            <div class="container">
                <div class="hero"><img src="{get_dynamic_image(keyword)}" alt="{keyword} Analysis"></div>
                <h1>The 2026 Engineering Report on {keyword}</h1>
                <p>In the current industrial landscape, <strong>{keyword}</strong> integration requires a multi-layered approach to hardware durability and digital handshake protocols. Our technical board recommends high-redundancy specifications for operations within the UK, EU, and South African markets.</p>
                
                <div class="ad-grid">
                    <div class="ad-card" onclick="trackAffClick('Amazon-{keyword}')">
                        <small style="color:var(--primary); font-weight:bold;">HARDWARE PROCUREMENT</small>
                        <h4>Verified {keyword} Units</h4>
                        <p>Procure ISO-certified hardware for high-demand environments.</p>
                        <a href="#" style="color:var(--primary); font-weight:bold; text-decoration:none;">View Specs &rarr;</a>
                    </div>
                    <div class="ad-card" onclick="location.href='{CONFIG['SURFSHARK_URL']}'; trackAffClick('Surfshark-{keyword}')">
                        <small style="color:var(--primary); font-weight:bold;">DATA INTEGRITY</small>
                        <h4>Secure Diagnostic Tunnels</h4>
                        <p>Protect {keyword} data streams with 256-bit military-grade encryption.</p>
                        <a href="{CONFIG['SURFSHARK_URL']}" style="color:var(--primary); font-weight:bold; text-decoration:none;">Secure Link &rarr;</a>
                    </div>
                </div>

                <div class="cta-box">
                    <h2>Mission Critical Support</h2>
                    <p>Precision calibration and lifecycle maintenance for {keyword} infrastructure.</p>
                    <a href="{CONFIG['CONFIG']['AURORA_URL'] if 'CONFIG' in CONFIG else CONFIG['AURORA_URL']}" class="btn">Visit Aurora-Repair.com</a>
                </div>
                
                <p style="font-size:10px; color:#bbb; text-align:center; margin-top:40px;">
                    Associate Disclosure: As an Amazon Associate, we earn from qualifying purchases. 
                    Ad revenue supports free technical reporting for the global engineering community.
                </p>
            </div>
            <footer>&copy; 2026 Fair Discovery | Global Industrial Intelligence</footer>
        </body>
        </html>
        """)

def update_sitemap():
    """Builds a fresh sitemap.xml in the root for Google/AI crawlers."""
    print("🛰️ Scanning for URLs...")
    today = datetime.date.today().strftime("%Y-%m-%d")
    entries = [f"<url><loc>{CONFIG['BASE_URL']}/</loc><priority>1.0</priority></url>"]
    
    affiliates_path = os.path.join(os.getcwd(), "affiliates")
    for root, _, files in os.walk(affiliates_path):
        for file in files:
            if file.endswith(".html"):
                path = os.path.relpath(os.path.join(root, file), os.getcwd()).replace(os.sep, '/')
                entries.append(f"<url><loc>{CONFIG['BASE_URL']}/{path}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")

    sitemap_xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(entries)}</urlset>'
    with open("sitemap.xml", "w") as f:
        f.write(sitemap_xml)
    print(f"✅ Sitemap complete. {len(entries)} URLs mapped.")

# --- 4. THE EXECUTION ---
if __name__ == "__main__":
    # Add your massive list of portals here
    # portals = [("auto-tech", "Automotive", ["OBD2 Scanner", "ECU Tuner"])...]
    
    # Simple example to verify logic
    test_portals = [("pro-solar", "Solar Infrastructure", ["Solar Inverter", "Lithium Battery"])]
    
    count = 0
    for folder, title, keywords in test_portals:
        for k in keywords:
            if count < CONFIG["LIMIT"]:
                build_page(folder, k)
                count += 1
            else:
                break
    
    update_sitemap()
    print(f"🏁 MISSION COMPLETE: {count} pages generated.")
