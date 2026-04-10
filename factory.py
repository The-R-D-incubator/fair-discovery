import os

# --- BRANDING & ASSETS ---
AMAZON_TAG = "fairdiscovery-20"
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"
AURORA_URL = "https://www.aurora-repair.com"

def generate_industry_report(item):
    return f"""
    <p>The global market for <strong>{item}</strong> has entered a transformative phase in 2026. As industrial standards shift toward decentralized infrastructure—particularly in the UK, EU, and South African markets—the requirement for verified hardware has become the primary operational bottleneck.</p>
    <p>Our technical board has identified that {item} integration now requires a multi-layered approach to both physical durability and digital handshake protocols. For enterprises operating in high-demand zones, we recommend a baseline hardware specification that exceeds standard ISO requirements by at least 15% to ensure a 10-year lifecycle ROI.</p>
    <p>Furthermore, the convergence of {item} with IoT-driven diagnostics means that cybersecurity can no longer be an afterthought. Every procurement decision must be audited against current encryption standards to prevent unauthorized data exfiltration at the edge.</p>
    """

def build_elite_portal(folder_name, title, keywords):
    root_affiliates = os.path.join(os.getcwd(), "affiliates")
    if not os.path.exists(root_affiliates): os.makedirs(root_affiliates)
    base_path = os.path.join(root_affiliates, folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # HUB
    with open(os.path.join(base_path, "index.html"), "w") as f:
        links = "".join([f'<a href="{k.lower().replace(" ", "-")}.html" style="display:block; padding:20px; margin:10px 0; background:#fff; border-left:5px solid #00d18a; text-decoration:none; color:#333; box-shadow:0 2px 5px rgba(0,0,0,0.1);"><strong>{k}</strong> &rarr;</a>' for k in keywords])
        f.write(f"<html><head><title>{title}</title><style>body{{font-family:sans-serif; background:#f4f7f6; padding:40px;}} .container{{max-width:800px; margin:auto;}}</style></head><body><div class='container'><h1>{title} Hub</h1>{links}</div></body></html>")

    # ARTICLES
    for k in keywords:
        filename = k.lower().replace(" ", "-") + ".html"
        with open(os.path.join(base_path, filename), "w") as art:
            art.write(f"""
            <html><head><title>{k} | Technical Report</title>
            <style>body{{font-family:Georgia, serif; line-height:1.8; max-width:800px; margin:auto; padding:40px; color:#222;}} h1{{font-family:sans-serif;}} .box{{background:#f1f5f9; padding:25px; border-radius:8px; margin:20px 0; font-family:sans-serif;}}</style>
            </head><body>
                <h1>Engineering Analysis: {k}</h1>
                {generate_industry_report(k)}
                <div class="box">
                    <h3>Procurement Verified</h3>
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
                <div style="background:#00d18a; color:white; padding:30px; border-radius:12px; text-align:center;">
                    <h3>Need Technical Support?</h3>
                    <a href="{AURORA_URL}" style="color:white; font-weight:bold; font-size:1.2em;">Visit Aurora-Repair.com</a>
                </div>
                <p><small>🛡️ <a href="{SURFSHARK_URL}">Secure VPN</a> | 💰 <a href="{HONEYGAIN_URL}">Bandwidth Bounty</a></small></p>
            </body></html>
            """)

if __name__ == "__main__":
    # --- THE FULL 100-SITE REGISTRY ---
    all_portals = [
        ("pro-solar", "Solar Infrastructure", ["Solar Inverter", "Lithium Battery", "Solar Panels"]),
        ("auto-tech", "Automotive Diagnostics", ["OBD2 Scanner", "ECU Tuner", "Car Battery Tester"]),
        ("star-gear", "Satellite Comms", ["Starlink Mount", "Travel Case", "Starlink Adapter"]),
        ("mining-ops", "Mining Technology", ["Gas Detector", "Rock Bolt Tester", "Mine Phone"]),
        ("agri-pro", "Precision Farming", ["Soil Sensor", "Farm Camera", "Irrigation Controller"]),
        ("med-lab", "Clinical Laboratory", ["Centrifuge", "Microscope Digital", "Hematology Analyzer"]),
        ("cnc-fab", "Precision Fabrication", ["CNC Router", "Plasma Cutter", "3D Printer Pro"]),
        ("survey-pro", "Geospatial Survey", ["Total Station", "Theodolite", "Laser Rangefinder"]),
        ("cyber-guard", "Network Security", ["Hardware Security Key", "Encrypted USB", "Privacy Screen"]),
        ("marine-ops", "Maritime Tech", ["Marine GPS", "VHF Radio", "Fish Finder"]),
        ("hvac-pro", "Climate Engineering", ["Smart Thermostat", "Anemometer", "UV Purifier"]),
        ("hydro-grow", "Hydroponic Systems", ["EC Meter", "PH Controller", "Grow Lights"]),
        ("fiber-ops", "Fiber Infrastructure", ["Fusion Splicer", "OTDR Tester", "Fiber Cleaver"]),
        ("bio-hacking", "Human Performance", ["Red Light Therapy", "Glucose Monitor", "Sleep Tracker"]),
        ("fleet-pro", "Fleet Management", ["GPS Tracker", "Dash Cam 4K", "ELD Device"]),
        ("audio-eng", "Acoustic Tech", ["Studio Monitor", "Audio Interface", "Condenser Mic"]),
        ("weld-tech", "Metallurgy Tools", ["MIG Welder", "TIG Welder", "Plasma Torch"]),
        ("lab-automation", "Lab Robotics", ["Liquid Handler", "Plate Reader", "Thermal Cycler"]),
        ("wood-shop", "Woodworking Pro", ["Table Saw", "Wood Lathe", "Dust Collector"]),
        ("remote-office", "Work From Anywhere", ["4G LTE Router", "Noise Cancelling Mic", "Docking Station"]),
        ("ev-infra", "EV Charging", ["Level 2 Charger", "EV Cable", "Tesla Adapter"]),
        ("clean-room", "Sanitary Tech", ["HEPA Filter", "Sticky Mat", "Anti-Static Bench"]),
        ("watch-tools", "Horology Repair", ["Timing Machine", "Case Opener", "Loup Magnifier"]),
        ("broadcast-pro", "Video Engineering", ["4K PTZ Camera", "Video Switcher", "Wireless HDMI"]),
        ("crypto-infra", "Blockchain Hardware", ["ASIC Miner", "Cold Wallet", "Mining Frame"]),
        ("restoration-pro", "Hardware Restoration", ["Ultrasonic Cleaner", "Sandblaster", "Parts Washer"]),
        ("warehouse-ops", "Logistics Tech", ["Label Printer", "Barcode Scanner", "Shipping Scale"]),
        ("security-pro", "Smart Surveillance", ["Video Doorbell", "Smart Lock", "Wireless Camera"]),
        ("survey-drone", "Aerial Inspection", ["Inspection Drone", "Thermal Camera Drone", "RTK Base"]),
        ("coffee-eng", "Barista Tech", ["Espresso Pro", "Burr Grinder", "Milk Frother"]),
        ("power-pro", "Contractor Tools", ["Impact Driver", "Rotary Hammer", "Circular Saw"]),
        ("tele-health", "Remote Clinical", ["Digital Stethoscope", "ECG Monitor", "Vitals Station"]),
        ("metrology-pro", "Measurement Science", ["Digital Caliper", "CMM Probe", "Bore Gauge"]),
        ("office-ergos", "Corporate Wellness", ["Standing Desk", "Ergonomic Chair", "Monitor Arm"]),
        ("data-center", "Server Hardware", ["Rack Server", "Network Switch", "PDU Strip"]),
        ("sat-phone", "Global Comms", ["Iridium Phone", "Satellite Messenger", "PLB Beacon"]),
        ("tactical-gear", "Field Operations", ["Night Vision", "Tactical Light", "Ballistic Helmet"]),
        ("water-tech", "Filtration Science", ["Reverse Osmosis", "UV Sterilizer", "Water Tester"]),
        ("printing-pro", "Large Format", ["Plotter Printer", "Vinyl Cutter", "Heat Press"]),
        ("theatre-tech", "Stage Engineering", ["DMX Controller", "Stage Light", "Fog Machine"]),
        # --- Continue adding to hit 100 ---
        ("robotics-pro", "Robotics Lab", ["Cobot Arm", "Lidar Scanner", "Servo Motor"]),
        ("radio-tech", "Ham Radio", ["SDR Receiver", "Antenna Tuner", "HF Transceiver"]),
        ("gym-tech", "Fitness Science", ["Smart Rower", "Massage Gun", "Smart Mirror"]),
        ("solar-marine", "Nautical Power", ["Marine Solar", "Wind Turbine", "NMEA Gateway"]),
        ("pc-build", "High Performance PC", ["RTX GPU", "Liquid Cooler", "NVMe SSD"]),
        ("smart-lighting", "Lutron/Hue Pro", ["Smart Dimmer", "LED Strip Pro", "Bridge Hub"]),
        ("emergency-prep", "Survival Tech", ["Solar Crank Radio", "Water Filter Pro", "EMP Bag"]),
        ("music-biz", "Instrument Tech", ["Synthesizer", "Drum Machine", "Pedal Board"]),
        ("leather-tech", "Crafting Tools", ["Leather Stitcher", "Skiving Machine", "Burnisher"]),
        ("jewelry-eng", "Jewelry Tools", ["Micro-Motor", "Steam Cleaner", "Ring Stretcher"])
    ]

    print(f"🚀 INITIATING MASSIVE STRIKE: {len(all_portals)} Portals.")
    for folder, title, keywords in all_portals:
        build_elite_portal(folder, title, keywords)
    print("🏁 ALL SYSTEMS DEPLOYED.")
