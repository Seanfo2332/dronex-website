/* Drone X Malaysia — V2 shared behaviour
   Language toggle · mobile nav · reveal · tabs · dynamic year */
(function () {
  "use strict";

  var html = document.documentElement;
  html.classList.add("js");

  /* ---------- Language (EN / 中文) ---------- */
  var LANG_KEY = "dronex-lang";
  function applyLang(lang) {
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang === "zh" ? "zh-Hans" : "en");
    document.querySelectorAll(".lang-toggle button").forEach(function (b) {
      b.classList.toggle("active", b.getAttribute("data-lang") === lang);
    });
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* private mode: keep in-page state only */ }
  }
  var saved = "zh";
  try { saved = localStorage.getItem(LANG_KEY) || "zh"; } catch (e) { /* ignore */ }
  applyLang(saved === "en" ? "en" : "zh");

  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest(".lang-toggle button");
    if (btn) applyLang(btn.getAttribute("data-lang") === "zh" ? "zh" : "en");
  });

  /* ---------- Mobile menu ---------- */
  var burger = document.querySelector(".nav-burger");
  var menu = document.querySelector(".mobile-menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    menu.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) {
        menu.classList.remove("open");
        document.body.style.overflow = "";
      }
    });
  }

  /* ---------- Scroll motion: reveals + staggered grids (enhancement only) ---------- */
  var motionEls = document.querySelectorAll(".reveal, .stagger");
  if ("IntersectionObserver" in window && motionEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    motionEls.forEach(function (el) { io.observe(el); });
  } else {
    motionEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Header shadow once page is scrolled ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 8);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Stat count-up (respects reduced motion) ---------- */
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var stats = document.querySelectorAll("[data-countup]");
  if (stats.length && !reduceMotion && "IntersectionObserver" in window) {
    var statIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        statIO.unobserve(en.target);
        var el = en.target;
        var m = el.textContent.trim().match(/^([\d,]+)(.*)$/);
        if (!m) return;
        var target = parseInt(m[1].replace(/,/g, ""), 10);
        var suffix = m[2] || "";
        var t0 = null;
        var DUR = 900;
        function tick(ts) {
          if (t0 === null) t0 = ts;
          var k = Math.min((ts - t0) / DUR, 1);
          k = 1 - Math.pow(1 - k, 4); /* ease-out-quart */
          el.textContent = Math.round(target * k).toLocaleString("en-US") + suffix;
          if (k < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    stats.forEach(function (el) { statIO.observe(el); });
  }

  /* ---------- Tabs (Media Centre) ---------- */
  function selectTab(tabs, btn) {
    tabs.querySelectorAll(".tab-btn").forEach(function (b) {
      b.setAttribute("aria-selected", b === btn ? "true" : "false");
    });
    var scope = tabs.parentElement;
    scope.querySelectorAll(".tab-panel").forEach(function (p) {
      p.hidden = p.id !== btn.getAttribute("aria-controls");
    });
  }
  document.querySelectorAll(".tabs").forEach(function (tabs) {
    tabs.addEventListener("click", function (ev) {
      var btn = ev.target.closest(".tab-btn");
      if (!btn) return;
      selectTab(tabs, btn);
    });
    // Deep-link support: /media.html#tab-news opens straight to that tab
    // (e.g. a "back to Media Centre" link from a news article page).
    if (location.hash) {
      var targetBtn = tabs.querySelector('.tab-btn[aria-controls="' + location.hash.slice(1) + '"]');
      if (targetBtn) selectTab(tabs, targetBtn);
    }
  });

  /* ---------- Dynamic year (never hardcode) ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Contact form (client-side; backend email pending) ---------- */
  var form = document.getElementById("inquiry-form");
  if (form) {
    /* Prefill from calculator handoff (?area=…&unit=…&purpose=…) */
    var params = new URLSearchParams(location.search);
    if (params.get("area")) {
      var msg = form.querySelector("[name=message]");
      var svc = form.querySelector("[name=service]");
      if (svc) svc.value = "spraying";
      if (msg && !msg.value) {
        msg.value = "Calculator estimate — Area: " + params.get("area") + " " +
          (params.get("unit") || "acre") + ", Purpose: " + (params.get("purpose") || "spraying") +
          (params.get("crop") ? ", Crop: " + params.get("crop") : "");
      }
    }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        var wrap = field.closest(".form-field");
        var bad = !field.value.trim();
        if (field.name === "phone" && field.value.trim()) {
          bad = !/^[+0-9 ()-]{7,20}$/.test(field.value.trim());
        }
        if (wrap) wrap.classList.toggle("invalid", bad);
        if (bad) valid = false;
      });
      if (!valid) return;
      /* TODO(pending): wire to email service once Shirley's team provides
         the receiving inbox (PDF §14). Options: Formspree / Vercel function. */
      form.hidden = true;
      var thanks = document.getElementById("form-thanks");
      if (thanks) {
        thanks.hidden = false;
        thanks.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }
})();
