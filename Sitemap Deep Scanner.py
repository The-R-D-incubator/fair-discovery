import os
from datetime import datetime

# SETTINGS
domain = "https://fairdiscovery.org"
affiliates_dir = "affiliates"
sitemap_filename = "sitemap.xml"
today = datetime.now().strftime('%Y-%m-%d')

urls = []

# 1. ADD THE ROOT DOMAIN
urls.append(f"  <url><loc>{domain}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>")

# 2. SCAN THE AFFILIATES FOLDER RECURSIVELY
if os.path.exists(affiliates_dir):
    for root, dirs, files in os.walk(affiliates_dir):
        # Format the folder path for the URL
        relative_path = os.path.relpath(root, ".").replace("\\", "/")
        
        # If the folder has an index.html, add the folder URL
        if "index.html" in files:
            folder_url = f"{domain}/{relative_path}/"
            urls.append(f"  <url><loc>{folder_url}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")
        
        # Add every other .html file found in the folder
        for file in files:
            if file.endswith(".html") and file != "index.html":
                file_url = f"{domain}/{relative_path}/{file}"
                urls.append(f"  <url><loc>{file_url}</loc><lastmod>{today}</lastmod><priority>0.7</priority></url>")

# 3. CONSTRUCT THE XML
sitemap_content = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    *urls,
    '</urlset>'
]

# 4. WRITE THE FILE
with open(sitemap_filename, "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))

print(f"✅ Deep Scan Complete: {len(urls)} URLs mapped to {sitemap_filename}")
