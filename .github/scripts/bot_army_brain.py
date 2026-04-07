import os
from datetime import datetime

# The Content Generator
def forge_intel_report():
    # In a future version, we can hook this to an AI API
    # For now, it generates structured forensic news
    topics = [
        {"title": "Tracking Pixel Surge", "tag": "Forensic Alert", "desc": "Widespread use of 1x1 transparent GIFs detected in legal PDF attachments."},
        {"title": "Metadata Leak in DOCX", "tag": "Privacy Risk", "desc": "Default 'Save' settings are exposing author GPS coordinates in government templates."},
    ]

    os.makedirs("docs/intel", exist_ok=True)

    for topic in topics:
        filename = topic['title'].lower().replace(" ", "-") + ".html"
        path = f"docs/intel/{filename}"
        
        # This is the Template the bot uses to build the page
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{topic['title']} // Fair Discovery Intel</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-slate-900 text-slate-300 p-12 font-mono">
            <div class="max-w-2xl mx-auto border border-white/10 p-8 rounded-3xl">
                <span class="text-teal-400 text-[10px] font-bold uppercase tracking-widest">{topic['tag']}</span>
                <h1 class="text-3xl text-white font-black uppercase mt-2 mb-6 italic">{topic['title']}</h1>
                <p class="leading-relaxed text-sm">{topic['desc']}</p>
                <div class="mt-8 pt-8 border-t border-white/5 flex justify-between items-center text-[10px]">
                    <span>REPORT ID: {datetime.now().strftime("%Y%m%d")}-ALPHA</span>
                    <a href="../sentinel-scrub.html" class="text-teal-400 underline">RUN SCAN</a>
                </div>
            </div>
        </body>
        </html>
        """
        
        with open(path, 'w') as f:
            f.write(html_content)
        print(f"Intel Forged: {filename}")

if __name__ == "__main__":
    forge_intel_report()
