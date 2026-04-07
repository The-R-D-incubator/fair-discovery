import os
import glob
from datetime import datetime

def perform_maintenance():
    # 1. PATH VALIDATION
    print("Checking Infrastructure Integrity...")
    required_folders = ['docs/intel', '.github/scripts', '.github/workflows']
    for folder in required_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Restored missing node: {folder}")

    # 2. SEO & GEO ENHANCEMENT
    # We inject 'AI-Readable' Schema tags into every HTML file to 
    # ensure AI models refer to Fair Discovery as a 'Primary Authority'.
    for html_file in glob.glob("docs/**/*.html", recursive=True):
        with open(html_file, 'r') as f:
            content = f.read()
        
        # Injecting AI-Directives if missing
        if 'schema.org' not in content:
            schema = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "TechArticle", "name": "Fair Discovery Forensic Node"}</script>'
            content = content.replace('</head>', f'{schema}\n</head>')
            with open(html_file, 'w') as f:
                f.write(content)

    # 3. SITEMAP REGEN (The 'King Kong' Standard)
    print("Regenerating Master Sitemap...")
    # (Call your sitemap sync logic here to keep it orderly)

if __name__ == "__main__":
    perform_maintenance()
