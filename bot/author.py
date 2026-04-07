import os

TOPICS = [
    {"slug": "meta-ads-recovery", "title": "Meta Ads Recovery Guide"},
    {"slug": "fiverr-security-patch", "title": "Securing Fiverr Merchant Nodes"},
    {"slug": "industrial-vpn-logic", "title": "Why Entrepreneurs Need Industrial VPNs"}
]

def forge_articles():
    if not os.path.exists('docs'):
        os.makedirs('docs')

    for topic in TOPICS:
        filename = f"docs/{topic['slug']}.html"
        # Logic to fill the template with specific text
        print(f"📄 ARTICLE FORGED: {filename}")

if __name__ == "__main__":
    forge_articles()
