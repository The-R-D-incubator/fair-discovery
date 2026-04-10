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
    all_portals = [
        # --- BATCH 1-50 ---
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
        ("robotics-pro", "Robotics Lab", ["Cobot Arm", "Lidar Scanner", "Servo Motor"]),
        ("radio-tech", "Ham Radio", ["SDR Receiver", "Antenna Tuner", "HF Transceiver"]),
        ("gym-tech", "Fitness Science", ["Smart Rower", "Massage Gun", "Smart Mirror"]),
        ("solar-marine", "Nautical Power", ["Marine Solar", "Wind Turbine", "NMEA Gateway"]),
        ("pc-build", "High Performance PC", ["RTX GPU", "Liquid Cooler", "NVMe SSD"]),
        ("smart-lighting", "Lutron/Hue Pro", ["Smart Dimmer", "LED Strip Pro", "Bridge Hub"]),
        ("emergency-prep", "Survival Tech", ["Solar Crank Radio", "Water Filter Pro", "EMP Bag"]),
        ("music-biz", "Instrument Tech", ["Synthesizer", "Drum Machine", "Pedal Board"]),
        ("leather-tech", "Crafting Tools", ["Leather Stitcher", "Skiving Machine", "Burnisher"]),
        ("jewelry-eng", "Jewelry Tools", ["Micro-Motor", "Steam Cleaner", "Ring Stretcher"]),

        # --- THE FINAL SPRINT (51-100) ---
        ("lab-freezer", "Ultra-Low Temp Storage", ["Cryogenic Freezer", "Vaccine Fridge", "Freeze Dryer"]),
        ("drone-mapping", "Aerial Photogrammetry", ["Lidar Drone", "Multispectral Sensor", "RTK Ground Station"]),
        ("greenhouse-tech", "Commercial Cultivation", ["Climate Controller", "Auto-Doser", "Thermal Screen"]),
        ("packaging-pro", "Industrial Packaging", ["Vacuum Sealer", "Shrink Tunnel", "Pallet Wrapper"]),
        ("forklift-tech", "Warehouse Mobility", ["Electric Stacker", "Pallet Jack", "Forklift Battery"]),
        ("boiler-tech", "Thermal Engineering", ["Steam Boiler", "Heat Exchanger", "Pressure Gauge"]),
        ("valve-eng", "Flow Control Systems", ["Solenoid Valve", "Ball Valve", "Pneumatic Actuator"]),
        ("pump-tech", "Industrial Fluid Ops", ["Centrifugal Pump", "Diaphragm Pump", "Submersible Pump"]),
        ("crane-ops", "Overhead Lifting", ["Gantry Crane", "Jib Crane", "Hoist Controller"]),
        ("safe-storage", "High-Security Vaults", ["Biometric Safe", "Fireproof Cabinet", "Gun Safe"]),
        ("kitchen-pro", "Commercial Culinary", ["Combi Oven", "Blast Chiller", "Sous Vide Pro"]),
        ("gym-infra", "Facility Performance", ["Commercial Treadmill", "Squat Rack", "Cable Machine"]),
        ("physio-tech", "Rehabilitation Gear", ["Shockwave Therapy", "Laser Therapy", "TENS Unit"]),
        ("dental-tech", "Clinical Dentistry", ["Dental X-Ray", "Autoclave", "Intraoral Scanner"]),
        ("vet-med", "Veterinary Diagnostics", ["Vet Ultrasound", "Anesthesia Machine", "Vet Table"]),
        ("optometry-pro", "Visual Diagnostics", ["Phoropter", "Slit Lamp", "Autorefractor"]),
        ("audio-visual", "Conference Systems", ["Video Wall", "Ceiling Mic Array", "Control Processor"]),
        ("server-cool", "Data Center Thermal", ["Rack Cooling", "Immersion Cooling", "CRAH Unit"]),
        ("pos-tech", "Retail Infrastructure", ["Receipt Printer", "Cash Drawer", "Touch Terminal"]),
        ("kiosk-pro", "Self-Service Tech", ["Ordering Kiosk", "Check-in Kiosk", "Wayfinding Screen"]),
        ("vending-ops", "Automated Retail", ["Smart Vender", "Coin Mech", "Card Reader Pro"]),
        ("laundry-pro", "Industrial Washing", ["Commercial Dryer", "Washer Extractor", "Ironing Machine"]),
        ("pool-tech", "Aquatic Management", ["Variable Speed Pump", "Salt Chlorinator", "Pool Robot"]),
        ("spa-eng", "Wellness Engineering", ["Steam Generator", "Sauna Heater", "Hydrotherapy Jet"]),
        ("light-show", "Event Production", ["Moving Head Light", "LED Video Panel", "Laser Projector"]),
        ("sound-reinforcement", "Live Sound Tech", ["Line Array", "Digital Mixer", "Stage Monitor"]),
        ("recording-pro", "Studio Infrastructure", ["Vocal Booth", "Patch Bay", "Preamp Rack"]),
        ("film-gear", "Cinema Production", ["Camera Gimbal", "Follow Focus", "Matte Box"]),
        ("lighting-grip", "Film Studio Tech", ["C-Stand", "LED Softbox", "DMX Dimmer"]),
        ("battery-storage", "BESS Technology", ["Grid Battery", "Battery Management System", "DC Combiner"]),
        ("wind-power", "Wind Turbine Tech", ["Vertical Wind Turbine", "Anemometer", "Brake System"]),
        ("hydro-power", "Micro-Hydro Systems", ["Water Turbine", "Pelton Wheel", "Governor"]),
        ("gas-eng", "Natural Gas Tech", ["Gas Meter", "Leak Detector", "Regulator Station"]),
        ("welding-robot", "Automated Metallurgy", ["Welding Arm", "Positioner", "Wire Feeder"]),
        ("conveyor-pro", "Material Handling", ["Belt Conveyor", "Roller Track", "Sortation System"]),
        ("lab-glass", "Scientific Glassware", ["Rotary Evaporator", "Distillation Kit", "Glass Reactor"]),
        ("chem-ops", "Chemical Processing", ["Magnetic Stirrer", "Heating Mantle", "Chemical Pump"]),
        ("safety-gear", "PPE Industrial", ["Powered Respirator", "Safety Harness", "Gas Mask"]),
        ("fire-defense", "Suppression Systems", ["Fire Panel", "Smoke Detector Pro", "Extinguisher Cabinet"]),
        ("access-control", "Entry Security", ["Turnstile", "RFID Reader", "Maglock"]),
        ("parking-tech", "Revenue Parking", ["Boom Gate", "Ticket Dispenser", "LPR Camera"]),
        ("waste-ops", "Recycling Tech", ["Cardboard Baler", "Trash Compactor", "Glass Crusher"]),
        ("water-well", "Borehole Tech", ["Well Pump", "Drilling Rig", "Casing Pipe"]),
        ("irrigation-pro", "Agri-Water Tech", ["Center Pivot", "Drip Tape", "Pump Station"]),
        ("pest-tech", "Commercial Mitigation", ["Thermal Fogger", "Bait Station", "UV Trap"]),
        ("cold-chain", "Logistics Thermal", ["Reefer Unit", "Data Logger", "Insulated Container"]),
        ("air-cargo", "Aviation Logistics", ["ULD Container", "Cargo Loader", "X-Ray Scanner"]),
        ("rail-tech", "Railway Engineering", ["Track Switch", "Signaling System", "Locomotive Part"]),
        ("telecom-tower", "Cellular Infra", ["RF Amplifier", "Sector Antenna", "Tower Light"]),
        ("space-tech", "Satellite Engineering", ["Ground Station", "Star Tracker", "Ion Thruster"])
    ]

    print(f"🚀 INITIATING MASSIVE STRIKE: {len(all_portals)} Portals.")
    for folder, title, keywords in all_portals:
        build_elite_portal(folder, title, keywords)
    print("🏁 ALL SYSTEMS DEPLOYED.")
