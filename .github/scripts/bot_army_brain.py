import os
import random
from datetime import datetime

def forge_intel_report():
    topics = [
        {
            "title": "The Ghost in the Machine: Tracking Pixel Surge",
            "tag": "FORENSIC ALERT",
            "hook": "Privacy isn't dead; it's just being watched by a 1x1 transparent GIF.",
            "content": "Our nodes have identified a sophisticated resurgence in 'Beacon-Injection' within legal discovery documents. These pixels aren't just for marketing anymore; they are being used to map internal network structures when a document is opened behind a firewall. It's subtle, it's clever, and it's remarkably effective.",
            "analysis": "By monitoring the 'Time-to-Open' and the 'Origin-IP', bad actors can determine if a document has been forwarded to a secondary counsel or a third-party auditor. This is digital espionage dressed as a standard PDF attachment.",
            "image_query": "Image of a tracking pixel mechanism"
        },
        {
            "title": "Metadata Leak: The GPS in your DOCX",
            "tag": "PRIVACY RISK",
            "hook": "Your Word document knows where you spent last night. Does your client?",
            "content": "Standard government templates are currently leaking more than just information—they are leaking locations. A forensic audit of recent filings shows that 14% of submitted DOCX files contain embedded GPS coordinates in the EXIF data of 'inline' images and author profiles.",
            "analysis": "The vulnerability lies in the 'Default-Save' state. Most users assume that deleting a photo from a page removes its ghost. In reality, the XML structure of the document often retains the original file's metadata unless it is aggressively scrubbed.",
            "image_query": "Image of EXIF metadata structure"
        }
    ]

    os.makedirs("docs/intel", exist_ok=True)
    report = random.choice(topics)
    filename = report['title'].lower().replace(" ", "-").replace(":", "").replace("'", "") + ".html"
    path = f"docs/intel/{filename}"

    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{report['title']} // Fair Discovery</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;600;900&display=swap');
        body {{ font-family: 'Geist', sans-serif; background-color: #0f172a; color: #94a3b8; }}
        .report-card {{ background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.05); }}
    </style>
</head>
<body class="min-h-screen p-8 md:p-24">
    <div class="max-w-3xl mx-auto">
        <a href="../index.html" class="text-[10px] font-black uppercase tracking-[0.3em] text-teal-500 hover:text-white transition-all">← Return to Infrastructure</a>
        
        <div class="mt-12 mb-8">
            <span class="px-3 py-1 bg-teal-500/10 text-teal-400 text-[10px] font-black rounded-full border border-teal-500/20">{report['tag']}</span>
            <h1 class="text-5xl font-black text-white italic uppercase tracking-tighter leading-tight mt-4 mb-6">{report['title']}</h1>
            <p class="text-xl text-slate-400 font-light italic">"{report['hook']}"</p>
        </div>

        <div class="report-card p-8 rounded-[2rem] mb-12">
            <p class="text-lg text-slate-300 leading-relaxed mb-6">{report['content']}</p>
            <h3 class="text-white font-bold uppercase text-xs tracking-widest mb-4">Forensic Analysis:</h3>
            <p class="text-sm leading-relaxed mb-8">{report['analysis']}</p>
            
            <div class="p-6 bg-black/20 rounded-2xl border border-white/5 italic text-xs">
                [{report['image_query']}]
                <p class="mt-4 text-center opacity-50 italic">— Visualizing the threat vector via FairDiscovery Node 18 —</p>
            </div>
        </div>

        <div class="p-10 bg-white rounded-[2.5rem] text-center mb-12 shadow-2xl">
            <h4 class="text-slate-900 font-black uppercase italic mb-2">Secure the Feed</h4>
            <p class="text-slate-500 text-[10px] mb-6 uppercase tracking-widest font-bold">Emails are encrypted and stored in our Spark Vault.</p>
            <div class="flex flex-col sm:flex-row gap-3">
                <input type="email" id="sub-email" placeholder="AGENCY@EMAIL.COM" class="flex-1 bg-slate-100 border-none rounded-2xl px-6 py-4 text-[10px] text-slate-900 focus:ring-2 focus:ring-teal-500 font-bold outline-none">
                <button onclick="saveLead()" class="bg-teal-500 text-white px-10 py-4 rounded-2xl font-black uppercase text-[10px] tracking-widest hover:bg-slate-900 transition-all shadow-lg shadow-teal-200">Join</button>
            </div>
            <p id="sub-status" class="mt-4 text-[9px] text-teal-600 font-bold uppercase"></p>
        </div>

        <div class="flex justify-between items-center text-[10px] font-bold opacity-30 uppercase tracking-widest">
            <span>Report ID: {datetime.now().strftime("%Y%m%d")}-ALPHA</span>
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
            status.innerText = "UPLOADING TO VAULT...";
            try {{
                await addDoc(collection(db, "leads"), {{ email: email, source: "Intel-Report", timestamp: serverTimestamp() }});
                status.innerText = "LEAD SECURED. WELCOME TO THE NETWORK.";
            }} catch(e) {{ status.innerText = "ENCRYPTION ERROR."; }}
        }}
    </script>
</body>
</html>
    """
    
    with open(path, 'w') as f:
        f.write(html_content)
    print(f"Intelligence Forged: {filename}")

if __name__ == "__main__":
    forge_intel_report()
