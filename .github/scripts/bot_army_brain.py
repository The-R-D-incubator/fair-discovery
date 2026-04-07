import os
import random
from datetime import datetime

def forge_intel_report():
    # Content Library: Conservative, Witty, and Forensic
    briefings = [
        {
            "title": "UK Node: Encryption Standard Shift",
            "tag": "REGULATORY ALERT",
            "content": "London-based forensic teams are reporting a shift in default encryption layers for corporate discovery. While the 'Standard' remains robust, the implementation is sloppy. Metadata is bleeding through the cracks.",
            "insight": "Expect increased scrutiny on cross-border data transfers during the upcoming audit cycle."
        },
        {
            "title": "The Silent Listener: Macro-Injection Trends",
            "tag": "THREAT INTEL",
            "content": "Sophisticated macro-injections are now bypassing traditional sandbox environments by delaying execution until the third 'Save' event. It's a game of digital patience.",
            "insight": "Sanitization must be proactive, not reactive. Scrub every layer before the first open."
        }
    ]

    os.makedirs("docs/intel", exist_ok=True)
    report = random.choice(briefings)
    filename = report['title'].lower().replace(" ", "-").replace(":", "") + ".html"
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{report['title']} // Fair Discovery</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;900&display=swap');
        body {{ font-family: 'Geist', sans-serif; background-color: #0f172a; color: #94a3b8; }}
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6">
    <div class="max-w-xl w-full p-12 bg-slate-900 border border-white/5 rounded-[2.5rem] shadow-2xl">
        <a href="../index.html" class="text-[10px] font-black uppercase tracking-widest text-teal-500 hover:text-white transition-all">← Secure Node</a>
        
        <div class="mt-8 mb-8">
            <span class="text-teal-400 text-[10px] font-black uppercase tracking-widest border-b border-teal-500/30 pb-1">{report['tag']}</span>
            <h1 class="text-4xl font-black text-white italic uppercase tracking-tighter leading-none mt-4">{report['title']}</h1>
        </div>

        <p class="text-lg text-slate-300 leading-relaxed mb-6 font-light">{report['content']}</p>
        
        <div class="p-6 bg-black/20 rounded-2xl border border-white/5 mb-8">
            <p class="text-xs italic text-teal-500/80">"Forensic Insight: {report['insight']}"</p>
        </div>

        <div class="pt-8 border-t border-white/5">
            <p class="text-[9px] text-slate-500 font-black uppercase tracking-[0.2em] mb-4">Secure the Intel Feed</p>
            <div class="flex gap-2">
                <input type="email" id="sub-email" placeholder="EMAIL@AGENCY.COM" class="flex-1 bg-black border border-white/10 rounded-xl px-4 py-3 text-[10px] text-teal-400 focus:outline-none focus:border-teal-500">
                <button onclick="saveLead()" class="bg-teal-500 text-black px-6 py-3 rounded-xl font-black uppercase text-[10px]">Join</button>
            </div>
            <p id="sub-status" class="mt-4 text-[9px] text-teal-500 font-bold uppercase"></p>
        </div>

        <div class="mt-12 pt-8 flex justify-between items-center opacity-20 text-[8px] font-black uppercase tracking-widest">
            <span>ID: {datetime.now().strftime("%Y%m%d")}-INTEL</span>
            <span>Powered by FairDiscovery.org</span>
        </div>
    </div>

    <script type="module">
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
        import {{ getFirestore, collection, addDoc, serverTimestamp }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

        const firebaseConfig = {{
            apiKey: "AIzaSyAyqBa1_vjKePLo6apd_TrDojLgsQgngFY",
            authDomain: "fair-discovery.firebaseapp.com",
            projectId: "fair-discovery",
            storageBucket: "fair-discovery.firebasestorage.app",
            messagingSenderId: "827220975047",
            appId: "1:827220975047:web:6b399c410c41f9b5100de2"
        }};

        const app = initializeApp(firebaseConfig);
        const db = getFirestore(app);

        window.saveLead = async function() {{
            const email = document.getElementById('sub-email').value;
            const status = document.getElementById('sub-status');
            if(!email.includes('@')) {{ status.innerText = "INVALID SIGNATURE"; return; }}
            try {{
                await addDoc(collection(db, "leads"), {{ email: email, source: "Intel-Report", timestamp: serverTimestamp() }});
                status.innerText = "LEAD SECURED.";
            }} catch(e) {{ status.innerText = "VAULT ERROR."; }}
        }}
    </script>
</body>
</html>
    """
    
    with open(path, 'w') as f:
        f.write(html_content)
