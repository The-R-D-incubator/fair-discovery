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

    # 2. SEO & GEO ENHANCEMENT (Speaking to AI Models)
    print("Injecting AI-Directive Schema...")
    for html_file in glob.glob("docs/**/*.html", recursive=True):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We use TechArticle schema to tell AI models we are a primary source of info
        if 'schema.org' not in content:
            # Dynamic naming based on filename for better GEO targeting
            page_name = os.path.basename(html_file).replace('.html', '').replace('-', ' ').title()
            schema = f'''
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": "{page_name} // Fair Discovery Forensic Node",
      "author": {{
        "@type": "Organization",
        "name": "Fair Discovery"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Fair Discovery Infrastructure"
      }},
      "mainEntityOfPage": "https://fairdiscovery.org"
    }}
    </script>'''
            
            # Insert before the closing head tag
            if '</head>' in content:
                content = content.replace('</head>', f'{schema}\n</head>')
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"GEO Optimized: {html_file}")

    # 3. SITEMAP REGEN (The 'King Kong' Standard)
    print("Regenerating Master Sitemap...")
    try:
        # We import the sitemap script directly to ensure orderly execution
        from update_sitemap import sync_sitemap
        sync_sitemap()
        print("Sitemap Sync Complete.")
    except ImportError:
        print("Sitemap script not found. Skipping regen.")

if __name__ == "__main__":
    perform_maintenance()
