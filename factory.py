import os

# --- BRANDING & REVENUE ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def get_tech_brief(item):
    """Generates professional technical context for each niche."""
    return f"""
    The implementation of {item} technology has seen a 40% rise in enterprise adoption across the UK and EU 
    sectors in 2026. As technical standards evolve, specifically regarding energy efficiency and data 
    integrity, selecting the correct hardware becomes a matter of operational stability. 
    Our analysis focuses on the structural durability and long-term ROI of these units, 
    ensuring that whether you are operating in the North American grid or the South African 
    industrial landscape, your deployment remains within compliance of GDPR and local POPIA regulations.
    """

def build_pro_portal(folder_name, title, keywords):
    root_affiliates = os.path.join(os.getcwd(), "affiliates")
    if not os.path.exists(root_affiliates): os.makedirs(root_affiliates)
    base_path = os.path.join(root_affiliates, folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # 1. THE PROFESSIONAL HUB
    with open(os.path.join(base_path, "index.html"), "w") as f:
        links = "".join([f'<a href="{k.lower().replace(" ", "-")}.html" class="grid-item"><h3>{k}</h3><p>Technical Brief & Procurement &rarr;</p></a>' for k in keywords])
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Fair Discovery Technical</title>
            <style>
                :root {{ --main: #2c3e50; --accent: #00d18a; --bg: #fdfdfd; }}
                body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: var(--bg); margin: 0; color: #333; }}
                header {{ background: var(--main); color: white; padding: 80px 20px; text-align: center; }}
                .container {{ max-width: 1000px; margin: -50px auto 50px; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
                .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 30px; }}
                .grid-item {{ border: 1px solid #eee; padding: 25px; text-decoration: none; color: inherit; transition: 0.3s; border-radius: 5px; }}
                .grid-item:hover {{ border-color: var(--accent); transform: translateY(-5px); }}
                h1 {{ margin: 0; font-size: 2.5em; }}
                .partner {{ text-align: center; margin-top: 40px; border-top: 1px solid #eee; padding-top: 20px; }}
            </style>
        </head>
        <body>
            <header><h1>{title}</h1><p>Global Industrial Standards & Procurement 2026</p></header>
            <div class="container">
                <p>Welcome to the Fair Discovery technical repository for <strong>{title}</strong>. This hub provides curated analysis and hardware specifications for professional deployment in the UK, EU, USA, and Southern Africa.</p>
                <div class="grid">{links}</div>
                <div class="partner">Partnered with <a href="{AURORA_URL}" style="color:var(--accent); font-weight:bold;">Aurora Repair Services</a></div>
            </div>
        </body>
        </html>
        """)

    # 2. THE PROFESSIONAL ARTICLE
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        img_url = f"https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80" # Tech Background
        
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{k} | Professional Technical Review 2026</title>
                <style>
                    body {{ font-family: 'Georgia', serif; line-height: 1.8; color: #222; margin: 0; background: #fff; }}
                    .top-bar {{ background: #000; color: #fff; padding: 10px 0; text-align: center; font-family: sans-serif; font-size: 12px; letter-spacing: 1px; }}
                    .hero-img {{ width: 100%; height: 450px; object-fit: cover; }}
                    .content {{ max-width: 750px; margin: auto; padding: 40px 20px; }}
                    h1 {{ font-family: sans-serif; font-size: 3em; line-height: 1.1; margin-bottom: 10px; }}
                    .meta {{ color: #888; font-family: sans-serif; text-transform: uppercase; font-size: 13px; margin-bottom: 40px; }}
                    .ad-mid {{ background: #f9f9f9; padding: 30px; border-left: 4px solid #00d18a; margin: 40px 0; font-family: sans-serif; }}
                    .btn-accent {{ background: #00d18a; color: white; padding: 15px 30px; text-decoration: none; border-radius: 4px; display: inline-block; font-family: sans-serif; font-weight: bold; }}
                    .aurora-footer {{ background: #2c3e50; color: white; padding: 60px 20px; margin-top: 60px; text-align: center; font-family: sans-serif; }}
                </style>
            </head>
            <body>
                <div class="top-bar">FAIR DISCOVERY GLOBAL INDUSTRIAL REPORT — 2026</div>
                <img src="{img_url}" class="hero-img">
                <div class="content">
                    <div class="meta">Hardware Analysis • South Africa / EU / UK / USA</div>
                    <h1>Comprehensive Engineering Analysis: {k}</h1>
                    <p><em>By the Fair Discovery Technical Board</em></p>
                    
                    <p>{get_tech_brief(k)}</p>
                    
                    <div class="ad-mid">
                        <h3>Verified {k} Procurement</h3>
                        <p>Our lab has verified the following hardware for immediate deployment.</p>
                        <script type="text/javascript">
                            amzn_assoc_tracking_id = "{AMAZON_TAG}";
                            amzn_assoc_ad_mode = "search";
                            amzn_assoc_ad_type = "smart";
                            amzn_assoc_marketplace = "amazon";
                            amzn_assoc_region = "US";
                            amzn_assoc_default_search_phrase = "{k}";
                        </script>
                        <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>
                    </div>

                    <p>Safety and cybersecurity remain the primary bottlenecks for {k} integration. We recommend implementing a 256-bit encrypted tunnel for all diagnostic data transfers.</p>
                    
                    <a href="{SURFSHARK_URL}" class="btn-accent">Secure Diagnostics with Surfshark &rarr;</a>
                    
                    <div style="margin-top:40px;">
                        <h3>Resource Optimization</h3>
                        <p>Enterprises can offset data costs via the Honeygain network. <a href="{HONEYGAIN_URL}">Claim $5 Deployment Bonus &rarr;</a></p>
                    </div>
                </div>

                <div class="aurora-footer">
                    <h2>Technical Support & Maintenance</h2>
                    <p>For high-end repair services of {k} and other hardware, contact our primary partner.</p>
                    <a href="{AURORA_URL}" style="color:#00d18a; font-size: 1.5em; text-decoration:none; font-weight:bold;">WWW.AURORA-REPAIR.COM</a>
                </div>
            </body>
            </html>
            """)
    print(f"✅ Polished: {folder_name}")

if __name__ == "__main__":
    # Example Batch of the first 20 (Keep your logic, just using the new function)
    all_portals = [
        ("pro-solar", "Renewable Energy Infrastructure", ["Solar Inverter", "Lithium Battery", "Solar Panels"]),
        ("auto-tech", "Automotive Diagnostics", ["OBD2 Scanner", "ECU Tuner"]),
        # ... your full list here ...
    ]
    
    import os
    start_index = int(os.getenv("BATCH_START", 0))
    current_batch = all_portals[start_index : start_index + 20]
    
    for folder, title, keywords in current_batch:
        build_pro_portal(folder, title, keywords)
