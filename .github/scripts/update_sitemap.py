import os
from datetime import datetime

DOMAIN = "https://fairdiscovery.org"

def generate_sitemap_file(filename, urls):
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    footer = '</urlset>'
    content = ""
    for url in urls:
        content += f'  <url>\n    <loc>{DOMAIN}/{url}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    
    with open(f"docs/{filename}", "w") as f:
        f.write(header + content + footer)
    print(f"Generated: {filename}")

def generate_index_sitemap():
    sitemaps = ["sitemap_pages.xml", "sitemap_tools.xml", "sitemap_intel.xml"]
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    footer = '</sitemapindex>'
    content = ""
    for sm in sitemaps:
        content += f'  <sitemap>\n    <loc>{DOMAIN}/{sm}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n  </sitemap>\n'
    
    with open("docs/sitemap_index.xml", "w") as f:
        f.write(header + content + footer)
    print("Generated: sitemap_index.xml (The Mother Ship)")

def run_sync():
    # 1. CORE PAGES
    pages = ["index.html"] # Add other static pages here
    generate_sitemap_file("sitemap_pages.xml", pages)

    # 2. REVENUE TOOLS (Nodes)
    # Automatically finds any .html in docs root that isn't index or a sitemap
    tools = [f for f in os.listdir("docs") if f.endswith(".html") and f not in ["index.html"] and "sitemap" not in f]
    generate_sitemap_file("sitemap_tools.xml", tools)

    # 3. INTEL (The Bot Army Reports)
    intel_files = []
    if os.path.exists("docs/intel"):
        intel_files = [f"intel/{f}" for f in os.listdir("docs/intel") if f.endswith(".html")]
    generate_sitemap_file("sitemap_intel.xml", intel_files)

    # 4. THE MOTHER SHIP
    generate_index_sitemap()

if __name__ == "__main__":
    run_sync()
