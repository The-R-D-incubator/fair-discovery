import os
import datetime
import random

# --- 1. CONFIG & BATCHING ---
BATCH_START = int(os.environ.get("BATCH_START", 0))
BATCH_SIZE = 1000 
BASE_URL = "https://fairdiscovery.org"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

# --- 2. THE REVENUE STACK ---
LINKS = {
    "peerpush": "https://peerpush.net?atp=forgevertical", # YOUR NEW REPOSITORY LINK
    "nord_vpn": "https://go.nordvpn.net/aff_c?offer_id=15&aff_id=145959&url_id=902",
    "nord_pass": "https://go.nordpass.io/aff_c?offer_id=488&aff_id=145959&url_id=9356",
    "honeygain": "https://join.honeygain.com/PRINY5083C",
    "surfshark": "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160",
    "aurora": "https://www.aurora-repair.com",
    "amazon": "fairdiscovery-20"
}

def get_image(k):
    sources = [
        f"https://source.unsplash.com/800x450/?{k.replace(' ', ',')},industrial",
        f"https://loremflickr.com/800/450/{k.replace(' ', ',')},tech",
        f"https://picsum.photos/seed/{k.replace(' ', '')}/800/450"
    ]
    return random.choice(sources)

def generate_header(keyword):
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="2026 Technical analysis of {keyword} systems. Industrial ROI and security protocols verified.">
    <title>{keyword} | Technical Analysis 2026</title>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
      function trackAff(l){{gtag('event','click',{{'event_category':'Affiliate','event_label':l}});}}
    </script>
    <style>
        :root {{ --primary: #00d18a; --nord: #005ae6; --honey: #ffbf00; --dark: #1a2a3a; --forge: #e63946; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: #f4f7f6; margin: 0; line-height: 1.6; color: #333; }}
        .nav {{ background: var(--dark); padding: 15px 20px; color: white; display: flex; justify-content: space-between; }}
        .nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 850px; margin: 30px auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
        .hero-img {{ width: 100%; height: 350px; object-fit: cover; border-radius: 8px; margin-bottom: 25px; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ border: 1px solid #eee; padding: 20px; border-radius: 10px; border-top: 4px solid var(--primary); transition: 0.3s; cursor: pointer; text-decoration:none; color:inherit; display:block; }}
        .ad-card.forge {{ border-top: 4px solid var(--forge); background: #fffcfc; }}
        .ad-card.nord {{ border-top: 4px solid var(--nord); }}
        .ad-card.honey {{ border-top: 4px solid var(--honey); }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 6px; margin-top: 10px; }}
    </style>
    """

def build_page(folder, keyword):
    path = os.path.join("affiliates", folder)
    os.makedirs(path, exist_ok=True)
    filename = f"{keyword.lower().replace(' ', '-')}.html"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>{generate_header(keyword)}</head>
    <body>
        <div class="nav">
            <a href="{BASE_URL}">FAIR DISCOVERY</a>
            <a href="{LINKS['peerpush']}">REPOSITORIES</a>
            <a href="{LINKS['aurora']}">SUPPORT</a>
        </div>
        <div class="container">
            <img src="{get_image(keyword)}" class="hero-img">
            <h1>2026 Engineering Guide: {keyword}</h1>
            <p>Verified technical analysis of <strong>{keyword}</strong> infrastructure deployment. Audit focus: hardware resilience, diagnostic handshakes, and 2026 network security standards.</p>
            
            <div class="ad-grid">
                <a href="{LINKS['peerpush']}" class="ad-card forge" onclick="trackAff('Peerpush')">
                    <small style="color:var(--forge); font-weight:bold;">PRECISION TOOLS</small>
                    <h4>{keyword} Node Repo</h4>
                    <p>Access specialized industrial nodes for {keyword} forensics and automation.</p>
                </a>
                
                <a href="{LINKS['nord_vpn']}" class="ad-card nord" onclick="trackAff('NordVPN')">
                    <small style="color:var(--nord); font-weight:bold;">ENCRYPTION</small>
                    <h4>Secure {keyword} Stream</h4>
                    <p>Protect your industrial data with NordVPN tunnels.</p>
                </a>
                
                <a href="{LINKS['honeygain']}" class="ad-card honey" onclick="trackAff('Honeygain')">
                    <small style="color:var(--honey); font-weight:bold;">PASSIVE REVENUE</small>
                    <h4>Monetize Idle Bandwidth</h4>
                    <p>Turn your {keyword} network into passive income.</p>
                </a>
            </div>

            <div style="background:var(--dark); color:white; padding:30px; border-radius:10px; text-align:center;">
                <h3>Professional Calibration Support</h3>
                <p>Onsite and remote diagnostics for {keyword} via Aurora Repair.</p>
                <a href="{LINKS['aurora']}" class="btn">Contact Aurora &rarr;</a>
            </div>
            
            <p style="font-size:10px; color:#aaa; margin-top:40px; text-align:center;">
                Associate Disclosure: Peerpush access provided via Forge Vertical. 
                Reports are funded by Nord Security and Honeygain passive income partnerships.
            </p>
        </div>
    </body>
    </html>
    """
    with open(os.path.join(path, filename), "w") as f:
        f.write(html)

# ... (rest of the sitemap and main logic remain the same)
