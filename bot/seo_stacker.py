import os

DATA = [
    {"code": "za", "country": "South Africa", "focus": "Fiverr POPIA Fraud", "stat": "38%"},
    {"code": "usa", "country": "United States", "focus": "Meta Ad Manager Hijacks", "stat": "51%"},
    {"code": "uk", "country": "United Kingdom", "focus": "Merchant Node Security", "stat": "29%"}
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
      "description": "Step-by-step industrial guide to identifying hijacked session tokens.",
      "offers": {{
        "@type": "Offer",
        "url": "https://www.paypal.com/ncp/payment/VW2NURU4VEV9J",
        "price": "20.00",
        "priceCurrency": "USD"
      }}
    }}
    </script>
</head>
<body class="bg-black text-zinc-400 p-10 md:p-20 font-sans leading-relaxed">
    <div class="max-w-3xl mx-auto border-l-2 border-yellow-500 pl-8">
        <nav class="mb-12 text-[10px] uppercase tracking-widest font-bold">
            <a href="../index.html" class="text-yellow-500">← Return to Repository</a>
        </nav>
        <h1 class="text-white text-5xl font-black italic uppercase mb-8 leading-none">The {country} <span class="text-yellow-500">Security Audit</span></h1>
        <p class="text-xl mb-6 text-white font-light italic">Did you know that you can spot a malicious link right away? In {country}, platform fraud regarding {focus} has increased by {stat}.</p>
        
        <div class="space-y-6 text-sm">
            <p>To effectively protect your revenue stream, you must understand the forensic footprint of a session hijack. Manual detection is failing; entrepreneurs are losing access to their primary merchant nodes daily.</p>
        </div>

        <div class="my-16 p-12 bg-zinc-950 rounded-[3rem] border border-yellow-500/30 text-center shadow-[0_0_50px_rgba(250,204,21,0.1)]">
            <h3 class="text-white text-2xl font-black mb-4 uppercase italic">Deploy Guard Node v7.1</h3>
            <p class="text-zinc-500 mb-8 text-sm px-4">Instant digital isolation for {focus}. Stop the hijack before it starts.</p>
            <a href="https://www.paypal.com/ncp/payment/VW2NURU4VEV9J" class="bg-yellow-500 text-black px-12 py-5 rounded-2xl font-black uppercase text-xs inline-block hover:scale-105 transition-transform">Acquire Node ($20)</a>
        </div>
        
        <footer class="mt-20 opacity-30 text-[9px] uppercase tracking-[0.5em]">Fair Discovery Sovereign Infrastructure &copy; 2026</footer>
    </div>
</body>
</html>
"""

def generate():
    if not os.path.exists('intel'): os.makedirs('intel')
    for item in DATA:
        filename = f"intel/report-{item['code']}.html"
        with open(filename, "w", encoding='utf-8') as f:
            f.write(TEMPLATE.format(**item))
        print(f"✅ FORGED: {filename}")

if __name__ == "__main__":
    generate()
