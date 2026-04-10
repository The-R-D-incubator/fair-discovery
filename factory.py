import os

# --- REVENUE & GLOBAL ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def build_ultimate_portal(folder_name, title, keywords):
    # FORCE PATH TO BE RELATIVE TO ROOT
    root_affiliates = os.path.join(os.getcwd(), "affiliates")
    if not os.path.exists(root_affiliates):
        os.makedirs(root_affiliates)
        
    base_path = os.path.join(root_affiliates, folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # 1. GENERATE HUB PAGE (index.html)
    with open(os.path.join(base_path, "index.html"), "w") as f:
        links = "".join([f'<li><a href="{k.lower().replace(" ", "-")}.html">{k}</a></li>' for k in keywords])
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Fair Discovery Global</title>
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
                <p>Global Solutions & Technical Guides 2026.</p>
                <hr>
                <ul>{links}</ul>
                <p><small>Partnered with <a href="{AURORA_URL}">Aurora Repair</a></small></p>
            </div>
        </body>
        </html>
        """)

    # 2. GENERATE ARTICLE PAGES
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        img_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80"
        
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Top Rated {k} for 2026</title>
                <style>
                    body {{ font-family: sans-serif; margin: 0; color: #333; line-height: 1.8; }}
                    .nav {{ background: #121212; color: white; padding: 15px; text-align: center; }}
                    .container {{ max-width: 800px; margin: auto; padding: 30px; }}
                    .hero-img {{ width: 100%; height: auto; border-radius: 12px; }}
                    .cta-box {{ background: #f1c40f; padding: 20px; border-radius: 12px; margin: 20px 0; text-align: center; }}
                </style>
            </head>
            <body>
                <div class="nav">FAIR DISCOVERY GLOBAL</div>
                <div class="container">
                    <h1>The 2026 Guide to {k}</h1>
                    <img src="{img_url}" class="hero-img">
                    <script type="text/javascript">
                        amzn_assoc_tracking_id = "{AMAZON_TAG}";
                        amzn_assoc_ad_mode = "search";
                        amzn_assoc_ad_type = "smart";
                        amzn_assoc_marketplace = "amazon";
                        amzn_assoc_region = "US";
                        amzn_assoc_title = "Global Inventory";
                        amzn_assoc_default_search_phrase = "{k}";
                    </script>
                    <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>
                    <div class="cta-box">
                        <a href="{HONEYGAIN_URL}">Claim $5 Honeygain Bonus →</a>
                    </div>
                </div>
            </body>
            </html>
            """)
    print(f"✅ Created: {folder_name}")

if __name__ == "__main__":
    all_portals = [
        ("pro-solar", "Energy Systems", ["Solar Inverter", "Lithium Battery", "Solar Panels"]),
        ("auto-tech", "Vehicle Diagnostics", ["OBD2 Scanner", "ECU Tuner"]),
        ("star-gear", "Starlink Accessories", ["Starlink Mount", "Travel Case"]),
        ("home-defense", "Smart Security", ["Video Doorbell", "Smart Lock"]),
        ("mining-tech", "Industrial Gear", ["Hard Hat Camera", "Gas Detector"]),
        ("marine-tech", "Marine Electronics", ["Marine GPS", "VHF Radio"]),
        ("agri-tech", "Smart Farming", ["Soil Sensor", "Farm Camera"]),
        ("health-tech", "Clinical Home Tech", ["Pulse Oximeter", "Air Purifier"])
    ]

    start_index = int(os.getenv("BATCH_START", 0))
    batch_size = 20
    current_batch = all_portals[start_index : start_index + batch_size]
    
    for folder, title, keywords in current_batch:
        build_ultimate_portal(folder, title, keywords)
    
    print("🚀 Batch process complete.")
