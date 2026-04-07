import os
from datetime import datetime

def generate_sitemap():
    base_url = "https://fairdiscovery.org"
    intel_dir = "docs/intel"
    sitemap_path = "docs/sitemap_intel.xml"
    
    # Start the XML structure
    pages = [f"{base_url}/sentinel-scrub.html", f"{base_url}/pixel-purge.html"]
    
    # Scan the intel folder for new forensic reports
    if os.path.exists(intel_dir):
        for file in os.listdir(intel_dir):
            if file.endswith(".html"):
                pages.append(f"{base_url}/intel/{file}")

    # Build the XML string
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml += f'  <url>\n    <loc>{page}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n  </url>\n'
    xml += '</urlset>'

    with open(sitemap_path, 'w') as f:
        f.write(xml)
    print(f"Sitemap Sync: {len(pages)} pages indexed.")

if __name__ == "__main__":
    generate_sitemap()
