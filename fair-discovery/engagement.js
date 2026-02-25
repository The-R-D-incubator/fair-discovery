(async () => {
  const root = "/fair-discovery/";
  const res = await fetch(root + "discovery.json");
  const config = await res.json();
  const PIXELS = config.pixels || {};

  // 1. TRIAL PROTECTION
  const trialStart = new Date(config.visitors.current_week_start);
  const daysActive = Math.ceil((new Date() - trialStart) / (1000 * 60 * 60 * 24));
  const isLicensed = config.license === "LIFETIME";

  if (daysActive > 30 && !isLicensed) {
    const wall = document.createElement('div');
    wall.style.cssText = "position:fixed;inset:0;z-index:999999;background:rgba(0,0,0,0.98);display:flex;align-items:center;justify-content:center;color:white;text-align:center;font-family:sans-serif;padding:40px;";
    wall.innerHTML = `<div><h2 style="font-size:32px;font-weight:900;">Trial Expired</h2><p style="color:#666;margin:20px 0;">Unlock Lifetime Ad Spend Protection.</p><a href="https://fairdiscovery.org/pay?site=${window.location.hostname}" style="background:#3b82f6;color:white;padding:20px 40px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;">Get Lifetime License (R1499)</a></div>`;
    document.body.appendChild(wall);
    return;
  }

  let fired = false;
  let source = "Direct/Website";
  const ref = document.referrer.toLowerCase();
  const par = new URLSearchParams(window.location.search);
  if (ref.includes("youtube.com") || par.has("ref")) source = "YouTube";
  else if (ref.includes("tiktok.com")) source = "TikTok";
  else if (ref.includes("google.com") || par.has("gclid")) source = "Google/Ads";

  function release() {
    if (fired) return; fired = true;
    console.log(`[Fair Discovery] Human Verified: ${source}`);
    // FIRE PIXELS DYNAMICALLY
    if (PIXELS.FB) { /* Meta Implementation */ }
    if (PIXELS.GTAG) { /* Google Implementation */ }
    if (PIXELS.TT) { /* TikTok Implementation */ }
    if (PIXELS.LI) { /* LinkedIn Implementation */ }
  }

  window.addEventListener("scroll", () => { if(window.scrollY > 15) release(); });
  ["click", "mousemove", "touchstart"].forEach(e => window.addEventListener(e, release, {once: true}));

  // SHADOW CALL: Silently records path and source
  window.addEventListener("beforeunload", () => {
    navigator.sendBeacon(root + "record.php", JSON.stringify({ path: location.pathname, source: source, score: 1 }));
  });
})();
