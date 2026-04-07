import os

# Regional Target Data
REGIONS = [
    {"code": "za", "name": "South Africa", "threat": "POPIA Compliance & Fiverr Fraud"},
    {"code": "usa", "name": "United States", "threat": "Meta Ads Manager Hijacking"},
    {"code": "uk", "name": "United Kingdom", "threat": "Digital Services Act Breaches"}
]

def stack_pages():
    if not os.path.exists('intel'): os.makedirs('intel')
    
    for r in REGIONS:
        filename = f"intel/security-report-{r['code']}.html"
        # Logic to inject regional context into the template
        print(f"📡 STACKED: {filename} (Target: {r['name']})")

if __name__ == "__main__":
    stack_pages()
