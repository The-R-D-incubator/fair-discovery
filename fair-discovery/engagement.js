/**
 * Fair Discovery | Global Gatekeeper v2.0
 * Includes: Meta, Google, LinkedIn, and TikTok.
 * Feature: Bot Honeypot & Human Verification.
 */
(() => {
  // --- 🟢 CUSTOMER CONFIGURATION AREA ---
  const CONFIG = {
    COMPANY_NAME: "Your Company Name",
    LICENSE_KEY: "FD-XXXX-XXXX",
    PIXELS: {
      FACEBOOK: "YOUR_FB_ID",
      GOOGLE_GTAG: "G-XXXXXXXXXX",
      LINKEDIN: "YOUR_LINKEDIN_ID",
      TIKTOK: "YOUR_TIKTOK_ID" // Added TikTok Support
    },
    DASHBOARD_PATH: "/fair-discovery/record.php" [cite: 5, 6]
  };
  // ---------------------------------------

  const start = Date.now();
  let pixelsFired = false;

  // HONEYPOT: Bots often try to fill hidden inputs or click hidden elements
  let honeypotTriggered = false;
  const hp = document.createElement('div');
  hp.style.cssText = "opacity:0;position:absolute;z-index:-1;left:-999px;";
  hp.innerHTML = `<input type="text" id="fd_honeypot" tabindex="-1" value="">`;
  document.body.appendChild(hp);

  document.getElementById('fd_honeypot').addEventListener('change', () => {
    honeypotTriggered = true; 
    console.warn("Fair Discovery: Bot detected via Honeypot.");
  });

  function releasePixels() {
    if (pixelsFired || honeypotTriggered) return;
    pixelsFired = true;

    console.log(`[${CONFIG.COMPANY_NAME}] Human Verified. Releasing Pixels...`);

    // TIKTOK PIXEL
    if (CONFIG.PIXELS.TIKTOK) {
        !function (w, d, t) { w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","trackAdClick","trackAdReveal"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var z="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=z,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n;var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=z+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
        ttq.load(CONFIG.PIXELS.TIKTOK);
        ttq.page();
    }(window, document, 'ttq');
    }

    // FIRE OTHERS (GTag, FB, LinkedIn as per previous logic)
    // ... [Previous logic for FB, Google, and LinkedIn goes here]
  }

  // HUMAN SENSORS
  window.addEventListener("scroll", () => { if(window.scrollY > 20) releasePixels(); });
  ["click", "mousemove", "keydown"].forEach(e => window.addEventListener(e, releasePixels, {once: true}));

  // RECORDING
  window.addEventListener("beforeunload", () => {
    if (honeypotTriggered) return; 
    const data = JSON.stringify({ path: location.pathname, score: 1 });
    navigator.sendBeacon(CONFIG.DASHBOARD_PATH, data); [cite: 5, 6]
  });
})();
