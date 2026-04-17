import os
import datetime
import random

# --- 1. CONFIG & REVENUE STACK ---
BATCH_START = int(os.environ.get("BATCH_START", 0))
BATCH_SIZE = 10000 
BASE_URL = "https://fairdiscovery.org"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

# ALL LINKS RESTORED
LINKS = {
    "peerpush": "https://peerpush.net?atp=forgevertical",
    "nord_vpn": "https://go.nordvpn.net/aff_c?offer_id=15&aff_id=145959&url_id=902",
    "nord_pass": "https://go.nordpass.io/aff_c?offer_id=488&aff_id=145959&url_id=9356",
    "honeygain": "https://join.honeygain.com/PRINY5083C",
    "surfshark": "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160",
    "aurora": "https://www.aurora-repair.com",
    "amazon": "fairdiscovery-20" # Associate Tag
}

def generate_header(keyword):
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{keyword} | Industrial Analysis 2026</title>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
    </script>
    <style>
        :root {{ --primary: #00d18a; --nord: #005ae6; --honey: #ffbf00; --dark: #1a2a3a; --forge: #e63946; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: #f4f7f6; margin: 0; line-height: 1.6; color: #333; }}
        .nav {{ background: var(--dark); padding: 15px 20px; display: flex; justify-content: space-between; }}
        .nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 850px; margin: 30px auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ border: 1px solid #eee; padding: 20px; border-radius: 10px; border-top: 4px solid var(--primary); text-decoration:none; color:inherit; display:block; transition: 0.3s; }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .ad-card.forge {{ border-top-color: var(--forge); background: #fffcfc; }}
        .ad-card.nord {{ border-top-color: var(--nord); }}
        .ad-card.honey {{ border-top-color: var(--honey); }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 6px; }}
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
            <a href="{LINKS['peerpush']}">FORGE REPO</a>
        </div>
        <div class="container">
            <h1>Engineering Analysis: {keyword}</h1>
            <p>Verification of <strong>{keyword}</strong> infrastructure. Audit focus: data resilience and 2026 connectivity standards.</p>
            
            <div class="ad-grid">
                <a href="{LINKS['peerpush']}" class="ad-card forge" onclick="trackAff('Peerpush')">
                    <small style="color:var(--forge); font-weight:bold;">FORGE VERTICAL</small>
                    <h4>{keyword} Node Repo</h4>
                    <p>Access the industrial-grade toolset for {keyword} automation.</p>
                </a>

                <a href="{LINKS['nord_vpn']}" class="ad-card nord" onclick="trackAff('NordVPN')">
                    <small style="color:var(--nord); font-weight:bold;">NETWORK SECURITY</small>
                    <h4>NordVPN: {keyword} Tunnels</h4>
                    <p>Secure remote access to hardware endpoints.</p>
                </a>

                <a href="{LINKS['surfshark']}" class="ad-card" onclick="trackAff('Surfshark')" style="border-top-color:#00d1ff;">
                    <small style="color:#00d1ff; font-weight:bold;">DATA PRIVACY</small>
                    <h4>Surfshark Protection</h4>
                    <p>Unlimited device coverage for {keyword} monitoring labs.</p>
                </a>

                <a href="{LINKS['honeygain']}" class="ad-card honey" onclick="trackAff('Honeygain')">
                    <small style="color:var(--honey); font-weight:bold;">PASSIVE INCOME</small>
                    <h4>Bandwidth Monetization</h4>
                    <p>Offset {keyword} operational costs via Honeygain.</p>
                </a>

                <a href="{LINKS['nord_pass']}" class="ad-card" onclick="trackAff('NordPass')">
                    <small style="color:var(--primary); font-weight:bold;">ACCESS CONTROL</small>
                    <h4>NordPass Vault</h4>
                    <p>Encrypted credential storage for system admins.</p>
                </a>

                <a href="https://www.amazon.com/s?k={keyword.replace(' ', '+')}&tag={LINKS['amazon']}" class="ad-card" onclick="trackAff('Amazon')" style="border-top-color:#ff9900;">
                    <small style="color:#ff9900; font-weight:bold;">HARDWARE</small>
                    <h4>Industrial Components</h4>
                    <p>Source verified hardware for {keyword} projects.</p>
                </a>
            </div>

            <div style="background:var(--dark); color:white; padding:30px; border-radius:10px; text-align:center;">
                <h3>Professional Forensic Support</h3>
                <p>Diagnostic handshakes and repair for {keyword} via Aurora Repair.</p>
                <a href="{LINKS['aurora']}" class="btn">Contact Aurora &rarr;</a>
            </div>
        </div>
    </body>
    </html>
    """
    with open(os.path.join(path, filename), "w") as f:
        f.write(html)
