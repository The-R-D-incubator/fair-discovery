/**
 * Fair Discovery | Source-Aware Gatekeeper
 * Automatically identifies YouTube, TikTok, and Search traffic.
 */
(() => {
  const CONFIG = {
    DASHBOARD_PATH: "/fair-discovery/record.php"
  };

  let pixelsFired = false;
  let sourceChannel = "Direct/Website";

  // DETECT SOURCE: Identifies where the human came from
  const ref = document.referrer.toLowerCase();
  if (ref.includes("youtube.com") || location.search.includes("ref=youtube")) sourceChannel = "YouTube";
  else if (ref.includes("tiktok.com")) sourceChannel = "TikTok";
  else if (ref.includes("google.com") || location.search.includes("gclid")) sourceChannel = "Google/Ads";

  function release() {
    if (pixelsFired) return;
    pixelsFired = true;
    console.log(`[FairDiscovery] Source: ${sourceChannel} | Human Verified.`);
    // Pixel firing logic remains here...
  }

  window.addEventListener("scroll", () => { if(window.scrollY > 20) release(); });
  ["click", "mousemove", "keydown"].forEach(e => window.addEventListener(e, release, {once: true}));

  window.addEventListener("beforeunload", () => {
    const data = JSON.stringify({ 
        path: location.pathname, 
        source: sourceChannel, // Sends the specific channel
        score: 1 
    });
    navigator.sendBeacon(CONFIG.DASHBOARD_PATH, data);
  });
})();
