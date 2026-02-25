/**
 * Fair Discovery | All-in-One Global Gatekeeper
 * Facebook, Google, LinkedIn, TikTok + Honeypot
 */
(() => {
  const CONFIG = {
    COMPANY: "Your Company Name",
    PIXELS: {
      FB: "YOUR_FB_ID",
      GTAG: "G-XXXXXXXXXX",
      LINKEDIN: "YOUR_LI_ID",
      TIKTOK: "YOUR_TT_ID"
    }
  };

  let fired = false;
  let bot = false;

  // 🛡️ HONEYPOT: Trap bots clicking invisible elements
  const hp = document.createElement('input');
  hp.type = 'checkbox';
  hp.style.cssText = "position:absolute;opacity:0;z-index:-1;left:-999px";
  hp.addEventListener('change', () => { bot = true; console.warn("Bot Blocked."); });
  document.body.appendChild(hp);

  function release() {
    if (fired || bot) return;
    fired = true;
    console.log(`[FairDiscovery] ${CONFIG.COMPANY}: Human Verified.`);

    // 1. Meta (Facebook)
    if (CONFIG.PIXELS.FB) {
        !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', CONFIG.PIXELS.FB); fbq('track', 'PageView');
    }

    // 2. Google
    if (CONFIG.PIXELS.GTAG) {
        let s = document.createElement('script'); s.async=true; s.src=`https://www.googletagmanager.com/gtag/js?id=${CONFIG.PIXELS.GTAG}`;
        document.head.appendChild(s); window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', CONFIG.PIXELS.GTAG);
    }

    // 3. LinkedIn
    if (CONFIG.PIXELS.LINKEDIN) {
        window._linkedin_data_partner_id = CONFIG.PIXELS.LINKEDIN;
        (function(l){if(!l){window.lintrk=function(a,b){window.lintrk.q.push([a,b])};window.lintrk.q=[]}
        var s=document.getElementsByTagName("script")[0]; var b=document.createElement("script");
        b.type="text/javascript";b.async=true;b.src="https://snap.licdn.com/li.lms-analytics/insight.min.js";
        s.parentNode.insertBefore(b, s);})(window.lintrk);
    }

    // 4. TikTok
    if (CONFIG.PIXELS.TIKTOK) {
        !function(w,d,t){w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","trackAdClick","trackAdReveal"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var z="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=z,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n;var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=z+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};ttq.load(CONFIG.PIXELS.TIKTOK);ttq.page();}(window,document,'ttq');
    }
  }

  window.addEventListener("scroll", () => { if(window.scrollY > 20) release(); });
  ["click", "mousemove", "keydown"].forEach(e => window.addEventListener(e, release, {once: true}));

  window.addEventListener("beforeunload", () => {
    if (bot) return;
    navigator.sendBeacon("/fair-discovery/record.php", JSON.stringify({ path: location.pathname, score: 1 }));
  });
})();
