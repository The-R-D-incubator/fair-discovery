/**
 * Fair Discovery | All-in-One Global Gatekeeper
 * Protects Ad Budgets by verifying humans before firing pixels.
 */
(() => {
  const start = Date.now();
  let maxDepth = 0;
  let interactions = 0;
  let pixelsFired = false;

  // ----------------------------------------------------
  // 🟢 CONFIGURATION: ENTER YOUR IDS BELOW
  // ----------------------------------------------------
  const IDS = {
    FACEBOOK_PIXEL: "YOUR_FB_ID_HERE", 
    GOOGLE_GTAG: "G-XXXXXXXXXX",
    LINKEDIN_PARTNER: "YOUR_LINKEDIN_ID_HERE"
  };
  // ----------------------------------------------------

  function triggerAllPixels() {
    if (pixelsFired) return; 
    pixelsFired = true;

    console.log("[FairDiscovery] Human detected. Releasing Protected Pixels... 🎯");

    // 1. FIRE FACEBOOK PIXEL
    if (IDS.FACEBOOK_PIXEL !== "YOUR_FB_ID_HERE") {
        !function(f,b,e,v,n,t,s)
        {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
        n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)}(window, document,'script',
        'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', IDS.FACEBOOK_PIXEL);
        fbq('track', 'PageView'); 
    }

    // 2. FIRE GOOGLE GTAG
    if (IDS.GOOGLE_GTAG !== "G-XXXXXXXXXX") {
        let gt = document.createElement('script');
        gt.async = true;
        gt.src = `https://www.googletagmanager.com/gtag/js?id=${IDS.GOOGLE_GTAG}`;
        document.head.appendChild(gt);
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', IDS.GOOGLE_GTAG);
    }

    // 3. FIRE LINKEDIN INSIGHT TAG
    if (IDS.LINKEDIN_PARTNER !== "YOUR_LINKEDIN_ID_HERE") {
        window._linkedin_data_partner_id = IDS.LINKEDIN_PARTNER;
        (function(l) {
        if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
        window.lintrk.q=[]}
        var s = document.getElementsByTagName("script")[0];
        var b = document.createElement("script");
        b.type = "text/javascript";b.async = true;
        b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
        s.parentNode.insertBefore(b, s);})(window.lintrk);
    }
  }

  // DETECTION LOGIC: Scroll Detection
  window.addEventListener("scroll", () => {
    const depth = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    maxDepth = Math.max(maxDepth, depth);
    if (maxDepth > 0.01) triggerAllPixels();
  });

  // DETECTION LOGIC: Interaction Detection
  ["click", "mousemove", "keydown", "touchstart"].forEach(evt => {
    window.addEventListener(evt, () => {
      interactions++;
      triggerAllPixels(); 
    });
  });

  // DATA RECORDING LOGIC
  window.addEventListener("beforeunload", () => {
    if (interactions === 0 && maxDepth === 0) return;

    const timeSpent = (Date.now() - start) / 1000;
    const score = Math.round((timeSpent * (maxDepth + 0.1) * (interactions + 1)) / 5);
    
    const data = JSON.stringify({ path: location.pathname, score });
    const url = "/record.php"; // Path adjusted to your root folder
    
    navigator.sendBeacon(url, data);
  });

  console.log("[FairDiscovery] All-in-One Global Gatekeeper Initialized ✅");
})();
