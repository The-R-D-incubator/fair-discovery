import os

# --- YOUR REVENUE KEYS ---
AMAZON_TAG = "fairdiscovery-20" 
SURFSHARK_URL = "https://get.surfshark.net/aff_c?offer_id=6&aff_id=4160"

def build_niche_site(folder_name, title, keywords):
    """Generates a mini-site inside a subfolder"""
    base_path = f"affiliates/{folder_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # Create the landing page for this niche
    with open(f"{base_path}/index.html", "w") as f:
        f.write(f"""
        <html>
        <head><title>{title}</title></head>
        <body style="font-family:sans-serif; padding:40px; line-height:1.6;">
            <h1>{title}</h1>
            <p>Expert guides and hardware reviews for 2026.</p>
            <hr>
            <ul>
        """)
        
        # Generate 1 page for every keyword
        for k in keywords:
            filename = k.lower().replace(" ", "-") + ".html"
            f.write(f'<li><a href="{filename}">{k}</a></li>')
            
            # Create the actual article page
            with open(f"{base_path}/{filename}", "w") as art:
                art.write(f"""
                <html><body>
                    <h1>The Best {k} in 2026</h1>
                    <p>When looking for {k}, security and reliability are key.</p>
                    <p><a href="{SURFSHARK_URL}">Secure your connection with Surfshark VPN</a></p>
                    <p><a href="https://www.amazon.com/s?k={k.replace(' ','+')}&tag={AMAZON_TAG}">View top rated {k} on Amazon</a></p>
                    <hr>
                    <a href="index.html">Back to {title} Hub</a>
                </body></html>
                """)
        
        f.write("</ul></body></html>")
    print(f"✅ Created {title} at /affiliates/{folder_name}")

if __name__ == "__main__":
    # Let's test two "Verticals"
    build_niche_site("privacy-hub", "Global Privacy Portal", ["VPN for PC", "Secure Routers", "Encrypted Email"])
    build_niche_site("workshop-gear", "Elite Diagnostic Tools", ["OBD2 Scanner", "Digital Multimeter", "Thermal Camera"])
