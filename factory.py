import os
import datetime
import random

# --- CONFIG ---
BATCH_START = int(os.environ.get("BATCH_START", 0))
BATCH_SIZE = 200 # Adjust this if you want bigger strikes
BASE_URL = "https://fairdiscovery.org"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

# --- REVENUE STACK ---
LINKS = {
    "surfshark": "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160",
    "aurora": "https://www.aurora-repair.com",
    "amazon": "fairdiscovery-20"
}

def get_image(k):
    """Rotates through sources for high-quality variety."""
    sources = [
        f"https://source.unsplash.com/800x450/?{k.replace(' ', ',')},industrial",
        f"https://loremflickr.com/800/450/{k.replace(' ', ',')},tech"
    ]
    return random.choice(sources)

def build_page(folder, keyword):
    path = os.path.join("affiliates", folder)
    os.makedirs(path, exist_ok=True)
    filename = f"{keyword.lower().replace(' ', '-')}.html"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{keyword} | Technical Analysis 2026</title>
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
        <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GA_ID}');
        </script>
        <style>
            :root {{ --primary: #00d18a; --dark: #1a2a3a; }}
            body {{ font-family: sans-serif; background: #f4f7f6; margin: 0; line-height: 1.6; }}
            .nav {{ background: var(--dark); padding: 20px; color: white; text-align: center; font-weight: bold; }}
            .container {{ max-width: 800px; margin: 30px auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
            .hero-img {{ width: 100%; height: 350px; object-fit: cover; border-radius: 8px; }}
            .cta {{ background: var(--primary); color: white; padding: 30px; border-radius: 12px; text-align: center; margin-top: 30px; }}
            .btn {{ display: inline-block; background: white; color: var(--primary); padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 6px; }}
        </style>
    </head>
    <body>
        <div class="nav">FAIR DISCOVERY</div>
        <div class="container">
            <img src="{get_image(keyword)}" class="hero-img">
            <h1>2026 Engineering Guide: {keyword}</h1>
            <p>Verified technical analysis of {keyword} infrastructure and hardware integration standards.</p>
            <div class="cta">
                <h3>Industrial Security & Support</h3>
                <p>Ensure your {keyword} diagnostics are secured with 256-bit encryption.</p>
                <a href="{LINKS['surfshark']}" class="btn">Get Protected &rarr;</a>
            </div>
            <p style="font-size:10px; color:#aaa; margin-top:40px; text-align:center;">
                As an Amazon Associate, we earn from qualifying purchases. Support provided by Aurora Repair.
            </p>
        </div>
    </body>
    </html>
    """
    with open(os.path.join(path, filename), "w") as f:
        f.write(html)

def update_sitemap():
    """Builds the sitemap automatically after pages are created."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    entries = [f"<url><loc>{BASE_URL}/</loc><priority>1.0</priority></url>"]
    
    for root, _, files in os.walk("affiliates"):
        for file in files:
            if file.endswith(".html"):
                p = os.path.relpath(os.path.join(root, file), os.getcwd()).replace(os.sep, '/')
                entries.append(f"<url><loc>{BASE_URL}/{p}</loc><lastmod>{today}</lastmod></url>")
                
    with open("sitemap.xml", "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(entries)}</urlset>')

if __name__ == "__main__":
    # Add your massive keyword list here
    all_portals = [
        ("auto-tech", ["OBD2 Scanner", "ECU Tuner"]),
        ("solar-ops", ["Solar Inverter", "Lithium Battery"]),
        # Add 1000 more here...
    ]
    
    # Flatten list for batching
    flat_list = []
    for folder, k_list in all_portals:
        for k in k_list:
            flat_list.append((folder, k))

    batch = flat_list[BATCH_START : BATCH_START + BATCH_SIZE]
    for f, k in batch:
        build_page(f, k)
    
    update_sitemap()
