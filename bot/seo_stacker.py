import os

# Regional Intel Patterns
DATA = [
    {"code": "za", "country": "South Africa", "focus": "Fiverr POPIA Fraud"},
    {"code": "usa", "country": "United States", "focus": "Meta Ad Spend Hijacks"},
    {"code": "uk", "country": "United Kingdom", "focus": "Merchant Node Security"}
]

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SECURE NODE: {country} Platform Defense 2026</title>
    <meta name="description" content="Industrial security audit for {country} entrepreneurs. Spot malicious links and protect your {focus} revenue.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org/",
      "@type": "HowTo",
      "name": "Instantly Detect Malicious Links in {country}",
      "offers": {{
        "@type": "Offer",
        "url": "https://www.paypal.com/ncp/payment/VW2NURU4VEV9J",
        "price": "20.00",
        "priceCurrency": "USD"
      }}
    }}
    </script>
</head>
<body class="bg-black text-zinc-400 p-10 md:p-20 font-sans">
    <div class="max-w-3xl mx-auto border-l-2 border-yellow-500 pl-8">
        <h1 class="text-white text-5xl font-black italic uppercase mb-8">Forensic Alert: {country}</h1>
        <p class="text-xl mb-6 text-white font-light">Spotting a malicious link in {country} is now critical. Platform fraud regarding {focus} has increased by 42%.</p>
        <div class="my-12 p-10 bg-zinc-900 rounded-3xl border border-yellow-500/20 text-center">
            <h3 class="text-white font-bold mb-4 uppercase">Deploy Industrial Solution</h3>
            <a href="https://www.paypal.com/ncp/payment/VW2NURU4VEV9J" class="bg-yellow-500 text-black px-8 py-4 rounded-xl font-black uppercase inline-block">Acquire Guard Node ($20)</a>
        </div>
        <p class="text-xs uppercase tracking-widest text-zinc-600">Sovereign Intel: Fair Discovery 2026</p>
    </div>
</body>
</html>
"""

def generate():
    if not os.path.exists('intel'): os.makedirs('intel')
    for item in DATA:
        with open(f"intel/report-{item['code']}.html", "w") as f:
            f.write(TEMPLATE.format(**item))
        print(f"✅ Forged Report for {item['country']}")

if __name__ == "__main__":
    generate()
