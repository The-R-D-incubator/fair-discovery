import os

# --- REVENUE & GLOBAL ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def generate_industry_report(item):
    return f"""
    <p>The global market for <strong>{item}</strong> has entered a transformative phase in 2026. As industrial standards shift toward decentralized infrastructure—particularly in the UK, EU, and South African markets—the requirement for verified, high-uptime hardware has become the primary operational bottleneck.</p>
    <p>Our technical board has identified that {item} integration now requires a multi-layered approach to both physical durability and digital handshake protocols. For enterprises operating in high-demand zones, we recommend a baseline hardware specification that exceeds standard ISO requirements by at least 15% to ensure a 10-year lifecycle ROI.</p>
    <p>Furthermore, the convergence of {item} with IoT-driven diagnostics means that cybersecurity can no longer be an afterthought. Every procurement decision must be audited against current encryption standards to prevent unauthorized data exfiltration at the edge.</p>
    """

def build_elite_portal(folder_name, title, keywords):
    root_affiliates = os.path.join(os.getcwd(), "affiliates")
    if not os.path.exists(root_affiliates): os.makedirs(root_affiliates)
    base_path = os.path.join(root_affiliates, folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # HUB GENERATOR
    with open(os.path.join(base_path, "index.html"), "w") as f:
        links = "".join([f'<a href="{k.lower().replace(" ", "-")}.html" class="card"><h3>{k}</h3><p>Technical Specs &rarr;</p></a>' for k in keywords])
        f.write(f"""
        <html><head><title>{title} | Technical Intelligence</title>
        <style>
            :root {{ --dark: #0f172a; --green: #00d18a; }}
            body {{ font-family: sans-serif; margin:0; background: #f8fafc; color: #1e293b; }}
            header {{ background: var(--dark); color: white; padding: 80px 20px; text-align: center; }}
            .container {{ max-width: 1100px; margin: -50px auto 60px; padding: 20px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
            .card {{ background: white; padding: 25px; border-radius: 12px; text-decoration: none; color: inherit; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid var(--green); transition: 0.3s; }}
            .card:hover {{ transform: translateY(-5px); }}
        </style></head>
        <body><header><h1>{title}</h1><p>2026 Procurement Advisory</p></header>
        <div class="container"><div class="grid">{links}</div></div></body></html>
        """)

    # ARTICLE GENERATOR
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        img_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80"
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <html><head><title>{k} | Engineering Analysis</title>
            <style>
                body {{ font-family: 'Georgia', serif; line-height: 1.8; color: #232323; margin: 0; }}
                .nav {{ padding: 15px; background: #0f172a; color: white; text-align: center; font-family: sans-serif; font-size: 12px; letter-spacing: 2px; }}
                .hero {{ height: 300px; background: url('{img_url}') center/cover; }}
                .main {{ max-width: 800px; margin: 40px auto; padding: 0 20px; }}
                .ad-box {{ background: #f1f5f9; padding: 25px; border-radius: 8px; margin: 30px 0; font-family: sans-serif; }}
                .cta {{ background: #00d18a; color: white; padding: 30px; border-radius: 12px; text-align: center; font-family: sans-serif; }}
                .btn {{ background: white; color: #00d18a; padding: 12px 25px; text-decoration: none; border-radius: 6px; font-weight: bold; display: inline-block; margin-top: 15px; }}
            </style></head>
            <body>
                <div class="nav">FAIR DISCOVERY GLOBAL TECHNICAL ADVISORY</div>
                <div class="hero"></div>
                <div class="main">
                    <h1>{k} Technical Report</h1>
                    {generate_industry_report(k)}
                    <div class="ad-box">
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
                    <div class="cta">
                        <h3>Industrial Support</h3>
                        <p>For large-scale maintenance of {k} systems.</p>
                        <a href="{AURORA_URL}" class="btn">Visit Aurora Repair</a>
                    </div>
                    <p style="margin-top:40px; font-size: 14px; font-family: sans-serif;">
                        🛡️ Secure diagnostics with <a href="{SURFSHARK_URL}">Surfshark VPN</a> | 
                        💰 Fund your data via <a href="{HONEYGAIN_URL}">Honeygain</a>
                    </p>
                </div>
            </body></html>
            """)

if __name__ == "__main__":
    all_portals = [
        # BATCH 0-19 (Already created, but update them with 10x design)
        ("pro-solar", "Renewable Energy", ["Solar Inverter", "Lithium Battery", "Solar Panels"]),
        ("auto-tech", "Automotive Diagnostics", ["OBD2 Scanner", "ECU Tuner", "Car Battery Tester"]),
        ("star-gear", "Satellite Performance", ["Starlink Mount", "Travel Case", "Ethernet Adapter"]),
        ("mining-tech", "Industrial Mining", ["Hard Hat Camera", "Gas Detector", "Rock Bolt Tester"]),
        ("agri-tech", "Precision Farming", ["Soil Sensor", "Farm Camera", "Drone Diagnostic"]),
        ("backup-power", "Grid Resilience", ["Portable Power Station", "Pure Sine Inverter", "UPS for WiFi"]),
        ("cyber-safe", "Digital Privacy", ["Hardware Security Key", "Privacy Screen", "Encrypted USB"]),
        ("fleet-pro", "Fleet Management", ["GPS Tracker", "Dash Cam 4K", "ELD Device"]),
        ("health-tech", "Home Clinical Tech", ["Pulse Oximeter", "Air Purifier", "Smart Scale"]),
        ("lab-supplies", "Professional Lab Gear", ["Digital Microscope", "Centrifuge", "Lab Power Supply"]),
        ("marine-tech", "Marine Electronics", ["Marine GPS", "VHF Radio", "Fish Finder"]),
        ("precision-tools", "Engineering Lab", ["Digital Micrometer", "Laser Level", "Dial Indicator"]),
        ("remote-comms", "Global Connectivity", ["4G LTE Router", "Satellite Messenger", "WiFi Mesh"]),
        ("restoration-tech", "Technical Restoration", ["Ultrasonic Cleaner", "Soldering Station", "Parts Washer"]),
        ("warehouse-ops", "Logistics Hardware", ["Label Printer", "Barcode Scanner", "Shipping Scale"]),
        ("home-defense", "Smart Security", ["Video Doorbell", "Smart Lock", "Wireless Camera"]),
        ("office-pro", "Enterprise Workspace", ["Ergonomic Chair", "Dual Monitor Arm", "Docking Station"]),
        ("sound-eng", "Acoustic Engineering", ["Studio Monitor", "Audio Interface", "Condenser Mic"]),
        ("hvac-tech", "Climate Control", ["Smart Thermostat", "Anemometer", "UV Air Purifier"]),
        ("ev-charging", "Electric Vehicle Infra", ["Level 2 Charger", "Charging Cable", "EV Adapter"]),
        
        # BATCH 20-39 (THE NEW FRONTIER)
        ("cnc-fab", "Precision Fabrication", ["CNC Router", "Plasma Cutter", "3D Printer Industrial"]),
        ("survey-tech", "Geospatial Tools", ["Total Station", "Theodolite", "Laser Rangefinder"]),
        ("hydro-grow", "Controlled Agriculture", ["Hydroponic Pump", "Grow Light Full Spectrum", "EC Meter"]),
        ("wood-shop", "Professional Woodworking", ["Table Saw", "Wood Lathe", "Dust Collector"]),
        ("metrology-pro", "Measurement Science", ["CMM Machine", "Optical Comparator", "Thread Gauge"]),
        ("tele-med", "Remote Healthcare", ["Telehealth Camera", "Bluetooth Stethoscope", "ECG Monitor"]),
        ("crypto-mining", "Blockchain Infra", ["ASIC Miner", "Mining Rig Frame", "PDU Power Strip"]),
        ("fiber-ops", "Network Infrastructure", ["Fiber Fusion Splicer", "OTDR Tester", "Fiber Cleaver"]),
        ("bio-hacking", "Performance Science", ["Red Light Therapy", "Cold Plunge Tub", "Continuous Glucose Monitor"]),
        ("coffee-tech", "Barista Engineering", ["Espresso Machine Pro", "Burr Grinder", "Milk Frother Commercial"]),
        ("vape-tech", "Aerosol Engineering", ["Vape Mod High End", "Ultrasonic Cleaner", "Ohm Meter"]),
        ("watch-repair", "Horology Tools", ["Watch Timing Machine", "Case Opener", "Bergeon Screwdriver"]),
        ("solar-marine", "Off-Grid Nautical", ["Flexible Solar Panel", "MPPT Controller", "Marine Battery"]),
        ("av-pro", "Broadcast Hardware", ["4K PTZ Camera", "Video Switcher", "Wireless Video Link"]),
        ("robotics-edu", "STEM Robotics", ["Cobot Arm", "Lidar Module", "Single Board Computer"]),
        ("hifi-audio", "Audiophile Systems", ["Tube Amplifier", "Vinyl Turntable", "DAC Converter"]),
        ("power-tools", "Contractor Grade", ["Impact Driver", "Rotary Hammer", "Table Saw"]),
        ("weld-tech", "Metallurgy Tools", ["MIG Welder", "TIG Welder", "Welding Helmet Auto-Dark"]),
        ("clean-room", "Sanitary Environments", ["HEPA Filter", "Sticky Mat", "Anti-Static Bench"]),
        ("camping-tech", "Overland Gear", ["Portable Fridge", "Roof Top Tent", "Solar Lantern"])
    ]

    start_index = int(os.getenv("BATCH_START", 0))
    current_batch = all_portals[start_index : start_index + 20]
    
    for folder, title, keywords in current_batch:
        build_elite_portal(folder, title, keywords)
    print(f"🚀 Successfully deployed batch starting at {start_index}")
