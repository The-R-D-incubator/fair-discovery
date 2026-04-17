import os
import datetime
import random

# --- 1. CONFIG & BATCHING ---
BATCH_START = int(os.environ.get("BATCH_START", 0))
BATCH_SIZE = 1000 
BASE_URL = "https://fairdiscovery.org"
ADSENSE_ID = "ca-pub-3215536871572990"
GA_ID = "G-C6Z3VMB0ND"

# --- 2. THE REVENUE STACK ---
LINKS = {
    "nord_vpn": "https://go.nordvpn.net/aff_c?offer_id=15&aff_id=145959&url_id=902",
    "nord_pass": "https://go.nordpass.io/aff_c?offer_id=488&aff_id=145959&url_id=9356",
    "honeygain": "https://join.honeygain.com/PRINY5083C",
    "surfshark": "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160",
    "aurora": "https://www.aurora-repair.com",
    "amazon": "fairdiscovery-20"
}

def get_image(k):
    """Dynamic tech-focused image fetcher."""
    sources = [
        f"https://source.unsplash.com/800x450/?{k.replace(' ', ',')},industrial",
        f"https://loremflickr.com/800/450/{k.replace(' ', ',')},tech",
        f"https://picsum.photos/seed/{k.replace(' ', '')}/800/450"
    ]
    return random.choice(sources)

def generate_header(keyword):
    today = datetime.date.today().strftime("%Y-%m-%d")
    return f"""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="2026 Technical analysis of {keyword} systems. Industrial ROI and security protocols verified.">
    <title>{keyword} | Technical Analysis 2026</title>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
      function trackAff(l){{gtag('event','click',{{'event_category':'Affiliate','event_label':l}});}}
    </script>
    <style>
        :root {{ --primary: #00d18a; --nord: #005ae6; --honey: #ffbf00; --dark: #1a2a3a; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: #f4f7f6; margin: 0; line-height: 1.6; color: #333; }}
        .nav {{ background: var(--dark); padding: 15px 20px; color: white; display: flex; justify-content: space-between; }}
        .nav a {{ color: white; text-decoration: none; font-weight: bold; font-size: 14px; }}
        .container {{ max-width: 850px; margin: 30px auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }}
        .hero-img {{ width: 100%; height: 350px; object-fit: cover; border-radius: 8px; margin-bottom: 25px; }}
        .ad-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; }}
        .ad-card {{ border: 1px solid #eee; padding: 20px; border-radius: 10px; border-top: 4px solid var(--primary); transition: 0.3s; cursor: pointer; text-decoration:none; color:inherit; display:block; }}
        .ad-card.nord {{ border-top: 4px solid var(--nord); }}
        .ad-card.honey {{ border-top: 4px solid var(--honey); }}
        .ad-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 12px 25px; text-decoration: none; font-weight: bold; border-radius: 6px; margin-top: 10px; }}
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
            <a href="{LINKS['aurora']}">SUPPORT</a>
        </div>
        <div class="container">
            <img src="{get_image(keyword)}" class="hero-img">
            <h1>2026 Engineering Guide: {keyword}</h1>
            <p>Verified technical analysis of <strong>{keyword}</strong> infrastructure deployment. Audit focus: hardware resilience, diagnostic handshakes, and 2026 network security standards.</p>
            
            <div class="ad-grid">
                <a href="{LINKS['nord_vpn']}" class="ad-card nord" onclick="trackAff('NordVPN')">
                    <small style="color:var(--nord); font-weight:bold;">ENCRYPTION</small>
                    <h4>Secure {keyword} Stream</h4>
                    <p>Protect your industrial data with NordVPN tunnels.</p>
                </a>
                <a href="{LINKS['honeygain']}" class="ad-card honey" onclick="trackAff('Honeygain')">
                    <small style="color:var(--honey); font-weight:bold;">PASSIVE REVENUE</small>
                    <h4>Monetize Idle Bandwidth</h4>
                    <p>Turn your {keyword} network into passive income with Honeygain.</p>
                </a>
                <a href="{LINKS['nord_pass']}" class="ad-card" onclick="trackAff('NordPass')">
                    <small style="color:var(--primary); font-weight:bold;">SECURITY</small>
                    <h4>Credential Management</h4>
                    <p>Encrypted vaulting for all {keyword} system passwords.</p>
                </a>
            </div>

            <div style="background:var(--dark); color:white; padding:30px; border-radius:10px; text-align:center;">
                <h3>Professional Calibration Support</h3>
                <p>Onsite and remote diagnostics for {keyword} via Aurora Repair.</p>
                <a href="{LINKS['aurora']}" class="btn">Contact Aurora &rarr;</a>
            </div>
            
            <p style="font-size:10px; color:#aaa; margin-top:40px; text-align:center;">
                Associate Disclosure: As an Amazon Associate, we earn from qualifying purchases. 
                Reports are funded by Nord Security and Honeygain passive income partnerships.
            </p>
        </div>
    </body>
    </html>
    """
    with open(os.path.join(path, filename), "w") as f:
        f.write(html)

def update_sitemap():
    today = datetime.date.today().strftime("%Y-%m-%d")
    entries = [f"<url><loc>{BASE_URL}/</loc><priority>1.0</priority></url>"]
    if os.path.exists("affiliates"):
        for root, _, files in os.walk("affiliates"):
            for file in files:
                if file.endswith(".html"):
                    p = os.path.relpath(os.path.join(root, file), os.getcwd()).replace(os.sep, '/')
                    entries.append(f"<url><loc>{BASE_URL}/{p}</loc><lastmod>{today}</lastmod></url>")
    with open("sitemap.xml", "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{"".join(entries)}</urlset>')

if __name__ == "__main__":
    all_portals = [
        ("cyber-intel", ["Zero Trust Architecture", "Endpoint Detection Response", "Network Traffic Analysis", "SIEM Log Management", "Encrypted Data Vault", "Hardware Security Module", "Biometric Access Control", "DDoS Mitigation", "Incident Response", "Quantum Encryption"]),
        ("robotics", ["Collaborative Robots", "Six Axis Robotic Arm", "Machine Vision System", "Delta Robot Assembly", "Hydraulic Actuators", "Pneumatic Logic", "PLC Programming", "SCADA Audit", "HMI Interface", "Industrial Sensors"]),
        ("solar-industrial", ["Three Phase Inverter", "MPPT Controller", "Bifacial Solar Panel", "Solar Tracker", "PV Combiner Box", "Battery Energy Storage", "Hybrid Power Plant", "Microgrid Control", "Grid Tie Protection", "Solar Maintenance"]),
        ("power-systems", ["Uninterruptible Power Supply", "Generator Sync", "Power Factor Correction", "Voltage Stabilizers", "Circuit Breakers", "Transformer Oil Analysis", "Busbar Trunking", "Energy Management", "Harmonic Filters", "Switchgear"]),
        ("green-hydrogen", ["Hydrogen Electrolyzer", "Fuel Cell Stack", "Hydrogen Storage", "Ammonia Synthesis", "Carbon Capture", "Electrolysis Membrane", "Ammonia Production", "Refuelling Stations", "Thermal Storage", "Biofuel Processing"]),
        ("additive-mfg", ["Industrial 3D Printer", "Sintering Furnace", "Laser Powder Bed Fusion", "CNC Machining", "Injection Molding", "Die Casting", "Surface Grinding", "Electro Discharge Machining", "Waterjet Cutting", "Plasma Cutter"]),
        ("precision-eng", ["CMM Inspection", "Digital Micrometers", "Laser Alignment", "Non Destructive Testing", "Metrology Lab", "Optical Comparator", "Borescope Inspection", "Hardness Tester", "Surface Profile Meter", "Profile Projector"]),
        ("smart-building", ["BMS Control", "HVAC Variable Speed Drive", "Smart Lighting", "Elevator Logic", "Water Treatment Automation", "Waste Management IoT", "Smart Parking Sensors", "EV Chargers", "Occupancy Sensors", "Energy Audit"]),
        ("agri-tech", ["Precision Irrigation", "Hydroponic Control", "Automated Greenhouse", "Livestock Tracking", "Soil Moisture Probe", "Satellite Crop Monitoring", "Drone Fertilizer Spreader", "Autonomous Tractor", "Grain Silo Sensors", "Dairy Automation"]),
        ("mining-tech", ["Underground Mining Drone", "Ore Crushing Automation", "Conveyor Monitor", "Blast Hole Drill", "Tailings Dam Sensor", "Autonomous Haul Truck", "Seismic Monitoring", "Mineral Processing", "Ventilation Control", "Rock Bolt Inspection"]),
        ("industrial-repair", [f"Repairing {k}" for k in ["PLC Modules", "VFD Drives", "Servo Motors", "CNC Spindles", "Hydraulic Pumps", "Solar Inverters", "Medical Imaging", "Lab Centrifuges", "Industrial Chillers", "Boiler Controls"]]),
        ("maintenance-guides", [f"{k} Maintenance" for k in ["Preventative", "Predictive", "Condition Based", "Reliability Centered", "Lifecycle", "Remote", "Augmented Reality", "AI Driven", "Scheduled", "Emergency"]]),
        ("procurement-2026", [f"Buying {k} in 2026" for k in ["Industrial Sensors", "Networking Gear", "Security Cameras", "Solar Batteries", "Encrypted Drives", "Laboratory Gear", "Robotic Parts", "Power Tools", "Server Hardware", "Measuring Tools"]])
    ]
    
    # Flat list generation
    flat_list = []
    for folder, k_list in all_portals:
        for k in k_list:
            flat_list.append((folder, k))

    # Slice handles the strike
    batch = flat_list[BATCH_START : BATCH_START + BATCH_SIZE]
    print(f"🚀 Processing Batch from {BATCH_START}. Found {len(batch)} keywords.")
    
    for f, k in batch:
        build_page(f, k)
    
    update_sitemap()
    print("🏁 Strike Complete. Sitemap Updated.")
