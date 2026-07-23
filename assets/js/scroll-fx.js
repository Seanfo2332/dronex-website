/**
 * Drone X Malaysia — GSAP ScrollTrigger recipes.
 *
 * Each recipe below is guarded by an element-existence check, so pages that
 * don't have a given section simply skip that block at ~zero cost. Nothing
 * here is required content: if GSAP fails to load, or the visitor prefers
 * reduced motion, this file does nothing and the page's normal (already
 * fully designed) layout and copy remain exactly as-is.
 */
(function () {
  "use strict";

  if (!window.gsap || !window.ScrollTrigger || !window.ScrollFx) return;
  if (window.ScrollFx.reduceMotion) return;

  var MOBILE_QUERY = window.ScrollFx.MOBILE_QUERY;

  /* ---------- 1. Before/After dramatic entrance (homepage only) ----------
     Panels converge from opposite directions with a slight rotation,
     settling into place — dramatizes the comparison instead of a plain fade. */
  var beforeAfter = document.querySelector(".before-after");
  if (beforeAfter) {
    var baBefore = beforeAfter.querySelector(".ba-before");
    var baAfter = beforeAfter.querySelector(".ba-after");
    if (baBefore && baAfter) {
      var baIsMobile = window.matchMedia(MOBILE_QUERY).matches;
      var baSlide = baIsMobile ? 30 : 60;
      var baRotate = baIsMobile ? 1.5 : 3;
      gsap.set(baBefore, { autoAlpha: 0, x: -baSlide, rotate: -baRotate });
      gsap.set(baAfter, { autoAlpha: 0, x: baSlide, rotate: baRotate });
      gsap
        .timeline({ scrollTrigger: { trigger: beforeAfter, start: "top 82%" } })
        .to(baBefore, { autoAlpha: 1, x: 0, rotate: 0, duration: 0.8, ease: "power3.out" })
        .to(baAfter, { autoAlpha: 1, x: 0, rotate: 0, duration: 0.8, ease: "power3.out" }, "-=0.55");
    }
  }

  /* ---------- 2. Compare-table row cascade (homepage only) ----------
     .compare-row uses `display: contents` (see v2-pages.css), so it isn't
     itself animatable — .compare-cell is the real animation target. DOM
     order already groups cells by row, so a plain stagger reads as a
     natural top-to-bottom row cascade. */
  var compareTable = document.querySelector(".compare-table");
  if (compareTable) {
    var cells = compareTable.querySelectorAll(".compare-cell");
    if (cells.length) {
      gsap.set(cells, { autoAlpha: 0, y: 16 });
      ScrollTrigger.batch(cells, {
        start: "top 90%",
        once: true,
        onEnter: function (batch) {
          gsap.to(batch, { autoAlpha: 1, y: 0, duration: 0.5, stagger: 0.04, ease: "power2.out" });
        },
      });
    }
  }

  /* ---------- 3. Step-card dramatic entrance (Home + Farmer Solutions) ----------
     Replaces the plain fade with a scale/rotate "settle" for extra flair.
     Matches .step on both the homepage's plain 1x4 row and Farmer
     Solutions' 2x2 photo cards (assets/css .steps--visual). */
  var steps = document.querySelectorAll(".step");
  if (steps.length) {
    gsap.set(steps, { autoAlpha: 0, y: 40, scale: 0.92, rotate: -2 });
    ScrollTrigger.batch(steps, {
      start: "top 88%",
      once: true,
      onEnter: function (batch) {
        gsap.to(batch, {
          autoAlpha: 1,
          y: 0,
          scale: 1,
          rotate: 0,
          duration: 0.7,
          stagger: 0.12,
          ease: "back.out(1.4)",
        });
      },
    });
  }
})();
