/**
 * Drone X Malaysia — GSAP ScrollTrigger engine bootstrap.
 *
 * Loaded after the self-hosted assets/js/vendor/gsap/{gsap,ScrollTrigger}.min.js
 * (both plain global/UMD builds — GSAP v3.15, free for all use under GSAP's
 * current Standard License since the 2024 relicense: https://gsap.com/pricing).
 *
 * This file only registers the plugin and exposes a couple of shared
 * constants/helpers on window.ScrollFx for the recipe file (scroll-fx.js)
 * to use. No animation logic lives here.
 */
(function () {
  "use strict";

  if (!window.gsap || !window.ScrollTrigger) {
    // Vendor script failed to load/parse — fail silently. Every recipe in
    // scroll-fx.js also checks for window.gsap itself, so the site's
    // existing content/layout is completely unaffected either way.
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  // Mobile browsers resize the viewport (address bar show/hide) constantly
  // during scroll; without this, ScrollTrigger would recalculate on every
  // one of those and cause jank.
  ScrollTrigger.config({ ignoreMobileResize: true });

  window.ScrollFx = {
    reduceMotion: window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    DESKTOP_QUERY: "(min-width: 800px)",
    MOBILE_QUERY: "(max-width: 799px)",
  };
})();
