import os

# --- REVENUE & GLOBAL ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def build_ultimate_portal(folder_name, title, keywords):
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        # Dynamic professional image query
        img_url = f"https://source.unsplash.com/800x450/?{k.replace(' ', ',')},technology"
        
        with open(f"{base_path}/{filename}", "w") as art:
            art.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Top Rated {k} for 2026 | Global Procurement Guide</title>
                
                <link rel="alternate" hreflang="en-us" href="https://fairdiscovery.github.io/{folder_name}/{filename}" />
                <link rel="alternate" hreflang="en-gb" href="https://fairdiscovery.github.io/{folder_name}/{filename}" />
                <link rel="alternate" hreflang="en-za" href="https://fairdiscovery.github.io/{folder_name}/{filename}" />
                <link rel="alternate" hreflang="en-ca" href="https://fairdiscovery.github.io/{folder_name}/{filename}" />

                <script type="application/ld+json">
                {{
                  "@context": "https://schema.org/",
                  "@type": "Product",
                  "name": "{k}",
                  "description": "Professional review and procurement guide for {k} in 2026.",
                  "brand": {{ "@type": "Brand", "name": "Fair Discovery Verified" }},
                  "offers": {{
                    "@type": "AggregateOffer",
                    "offerCount": "10",
                    "lowPrice": "49.00",
                    "highPrice": "5000.00",
                    "priceCurrency": "USD"
                  }}
                }}
                </script>

                <style>
                    :root {{ --primary: #00d18a; --secondary: #0055ff; --dark: #121212; }}
                    body {{ font-family: 'Inter', sans-serif; margin: 0; color: #333; line-height: 1.8; }}
                    .nav {{ background: #fff; border-bottom: 1px solid #eee; padding: 15px; display: flex; justify-content: space-between; }}
                    .hero-img {{ width: 100%; height: 400px; object-fit: cover; border-radius: 15px; margin: 20px 0; }}
                    .container {{ max-width: 900px; margin: auto; padding: 20px; }}
                    .cta-box {{ background: var(--dark); color: white; padding: 30px; border-radius: 15px; text-align: center; margin: 40px 0; }}
                    .aurora-link {{ border: 2px solid var(--primary); padding: 20px; border-radius: 10px; margin-top: 30px; text-align: center; }}
                    .btn {{ padding: 12px 25px; border-radius: 5px; text-decoration: none; font-weight: bold; display: inline-block; }}
                </style>
            </head>
            <body>
                <div class="nav">
                    <strong>FAIR DISCOVERY</strong>
                    <a href="{AURORA_URL}" style="color:var(--primary); text-decoration:none;">Partner: Aurora Repair</a>
                </div>

                <div class="container">
                    <h1>The 2026 Global Guide to {k}</h1>
                    <img src="{img_url}" class="hero-img" alt="{k} hardware display">
                    
                    <p>Our lab at <strong>Fair Discovery</strong> provides technical procurement data for enterprises and high-end consumers across North America, Europe, and Southern Africa. When selecting <strong>{k}</strong>, we prioritize structural integrity and digital security.</p>

                    <div style="margin: 40px 0;">
                        <script type="text/javascript">
                            amzn_assoc_tracking_id = "{AMAZON_TAG}";
                            amzn_assoc_ad_mode = "search";
                            amzn_assoc_ad_type = "smart";
                            amzn_assoc_marketplace = "amazon";
                            amzn_assoc_region = "US";
                            amzn_assoc_title = "Global Inventory: {k}";
                            amzn_assoc_default_search_phrase = "{k}";
                        </script>
                        <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>
                    </div>

                    <div class="aurora-link">
                        <h3>Need Professional Support or Repair?</h3>
                        <p>For high-end hardware maintenance and technical restoration, visit our partners at Aurora Repair.</p>
                        <a href="{AURORA_URL}" class="btn" style="background:var(--primary); color:white;">Visit Aurora-Repair.com</a>
                    </div>

                    <div class="cta-box">
                        <h3>Offset Your Tech Costs</h3>
                        <p>Turn your unused bandwidth into passive revenue while you research.</p>
                        <a href="{HONEYGAIN_URL}" class="btn" style="background:#f1c40f; color:black;">Claim $5 Honeygain Bonus</a>
                    </div>
                </div>

                <footer style="padding: 40px; text-align: center; background: #f4f4f4; font-size: 12px;">
                    Region Targeting: USA | CAN | UK | EU | ZA. 
                    <br>All analysis compliant with GDPR & POPIA standards.
                </footer>
            </body>
            </html>
            """)

if __name__ == "__main__":
    # The Full 100-Site Sprint (Example Batches)
    build_ultimate_portal("pro-solar", "Industrial Energy", ["Solar Inverter", "Lithium Home Battery", "Charge Controller"])
    build_ultimate_portal("workshop-tools", "Diagnostic Solutions", ["OBD2 Scanner", "Thermal Imaging Camera", "Oscilloscope"])
    print("🚀 Ultimate SEO Engine Deployed with Aurora-Repair integration.")
