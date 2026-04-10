# --- YOUR REVENUE KEYS ---
AMAZON_TAG = "fairdiscovery-20" 
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"

def generate_pro_ui(k, title):
    return f"""
    <div style="background:#fff9e6; padding:10px; border-bottom:2px solid #f1c40f; text-align:center; font-size:14px;">
        🚀 <strong>Exclusive:</strong> Get a $5 starting bonus to offset your {k} costs. <a href="{HONEYGAIN_URL}">Claim Bonus →</a>
    </div>

    <div style="max-width:800px; margin:auto; padding:40px; font-family: 'Helvetica Neue', Arial, sans-serif; color: #333;">
        <header style="border-bottom: 3px solid #00d18a; padding-bottom:10px; margin-bottom:30px;">
            <span style="color:#00d18a; font-weight:bold; text-transform:uppercase; letter-spacing:1px;">Expert Analysis 2026</span>
            <h1 style="font-size:36px; margin-top:10px;">The Ultimate Guide to {k}</h1>
        </header>

        <section style="line-height:1.8; font-size:18px;">
            <p>Our technical team at <strong>Fair Discovery</strong> has analyzed the latest {k} hardware to ensure compatibility, security, and performance. In a market flooded with generic options, these are the professional-grade solutions that actually deliver results.</p>
        </section>

        <div style="background:#0055ff; color:white; padding:30px; border-radius:15px; margin:40px 0; display:flex; align-items:center; gap:20px;">
            <div style="flex:1;">
                <h3 style="margin-top:0;">🛡️ Secure Your {k} Connection</h3>
                <p>Don't leave your hardware exposed. Surfshark provides 256-bit encryption for all your workshop and home devices.</p>
                <a href="{SURFSHARK_URL}" style="background:white; color:#0055ff; padding:12px 25px; border-radius:5px; text-decoration:none; font-weight:bold; display:inline-block;">Get 82% Off + 3 Months Free</a>
            </div>
            <img src="https://surfshark.com/wp-content/uploads/2021/08/surfshark-logo-white.png" width="120" style="opacity:0.9;">
        </div>

        <h2 style="border-left:5px solid #00d18a; padding-left:15px;">Hardware Recommendations</h2>
        <div style="margin:20px 0;">
            [AD_WIDGET_HERE]
        </div>

        <footer style="margin-top:60px; padding-top:20px; border-top:1px solid #eee; font-size:12px; color:#999;">
            Disclaimer: Fair Discovery provides independent reviews. We may earn a commission from partners listed on this page to support our research lab.
        </footer>
    </div>
    """
