/* Drone X Malaysia — V2 shared behaviour
   Language dropdown · mobile nav · reveal · tabs · dynamic year */
(function () {
  "use strict";

  var html = document.documentElement;
  html.classList.add("js");

  /* ---------- Language (EN / 中文 / Bahasa Malaysia) ---------- */
  var LANG_KEY = "dronex-lang";
  var LANG_CODES = { zh: "ZH", en: "EN", bm: "BM" };

  function closeAllLangDropdowns(exceptDd) {
    document.querySelectorAll(".lang-dd").forEach(function (dd) {
      if (dd === exceptDd) return;
      dd.classList.remove("open");
      var toggle = dd.querySelector(".lang-dd-toggle");
      var menu = dd.querySelector(".lang-dd-menu");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
      if (menu) menu.hidden = true;
    });
  }

  function applyLang(lang) {
    if (lang !== "en" && lang !== "bm") lang = "zh";
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang === "zh" ? "zh-Hans" : lang === "bm" ? "ms" : "en");
    document.querySelectorAll(".lang-dd").forEach(function (dd) {
      var codeEl = dd.querySelector(".lang-dd-code");
      if (codeEl) codeEl.textContent = LANG_CODES[lang];
      dd.querySelectorAll(".lang-dd-menu [data-lang]").forEach(function (li) {
        var active = li.getAttribute("data-lang") === lang;
        li.classList.toggle("active", active);
        li.setAttribute("aria-selected", active ? "true" : "false");
      });
    });
    /* <option> text can't use the .en/.zh/.bm span trick (browsers ignore
       CSS on option children), so sync it here whenever language changes. */
    document.querySelectorAll("option[data-en]").forEach(function (o) {
      o.textContent = o.getAttribute("data-" + lang) || o.getAttribute("data-en");
    });
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* private mode: keep in-page state only */ }
  }
  var saved = "zh";
  try { saved = localStorage.getItem(LANG_KEY) || "zh"; } catch (e) { /* ignore */ }
  applyLang(saved);

  document.addEventListener("click", function (ev) {
    var toggleBtn = ev.target.closest(".lang-dd-toggle");
    if (toggleBtn) {
      var dd = toggleBtn.closest(".lang-dd");
      var menu = dd.querySelector(".lang-dd-menu");
      var willOpen = !!(menu && menu.hidden);
      closeAllLangDropdowns(willOpen ? dd : null);
      if (menu) menu.hidden = !willOpen;
      toggleBtn.setAttribute("aria-expanded", willOpen ? "true" : "false");
      dd.classList.toggle("open", willOpen);
      return;
    }
    var option = ev.target.closest(".lang-dd-menu [data-lang]");
    if (option) {
      applyLang(option.getAttribute("data-lang"));
      closeAllLangDropdowns(null);
      return;
    }
    if (!ev.target.closest(".lang-dd")) closeAllLangDropdowns(null);
  });

  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" || ev.key === "Esc") closeAllLangDropdowns(null);
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
      var areaField = form.querySelector("[name=area]");
      var msg = form.querySelector("[name=message]");
      var svc = form.querySelector("[name=service]");
      if (svc) svc.value = "spraying";
      if (areaField && !areaField.value) {
        areaField.value = params.get("area") + " " + (params.get("unit") || "acre");
      }
      if (msg && !msg.value) {
        msg.value = "Calculator estimate — Purpose: " + (params.get("purpose") || "spraying") +
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
