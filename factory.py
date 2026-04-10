import os

# --- REVENUE & GLOBAL ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def build_ultimate_portal(folder_name, title, keywords):
    """Generates a professional B2B/Consumer portal with triple monetization."""
    if not os.path.exists("affiliates"):
        os.makedirs("affiliates")
        
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # 1. GENERATE HUB PAGE (index.html)
    with open(f"{base_path}/index.html", "w") as f:
        links = "".join([f'<li><a href="{k.lower().replace(" ", "-")}.html">{k}</a></li>' for k in keywords])
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Fair Discovery Global</title>
            <style>
                body {{ font-family: 'Inter', sans-serif; padding: 5%; line-height: 1.6; background: #f4f4f4; color: #333; }}
                .container {{ max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
                h1 {{ color: #00d18a; border-bottom: 2px solid #00d18a; padding-bottom: 10px; }}
                ul {{ list-style: none; padding: 0; }}
                li {{ margin: 15px 0; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
                a {{ color: #0055ff; text-decoration: none; font-weight: bold; }}
                footer {{ margin-top: 30px; font-size: 12px; color: #777; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{title}</h1>
                <p>Global Procurement & Technical Resource Center (2026).</p>
                <ul>{links}</ul>
                <div style="margin-top:40px; padding:20px; background:#f0f7ff; border-radius:10px;">
                    <p><strong>Technical Partner:</strong> Restoration and maintenance provided by <a href="{AURORA_URL}">Aurora Repair</a>.</p>
                </div>
                <footer>&copy; 2026 Fair Discovery Network | GDPR & POPIA Compliant</footer>
            </div>
        </body>
        </html>
        """)

    # 2. GENERATE ARTICLE PAGES (SEO Optimized)
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        img_url = f"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80"
        
        with open(f"{base_path}/{filename}", "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Top Rated {k} for 2026 | Global Procurement Guide</title>
                <script type="application/ld+json">
                {{
                  "@context": "https://schema.org/",
                  "@type": "Product",
                  "name": "{k}",
                  "description": "Professional technical analysis and hardware review for {k}.",
                  "brand": {{ "@type": "Brand", "name": "Fair Discovery Verified" }}
                }}
                </script>
                <style>
                    body {{ font-family: -apple-system, system-ui, sans-serif; margin: 0; color: #1a1a1a; line-height: 1.8; }}
                    .nav {{ background: #121212; color: white; padding: 15px; text-align: center; font-weight: bold; letter-spacing: 1px; }}
                    .container {{ max-width: 800px; margin: auto; padding: 30px; }}
                    .hero-img {{ width: 100%; height: auto; border-radius: 12px; margin: 20px 0; }}
                    .cta-box {{ background: #f1c40f; color: #000; padding: 25px; border-radius: 12px; margin: 30px 0; font-weight: bold; text-align: center; }}
                    .aurora-card {{ border: 3px solid #00d18a; padding: 25px; border-radius: 15px; margin: 30px 0; text-align: center; }}
                    .btn {{ padding: 12px 25px; background: #00d18a; color: white; text-decoration: none; border-radius: 5px; font-weight: 800; display: inline-block; }}
                    .amazon-area {{ min-height: 250px; background: #f9f9f9; padding: 20px; border-radius: 10px; }}
                </style>
            </head>
            <body>
                <div class="nav">FAIR DISCOVERY GLOBAL</div>
                <div class="container">
                    <h1>The 2026 Guide to Professional {k}</h1>
                    <img src="{img_url}" class="hero-img" alt="{k}">
                    
                    <p>Our lab monitors hardware trends across <strong>North America, the UK, Europe, and South Africa</strong>. For {k}, we prioritize industrial-grade reliability.</p>

                    <div class="amazon-area">
                        <script type="text/javascript">
                            amzn_assoc_tracking_id = "{AMAZON_TAG}";
                            amzn_assoc_ad_mode = "search";
                            amzn_assoc_ad_type = "smart";
                            amzn_assoc_marketplace = "amazon";
                            amzn_assoc_region = "US";
                            amzn_assoc_title = "Global {k} Inventory";
                            amzn_assoc_default_search_phrase = "{k}";
                        </script>
                        <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>
                    </div>

                    <div class="aurora-card">
                        <h3>Restoration & Support</h3>
                        <p>Need professional setup or technical repair for your hardware?</p>
                        <a href="{AURORA_URL}" class="btn">Visit Aurora-Repair.com</a>
                    </div>

                    <div class="cta-box">
                        💰 Passive Income: Share your bandwidth and get a $5 bonus.
                        <br><a href="{HONEYGAIN_URL}">Claim Honeygain Bonus →</a>
                    </div>

                    <div style="background:#0055ff; color:white; padding:20px; border-radius:10px; text-align:center;">
                        <a href="{SURFSHARK_URL}" style="color:white; font-weight:bold;">Secure your entire network with Surfshark VPN →</a>
                    </div>
                </div>
            </body>
            </html>
            """)
    print(f"✅ Created Batch Item: {folder_name}")

if __name__ == "__main__":
    # --- THE MASTER 100 SITE REGISTRY ---
    all_portals = [
        # Batch 1: Power & Energy
        ("pro-solar", "Industrial Energy", ["Solar Inverter", "Lithium Battery", "Solar Panels"]),
        ("backup-power", "Load Shedding Hub", ["Portable Power Station", "Pure Sine Inverter", "UPS for WiFi"]),
        # Batch 2: Auto & Fleet
        ("auto-tech", "Vehicle Diagnostics", ["OBD2 Scanner", "ECU Tuner", "Car Battery Tester"]),
        ("fleet-pro", "Fleet Management", ["GPS Tracker", "Dash Cam 4K", "ELD Device"]),
        # Batch 3: Starlink & Connectivity
        ("star-gear", "Starlink Performance", ["Starlink Mount", "Travel Case", "Ethernet Adapter"]),
        ("remote-comms", "Global Connectivity", ["4G LTE Router", "Satellite Messenger", "WiFi Mesh 6E"]),
        # Batch 4: Home & Personal Security
        ("home-defense", "Smart Security", ["Video Doorbell", "Smart Lock", "Wireless Camera"]),
        ("cyber-safe", "Digital Privacy", ["Hardware Security Key", "Privacy Screen", "Encrypted USB"]),
        # Batch 5: Industrial & Lab (B2B)
        ("lab-supplies", "Professional Lab Gear", ["Digital Microscope", "Centrifuge Machine", "Lab Power Supply"]),
        ("warehouse-ops", "Logistics Hardware", ["Label Printer Industrial", "Barcode Scanner Wireless", "Shipping Scale"]),
        # Batch 6: Professional Tools
        ("precision-tools", "Engineering Lab", ["Digital Micrometer", "Laser Level Pro", "Dial Indicator"]),
        ("restoration-tech", "Technical Restoration", ["Ultrasonic Cleaner Pro", "Soldering Station Digital", "Parts Washer"]),
        # ... You can add more triples here until you hit 100 ...
    ]

    # --- BATCH LOGIC ---
    start_index = int(os.getenv("BATCH_START", 0))
    batch_size = 20
    current_batch = all_portals[start_index : start_index + batch_size]
    
    print(f"🚀 STRIKE INITIATED: Processing sites {start_index} to {start_index + batch_size}")
    
    for folder, title, keywords in current_batch:
        build_ultimate_portal(folder, title, keywords)
    
    print("🏁 STRIKE COMPLETE. Syncing to Global Network.")
