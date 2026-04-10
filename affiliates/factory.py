import os

# --- YOUR REVENUE KEYS ---
AMAZON_TAG = "fairdiscovery-20" 
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"

def build_niche_site(folder_name, title, keywords):
    """Generates a mini-site inside a subfolder with Auto-Pilot Ads & Passive Income"""
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # Create the landing page for this niche
    with open(f"{base_path}/index.html", "w") as f:
        f.write(f"""
        <html>
        <head><title>{title} | Fair Discovery</title></head>
        <body style="font-family:sans-serif; padding:40px; line-height:1.6; max-width:900px; margin:auto;">
            <h1>{title}</h1>
            <p>Expert guides and hardware reviews for 2026. Managed by the Fair Discovery Network.</p>
            <hr>
            <h3>Research Categories:</h3>
            <ul>
        """)
        
        # Generate 1 page for every keyword
        for k in keywords:
            filename = k.lower().replace(" ", "-") + ".html"
            f.write(f'<li><a href="{filename}">{k}</a></li>')
            
            # THE SMART AD BLOCK (The "Auto-Pilot" code)
            amazon_widget = f"""
            <div id="amzn-assoc-ad-fd-network"></div>
            <script type="text/javascript">
                amzn_assoc_tracking_id = "{AMAZON_TAG}";
                amzn_assoc_ad_mode = "search";
                amzn_assoc_ad_type = "smart";
                amzn_assoc_marketplace = "amazon";
                amzn_assoc_region = "US";
                amzn_assoc_title = "Recommended {k} Gear";
                amzn_assoc_default_search_phrase = "{k}"; 
                amzn_assoc_default_category = "All";
                amzn_assoc_linkid = "fd_auto_search_widget";
            </script>
            <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"></script>
            """
            
            # Create the actual article page
            with open(f"{base_path}/{filename}", "w") as art:
                art.write(f"""
                <html>
                <head><title>Best {k} 2026 | Fair Discovery</title></head>
                <body style="font-family:sans-serif; padding:40px; line-height:1.6; max-width:800px; margin:auto;">
                    <small>Fair Discovery > {title}</small>
                    <h1>The Best {k} in 2026</h1>
                    <p>When looking for {k}, security and reliability are key. Our team has vetted the following options based on performance and search intent.</p>
                    
                    <div style="margin: 30px 0;">
                        {amazon_widget}
                    </div>

                    <div style="background:#fff9e6; padding:20px; border-radius:10px; border: 1px solid #ffe699; margin: 20px 0;">
                        <strong>💰 Passive Income Tip:</strong> Want to offset your internet costs? 
                        Share your unused bandwidth with Honeygain and get paid. 
                        <a href="{HONEYGAIN_URL}">Claim your $5 starting bonus here →</a>
                    </div>

                    <div style="background:#f0f7ff; padding:20px; border-radius:10px; border-left:5px solid #00d18a;">
                        <strong>Privacy Note:</strong> Always protect your data while shopping. 
                        <a href="{SURFSHARK_URL}">Secure your connection with Surfshark VPN →</a>
                    </div>
                    
                    <hr>
                    <a href="index.html">Back to {title} Hub</a>
                </body></html>
                """)
        
        f.write("</ul></body></html>")
    print(f"✅ Created {title} at /affiliates/{folder_name}")

if __name__ == "__main__":
    # BATCH 1: The Foundation
    build_niche_site("privacy-hub", "Global Privacy Portal", ["VPN for PC", "Secure Routers", "Encrypted Email", "Hardware Security Keys"])
    build_niche_site("workshop-gear", "Elite Diagnostic Tools", ["OBD2 Scanner", "Digital Multimeter", "Thermal Camera", "Tire Pressure Monitor"])
    
    # BATCH 2: SA Energy & Security
    build_niche_site("power-solutions", "SA Load Shedding Backup", ["Pure Sine Wave Inverter", "LiFePO4 Battery", "Portable Power Station", "Solar Charge Controller"])
    build_niche_site("road-safety", "Dashcam & Vehicle Security", ["4K Dash Cam", "GPS Tracker", "Blind Spot Monitor", "Reverse Camera Kit"])

    # BATCH 3: Starlink & Future Comms
    build_niche_site("star-comms", "Starlink Performance Hub", ["Starlink Ethernet Adapter", "Starlink Wall Mount", "Starlink Travel Case", "WiFi Mesh System"])

    print("\n🚀 Engine Ready. Run this script, then push the /affiliates folder to GitHub.")
