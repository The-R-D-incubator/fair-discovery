import os
import random
from datetime import datetime

def forge_intel_report():
    # THE INTELLIGENCE LIBRARY
    briefings = [
        {
            "title": "The Death of the Black Box",
            "tag": "FORENSIC MANIFESTO",
            "headline": "Why Modern Software is a Security Liability",
            "content": "We’ve entered a strange era of digital tools. Most modern software is a mystery — hidden behind monthly subscriptions, locked in proprietary clouds, and bloated with features you never asked for. <br><br> For security professionals, private investigators, and creators, this “Black Box” model isn’t just annoying; it’s a liability. When you are auditing a content gate or tracing a digital footprint, you don’t need a “platform.” <strong>You need a Node.</strong> <br><br> The internet is no longer a playground; it’s industrial infrastructure. It’s time our tools reflected that.",
            "insight": "Privacy isn't a feature you subscribe to. It's an infrastructure you own."
        },
        {
            "title": "Linux vs. Windows: The Kernel of Truth",
            "tag": "SYSTEM SOVEREIGNTY",
            "headline": "Reclaiming Your CPU Cycles from Telemetry",
            "content": "Windows isn't an OS; it's a telemetry suite that happens to run apps. Every click, file-open, and search query is indexed and sent to a centralized node. <br><br> Switching to a hardened Linux kernel isn't about being a 'hacker'—it's about owning your own hardware. In a Linux environment, the user is the ultimate authority, not a corporate data-harvesting engine.",
            "insight": "Start with a bootable Mint drive. Experience what it feels like to not be 'indexed' by your own hardware."
        },
        {
            "title": "Signal vs. WhatsApp: The Metadata War",
            "tag": "SECURE COMMS",
            "headline": "The Hidden Cost of 'Free' Encrypted Messaging",
            "content": "WhatsApp encrypts the message, but Meta owns the metadata. They know who you talked to, when, for how long, and your physical location during the handshake. <br><br> Signal is the only consumer-grade node that treats metadata as toxic waste—it simply doesn't store it. If a platform knows your contact list, you are the product.",
            "insight": "Signal's sealed-sender protocol is the only industry benchmark that matters in 2026."
        }
    ]

    os.makedirs("docs/intel", exist_ok=True)
    report = random.choice(briefings)
    
    # Clean filename logic
    filename = report['title'].lower().replace(" ", "-").replace(":", "").replace("/", "-") + ".html"
    path = f"docs/intel/{filename}"
    
    # THE SECURE TEMPLATE (No 'f' prefix here to prevent bracket crashes)
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} // Fair Discovery Intel</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;600;900&display=swap');
        body {{ font-family: 'Geist', sans-serif; background-color: #020617; color: #94a3b8; line-height: 1.6; }}
        .glow-border {{ border: 1px solid rgba(45, 212, 191, 0.1); }}
        .gradient-text {{ background: linear-gradient(135deg, #fff 0%, #2dd4bf 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
    </style>
</head>
<body class="min-h-screen py-12 px-6 md:py-24">
    <div class="max-w-3xl mx-auto">
        <nav class="flex justify-between items-center mb-20">
            <a href="../index.html" class="text-[10px] font-black uppercase tracking-[0.4em] text-teal-500 hover:text-white transition-all">← Infrastructure Home</a>
            <span class="text-slate-700 text-[10px] font-black uppercase tracking-widest italic tracking-[0.2em]">Node-2026-A1</span>
        </nav>

        <header class="mb-16">
            <span class="px-3 py-1 bg-teal-500/10 text-teal-400 text-[9px] font-black rounded-full border border-teal-500/20 uppercase tracking-[0.2em] mb-6 inline-block">{tag}</span>
            <h1 class="text-5xl md:text-7xl font-black italic uppercase tracking-tighter leading-[0.9] mt-4 mb-8 gradient-text">
                {title}
            </h1>
        </header>

        <article class="text-lg text-slate-300 font-light">
            <h2 class="text-white font-bold text-2xl mb-6 italic uppercase tracking-tight">{headline}</h2>
            <p>{content}</p>

            <div class="glow-border bg-slate-900/40 p-8 rounded-[2rem] my-12 italic border-l-4 border-l-teal-500">
                <p class="text-slate-400 text-md mb-0 italic">"Forensic Insight: {insight}"</p>
            </div>
            
            <h2 class="text-white font-bold text-2xl mb-8 italic uppercase tracking-tight">Deployment Access</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                <a href="../sentinel-scrub.html" class="block p-6 rounded-2xl border border-white/5 bg-white/5 hover:border-teal-500/50 transition-all">
                    <h4 class="text-teal-400 font-black uppercase text-xs tracking-widest mb-2">Sentinel-Scrub</h4>
                    <p class="text-[11px] text-slate-500 uppercase">Document Sanitization Node.</p>
                </a>
                <a href="../pixel-purge.html" class="block p-6 rounded-2xl border border-white/5 bg-white/5 hover:border-teal-500/50 transition-all">
                    <h4 class="text-teal-400 font-black uppercase text-xs tracking-widest mb-2">Pixel-Purge</h4>
                    <p class="text-[11px] text-slate-500 uppercase">Image Privacy Node.</p>
                </a>
            </div>
        </article>

        <div class="mt-20 p-12 bg-white rounded-[3.5rem] text-center">
            <h4 class="text-slate-900 font-black uppercase italic mb-2 tracking-tighter text-2xl">Secure the Feed</h4>
            <p class="text-slate-500 text-[10px] mb-8 uppercase tracking-[0.2em] font-bold">Initialize Cloud Token // Get 20 Credits</p>
            <div class="flex flex-col sm:flex-row gap-3">
                <input type="email" id="sub-email" placeholder="EMAIL@AGENCY.COM" class="flex-1 bg-slate-100 border-none rounded-2xl px-8 py-5 text-[11px] text-slate-900 focus:ring-2 focus:ring-teal-500 font-black outline-none uppercase tracking-widest">
                <button onclick="saveLead()" class="bg-teal-500 text-white px-12 py-5 rounded-2xl font-black uppercase text-[11px] tracking-widest">Initialize</button>
            </div>
            <p id="sub-status" class="mt-6 text-[9px] text-teal-600 font-black uppercase"></p>
        </div>

        <footer class="mt-24 pt-8 border-t border-white/5 flex justify-between items-center opacity-30 text-[8px] font-black uppercase tracking-[0.4em]">
            <span>FairDiscovery.org // Sovereign Utility</span>
            <span>2026 // ALPHA UNIT</span>
        </footer>
    </div>

    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
        import { getFirestore, doc, getDoc, setDoc, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

        const firebaseConfig = {
            apiKey: "AIzaSyAyqBa1_vjKePLo6apd_TrDojLgsQgngFY",
            authDomain: "fair-discovery.firebaseapp.com",
            projectId: "fair-discovery",
            storageBucket: "fair-discovery.firebasestorage.app",
            messagingSenderId: "827220975047",
            appId: "1:827220975047:web:6b399c410c41f9b5100de2"
        };

        const app = initializeApp(firebaseConfig);
        const db = getFirestore(app);

        window.saveLead = async function() {
            const emailInput = document.getElementById('sub-email');
            const status = document.getElementById('sub-status');
            const email = emailInput.value.toLowerCase().trim();
            if (!email.includes('@')) { status.innerText = "INVALID SECURE SIGNATURE"; return; }
            status.innerText = "SYNCING CLOUD TOKEN...";
            try {
                const userRef = doc(db, "users", email);
                const userSnap = await getDoc(userRef);
                if (userSnap.exists()) {
                    status.innerText = "NODE RECONNECTED. BALANCE RESTORED.";
                } else {
                    await setDoc(userRef, { email: email, credits: 20, joined: serverTimestamp() });
                    await addDoc(collection(db, "leads"), { email: email, source: "Master-Bot" });
                    status.innerText = "TOKEN AUTHORIZED: 20 CREDITS GRANTED.";
                }
                emailInput.value = "";
            } catch (e) { status.innerText = "VAULT OFFLINE."; }
        }
    </script>
</body>
</html>
"""
    
    # SAFER INJECTION: Injecting the report data into the template
    final_html = html_template.replace("{title}", report['title'])\
                              .replace("{tag}", report['tag'])\
                              .replace("{headline}", report['headline'])\
                              .replace("{content}", report['content'])\
                              .replace("{insight}", report['insight'])

    with open(path, 'w') as f:
        f.write(final_html)

if __name__ == "__main__":
    forge_intel_report()
