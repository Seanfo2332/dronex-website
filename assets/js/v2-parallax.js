/**
 * Drone X Malaysia — lightweight scroll parallax (homepage only).
 *
 * Vanilla JS, zero dependencies. Applies a subtle vertical drift to
 * [data-parallax-speed] elements as the page scrolls, so backgrounds feel
 * like they recede slightly behind the foreground content — classic depth
 * parallax, not a scroll-scrubbed sequence.
 *
 * Safety/perf:
 * - No-op entirely under prefers-reduced-motion: reduce.
 * - Only elements currently near the viewport are tracked (IntersectionObserver),
 *   so idle sections cost nothing.
 * - A single shared rAF loop batches all reads (getBoundingClientRect) before
 *   all writes (style.transform) each frame, avoiding layout thrash.
 * - will-change is added only while an element is active, removed when it
 *   scrolls away.
 * - Elements must already sit inside an `overflow: hidden` ancestor (true for
 *   both current targets: .hero-v2 and .crop-card) — the constant OVERSCAN
 *   scale gives translate headroom without ever revealing an edge gap.
 */
(function () {
  "use strict";

  var OVERSCAN = 1.15;
  var ROOT_MARGIN = "25% 0px";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var targets = document.querySelectorAll("[data-parallax-speed]");
  if (reduceMotion || !targets.length || !("IntersectionObserver" in window)) return;

  var active = new Set();
  var ticking = false;

  function applyTransform(el) {
    var speed = parseFloat(el.dataset.parallaxSpeed) || 0;
    var rect = el.getBoundingClientRect();
    var viewportCenter = window.innerHeight / 2;
    var elementCenter = rect.top + rect.height / 2;
    var offset = (elementCenter - viewportCenter) * speed;
    return "scale(" + OVERSCAN + ") translate3d(0, " + offset.toFixed(1) + "px, 0)";
  }

  function updateFrame() {
    ticking = false;
    if (!active.size) return;

    // Batch reads, then batch writes — avoids interleaved layout/paint thrash.
    var updates = [];
    active.forEach(function (el) {
      updates.push({ el: el, transform: applyTransform(el) });
    });
    updates.forEach(function (u) {
      u.el.style.transform = u.transform;
    });
  }

  function requestUpdate() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(updateFrame);
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          active.add(entry.target);
          entry.target.style.willChange = "transform";
        } else {
          active.delete(entry.target);
          entry.target.style.willChange = "";
        }
      });
      requestUpdate();
    },
    { rootMargin: ROOT_MARGIN }
  );

  targets.forEach(function (el) {
    io.observe(el);
  });

  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate, { passive: true });
})();
