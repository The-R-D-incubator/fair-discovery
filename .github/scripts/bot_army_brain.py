import os
import random
from datetime import datetime

def forge_intel_report():
    # Expanded Library: High-Value Tech Sovereignty & Privacy
    briefings = [
        {
            "title": "Linux vs. Windows: The Kernel of Truth",
            "tag": "SYSTEM SOVEREIGNTY",
            "content": "Windows isn't an OS; it's a telemetry suite that happens to run apps. Switching to a hardened Linux kernel isn't about being a 'hacker'—it's about owning your own CPU cycles and ensuring your file system isn't a glass house.",
            "insight": "Start with a bootable Mint or Fedora drive. Experience what it feels like to not be 'indexed' by your own hardware."
        },
        {
            "title": "iPhone Hardening: The Lockdown Myth",
            "tag": "MOBILE FORENSICS",
            "content": "Apple’s 'Privacy' marketing is the best in the business, but 'Lockdown Mode' is only the first step. iCloud backups remain the single largest leak-point for forensic investigators to bypass device encryption.",
            "insight": "Disable cloud-sync for sensitive notes and use local, encrypted backups to maintain a true 'Air-Gap'."
        },
        {
            "title": "Signal vs. WhatsApp: The Metadata War",
            "tag": "SECURE COMMS",
            "content": "WhatsApp encrypts the message, but Meta owns the metadata. They know *who* you talked to, *when*, and for *how long*. Signal is the only consumer-grade node that treats metadata as toxic waste—it simply doesn't store it.",
            "insight": "If the platform knows your contact list, you are the product. Signal's sealed-sender protocol is the industry benchmark."
        },
        {
            "title": "TikTok: The Packet-Sniffer in Your Pocket",
            "tag": "APP AUDIT",
            "content": "TikTok’s in-app browser is a keylogger. Every keystroke made while viewing an external link inside the app is visible to the parent node. It is the most efficient data-harvesting tool ever deployed at scale.",
            "insight": "Never use in-app browsers. Always break the sandbox and open links in a hardened, external browser."
        },
        {
            "title": "YouTube & Google: The Behavioral Ghost",
            "tag": "SHADOW PROFILING",
            "content": "Google doesn't need your name to know who you are. Your watch history, dwell time, and scroll speed create a 'Behavioral Fingerprint' that is more accurate than a DNA test for target-marketing.",
            "insight": "Use front-ends like FreeTube or NewPipe to consume content without feeding the behavioral engine."
        }
    ]

    # ... [Rest of the social topics from the previous update go here as well] ...

    os.makedirs("docs/intel", exist_ok=True)
    report = random.choice(briefings)
    filename = report['title'].lower().replace(" ", "-").replace(":", "").replace("/", "-").replace("'", "") + ".html"
    path = f"docs/intel/{filename}"
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{report['title']} // Fair Discovery Intel</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;900&display=swap');
        body {{ font-family: 'Geist', sans-serif; background-color: #0f172a; color: #94a3b8; }}
        .node-card {{ background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(45, 212, 191, 0.1); }}
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6 bg-slate-950">
    <div class="max-w-xl w-full p-12 node-card rounded-[2.5rem] shadow-2xl">
        <div class="flex justify-between items-center mb-10">
            <a href="../index.html" class="text-[10px] font-black uppercase tracking-widest text-teal-500 hover:text-white transition-all">← Secure Node</a>
            <span class="text-slate-600 text-[10px] font-bold uppercase tracking-widest italic">Node: FD-18</span>
        </div>
        
        <div class="mb-8">
            <span class="text-teal-400 text-[10px] font-black uppercase tracking-widest border-b border-teal-500/30 pb-1">{report['tag']}</span>
            <h1 class="text-4xl font-black text-white italic uppercase tracking-tighter leading-none mt-4">{report['title']}</h1>
        </div>

        <p class="text-lg text-slate-200 leading-relaxed mb-6 font-light">{report['content']}</p>
        
        <div class="p-6 bg-teal-500/5 rounded-2xl border border-teal-500/10 mb-8">
            <p class="text-xs italic text-teal-400">"Professional Action: {report['insight']}"</p>
        </div>

        <div class="pt-8 border-t border-white/5">
            <p class="text-[9px] text-slate-500 font-black uppercase tracking-[0.2em] mb-4 text-center">Join the Intel Network for Exclusive Tools</p>
            <div class="flex flex-col gap-3">
                <input type="email" id="sub-email" placeholder="SECURE@EMAIL.COM" class="bg-black border border-white/10 rounded-xl px-4 py-3 text-[10px] text-teal-400 focus:outline-none focus:border-teal-500 text-center">
                <button onclick="saveLead()" class="bg-teal-500 text-black py-3 rounded-xl font-black uppercase text-[10px] hover:bg-white transition-all">Join & Get 20 Credits</button>
            </div>
            <p id="sub-status" class="mt-4 text-[9px] text-teal-500 font-bold uppercase text-center"></p>
        </div>

        <div class="mt-12 pt-8 flex justify-between items-center opacity-20 text-[8px] font-black uppercase tracking-widest">
            <span>ID: {datetime.now().strftime("%Y%m%d")}-ALPHA</span>
            <span>FairDiscovery.org // Forensic Unit</span>
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
                status.innerText = "ACCESS GRANTED. CHECK STORAGE.";
            }} catch(e) {{ status.innerText = "VAULT OFFLINE."; }}
        }}
    </script>
</body>
</html>
    """
    
    with open(path, 'w') as f:
        f.write(html_content)
