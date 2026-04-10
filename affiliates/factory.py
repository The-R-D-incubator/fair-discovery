# --- YOUR REVENUE KEYS ---
AMAZON_TAG = "fairdiscovery-20" 
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"
HONEYGAIN_URL = "https://join.honeygain.com/PRINY5083C"

def generate_pro_ui(k, title, assets_path="assets/"):
    # Using one of your uploaded Surfshark assets
    surfshark_banner = f"{assets_path}Surfshark-Preview-01.png"
    
    return f"""
    <div style="background:#fff9e6; padding:12px; border-bottom:2px solid #f1c40f; text-align:center; font-size:14px; font-weight:bold;">
        🚀 <strong>Fair Discovery Bonus:</strong> Get a $5 starting bonus to offset your {k} costs. <a href="{HONEYGAIN_URL}" style="color:#d35400;">Claim Bonus Here →</a>
    </div>

    <div style="max-width:850px; margin:auto; padding:40px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; color: #1a1a1a; line-height:1.7;">
        <header style="border-bottom: 4px solid #00d18a; padding-bottom:15px; margin-bottom:40px;">
            <span style="color:#666; font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:2px;">Laboratory Tested • April 2026</span>
            <h1 style="font-size:42px; margin-top:10px; letter-spacing:-1px;">The Professional Guide to {k}</h1>
            <p style="font-size:20px; color:#555;">vetted hardware solutions for the modern {title} environment.</p>
        </header>

        <section style="margin-bottom:40px;">
            <p>At <strong>Fair Discovery</strong>, we bridge the gap between complex hardware and end-user reliability. Our engineers have benchmarked {k} solutions to provide a definitive list of equipment that meets the high-bandwidth and security demands of 2026.</p>
        </section>

        <div style="background:#0055ff; color:white; padding:35px; border-radius:18px; margin:50px 0; display:flex; align-items:center; gap:30px; box-shadow: 0 10px 30px rgba(0,85,255,0.2);">
            <div style="flex:1;">
                <h3 style="margin-top:0; font-size:24px;">🛡️ Secure Your {k} Stack</h3>
                <p style="font-size:16px; opacity:0.9;">Hardware is only as secure as the network it's on. Encrypt your entire {title} setup with Surfshark's 2026 Security Suite.</p>
                <a href="{SURFSHARK_URL}" style="background:white; color:#0055ff; padding:14px 30px; border-radius:8px; text-decoration:none; font-weight:800; display:inline-block; transition:0.3s;">GET 82% OFF + 3 MONTHS FREE</a>
            </div>
            <img src="{surfshark_banner}" width="180" style="border-radius:10px; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));">
        </div>

        <h2 style="font-size:28px; border-left:6px solid #00d18a; padding-left:20px; margin-bottom:25px;">Verified Hardware Inventory</h2>
        <div style="margin-bottom:50px;">
            [AD_WIDGET_HERE]
        </div>

        <div style="background:#f9f9f9; padding:30px; border-radius:15px; border:1px solid #eee;">
            <h3 style="margin-top:0;">Expert Troubleshooting for {k}</h3>
            <p><strong>Q: How do I ensure maximum data throughput?</strong><br>
            A: Always check your cable category (Cat6e or higher) when connecting high-end {k} components to ensure no local bottlenecks.</p>
        </div>

        <footer style="margin-top:80px; padding-top:20px; border-top:1px solid #eee; font-size:13px; color:#888; text-align:center;">
            &copy; 2026 Fair Discovery Network. Transparency Disclosure: We are a professional review site that receives compensation from the companies whose products we review.
        </footer>
    </div>
    """
