/**
 * Fair Discovery | Global Gatekeeper & Source Tracker
 */
(() => {
  const CONFIG = {
    DASHBOARD_PATH: "/fair-discovery/record.php",
    PIXELS: { FB: "YOUR_FB_ID", GTAG: "G-XXXXXXXXXX", LI: "YOUR_LI_ID", TT: "YOUR_TT_ID" }
  };

  let fired = false;
  let sourceChannel = "Direct/Website";

  // Identify Source
  const ref = document.referrer.toLowerCase();
  const params = new URLSearchParams(window.location.search);
  if (ref.includes("youtube.com") || params.has("ref")) sourceChannel = "YouTube";
  else if (ref.includes("tiktok.com")) sourceChannel = "TikTok";
  else if (ref.includes("google.com") || params.has("gclid")) sourceChannel = "Google/Ads";

  function release() {
    if (fired) return; fired = true;
    console.log(`[FairDiscovery] Source: ${sourceChannel} | Human Verified.`);
    // Pixel firing logic (FB, GTag, LI, TT) here...
  }

  window.addEventListener("scroll", () => { if(window.scrollY > 15) release(); });
  ["click", "mousemove", "touchstart"].forEach(e => window.addEventListener(e, release, {once: true}));

  window.addEventListener("beforeunload", () => {
    const data = JSON.stringify({ path: location.pathname, source: sourceChannel, score: 1 });
    navigator.sendBeacon(CONFIG.DASHBOARD_PATH, data);
  });
})();
