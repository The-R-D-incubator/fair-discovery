import os

# --- REVENUE & GLOBAL ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def build_ultimate_portal(folder_name, title, keywords):
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # 1. GENERATE HUB PAGE (index.html)
    with open(f"{base_path}/index.html", "w") as f:
        links = "".join([f'<li><a href="{k.lower().replace(" ", "-")}.html">{k}</a></li>' for k in keywords])
        f.write(f"""
        <html>
        <head>
            <title>{title} | Fair Discovery Global</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ font-family: sans-serif; padding: 5%; line-height: 1.6; background: #f4f4f4; }}
                .container {{ max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
                h1 {{ color: #00d18a; }}
                a {{ color: #0055ff; text-decoration: none; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{title}</h1>
                <p>Strategic Procurement & Technical Guides for 2026.</p>
                <hr>
                <ul>{links}</ul>
                <p><small>Partnered with <a href="{AURORA_URL}">Aurora Repair</a></small></p>
            </div>
        </body>
        </html>
        """)

    # 2. GENERATE ARTICLE PAGES (SEO Optimized)
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        # Dynamic professional image query (Placeholder for bots to crawl)
        img_url = f"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80"
        
        with open(f"{base_path}/{filename}", "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Top Rated {k} for 2026 | Global Guide</title>
                
                <script type="application/ld+json">
                {{
                  "@context": "https://schema.org/",
                  "@type": "Product",
                  "name": "{k}",
                  "description": "Professional review and procurement guide for {k} hardware.",
                  "brand": {{ "@type": "Brand", "name": "Fair Discovery" }}
                }}
                </script>

                <style>
                    body {{ font-family: -apple-system, sans-serif; margin: 0; color: #333; line-height: 1.8; }}
                    .nav {{ background: #fff; border-bottom: 1px solid #eee; padding: 15px; text-align: center; }}
                    .container {{ max-width: 800px; margin: auto; padding: 20px; }}
                    .hero-img {{ width: 100%; height: auto; border-radius: 10px; }}
                    .cta-box {{ background: #121212; color: white; padding: 25px; border-radius: 12px; margin: 30px 0; }}
                    .aurora-box {{ border: 2px solid #00d18a; padding: 20px; border-radius: 10px; margin: 20px 0; text-align: center; }}
                    .btn {{ padding: 10px 20px; background: #00d18a; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; }}
                </style>
            </head>
            <body>
                <div class="nav"><strong>FAIR DISCOVERY</strong> | <a href="{AURORA_URL}">Aurora Repair</a></div>
                <div class="container">
                    <h1>The Global Standard for {k} (2026)</h1>
                    <img src="{img_url}" class="hero-img">
                    
                    <p>Our lab provides technical data for users across the <strong>USA, UK, Canada, EU, and South Africa</strong>. When selecting {k}, we focus on durability and technical excellence.</p>

                    <script type="text/javascript">
                        amzn_assoc_tracking_id = "{AMAZON_TAG}";
                        amzn_assoc_ad_mode = "search";
                        amzn_assoc_ad_type = "smart";
                        amzn_assoc_marketplace = "amazon";
                        amzn_assoc_region = "US";
                        amzn_assoc_title = "Procure Verified {k}";
                        amzn_assoc_default_search_phrase = "{k}";
                    </script>
                    <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>

                    <div class="aurora-box">
                        <h3>Need Repair or Setup?</h3>
                        <p>For high-end restoration and tech support, visit Aurora Repair.</p>
                        <a href="{AURORA_URL}" class="btn">Visit Aurora-Repair.com</a>
                    </div>

                    <div class="cta-box">
                        <h3>Mercenary Cash: Get $5 Bonus</h3>
                        <p>Claim your Honeygain bonus and start earning passive income.</p>
                        <a href="{HONEYGAIN_URL}" style="color:#00d18a;">Join Honeygain Now →</a>
                    </div>

                    <div style="background:#f0f7ff; padding:20px; border-radius:10px;">
                        <a href="{SURFSHARK_URL}">Secure your hardware with Surfshark VPN →</a>
                    </div>
                </div>
            </body>
            </html>
            """)

if __name__ == "__main__":
    # --- THE 100 SITE LIST (BATCHED BY NICHE) ---
    
    # ENERGY & SOLAR
    build_ultimate_portal("pro-solar", "Energy Systems", ["Solar Inverter", "Lithium Battery", "Charge Controller", "Solar Panels"])
    build_ultimate_portal("backup-power", "Load Shedding Solutions", ["Portable Power Station", "Pure Sine Inverter", "UPS for WiFi"])

    # AUTOMOTIVE & TOOLS
    build_ultimate_portal("auto-tech", "Vehicle Diagnostics", ["OBD2 Scanner", "ECU Tuner", "Car Battery Tester", "Tire Pressure Monitor"])
    build_ultimate_portal("fleet-pro", "Fleet Management", ["GPS Tracker", "Dash Cam 4K", "Fleet Management Software"])

    # CONNECTIVITY & STARLINK
    build_ultimate_portal("star-gear", "Starlink Accessories", ["Starlink Ethernet Adapter", "Starlink Mount", "Travel Case", "Mesh WiFi"])
    build_ultimate_portal("remote-office", "Work From Anywhere", ["4G LTE Router", "Noise Cancelling Mic", "Ergonomic Chair", "Encrypted SSD"])

    # SECURITY & PRIVACY
    build_ultimate_portal("home-defense", "Smart Security", ["Video Doorbell", "Smart Lock", "Wireless Camera", "Motion Sensor"])
    build_ultimate_portal("cyber-safe", "Digital Privacy", ["Hardware Security Key", "Privacy Screen", "Webcam Cover", "Encrypted Email"])

    # Add 92 more niches here...
    print("🚀 100-Portal Engine Deployed Successfully.")
