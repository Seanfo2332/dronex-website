/* Drone X Malaysia — Drone Spraying Calculator (Farmer Solutions)
   ⚠ PLACEHOLDER RATES — the group must supply real coverage standards
   (PDF §14: acres/hectares per drone per hour) before go-live.       */
(function () {
  "use strict";

  /* -- Placeholder assumptions (clearly marked, swap when real data arrives) -- */
  var ACRES_PER_DRONE_HOUR = 20;   // TODO(pending): real figure from group
  var MAX_HOURS_PER_DAY = 6;       // TODO(pending): real operating window
  var HA_TO_ACRE = 2.47105;
  var SQFT_TO_ACRE = 1 / 43560;

  var state = { unit: "acre", purpose: "spraying", crop: "" };

  var root = document.getElementById("spray-calculator");
  if (!root) return;

  function bindChips(groupSel, key) {
    root.querySelectorAll(groupSel + " .chip").forEach(function (chip) {
      chip.addEventListener("click", function () {
        root.querySelectorAll(groupSel + " .chip").forEach(function (c) {
          c.setAttribute("aria-pressed", c === chip ? "true" : "false");
        });
        state[key] = chip.getAttribute("data-value");
        compute();
      });
    });
  }
  bindChips("[data-group=unit]", "unit");
  bindChips("[data-group=purpose]", "purpose");
  bindChips("[data-group=crop]", "crop");

  var areaInput = document.getElementById("calc-area");
  areaInput.addEventListener("input", compute);

  var resultBox = document.getElementById("calc-result");
  /* Reads the active language off <html data-lang>, set by v2-main.js.
     Falls back to "en" for any unrecognised value. */
  var getLang = function () {
    var lang = document.documentElement.getAttribute("data-lang");
    return (lang === "zh" || lang === "bm") ? lang : "en";
  };

  function toAcres(v) {
    if (state.unit === "hectare") return v * HA_TO_ACRE;
    if (state.unit === "sqft") return v * SQFT_TO_ACRE;
    return v;
  }

  function serviceLabel() {
    var map = {
      spraying:    { en: "Drone Spraying", zh: "无人机喷药", bm: "Semburan Dron" },
      fertilizing: { en: "Drone Fertilizing", zh: "无人机施肥", bm: "Baja Dron" },
      both:        { en: "Spraying + Fertilizing", zh: "喷药＋施肥", bm: "Semburan + Baja" }
    };
    return map[state.purpose] || map.spraying;
  }

  function droneUnitLabel(count) {
    if (getLang() === "zh") return " 架";
    if (getLang() === "bm") return " dron";
    return count > 1 ? " drones" : " drone";
  }

  function compute() {
    var raw = parseFloat(areaInput.value);
    if (!raw || raw <= 0) { resultBox.hidden = true; return; }

    var acres = toAcres(raw);
    var passes = state.purpose === "both" ? 2 : 1;
    var hours = (acres * passes) / ACRES_PER_DRONE_HOUR;
    var drones = Math.max(1, Math.ceil(hours / MAX_HOURS_PER_DAY));
    var hoursWithFleet = hours / drones;
    var lang = getLang();
    var timeTxt;
    if (hoursWithFleet <= 1) {
      timeTxt = { en: "Under ~1 hour", zh: "约 1 小时内", bm: "Bawah ~1 jam" }[lang];
    } else if (hoursWithFleet <= MAX_HOURS_PER_DAY) {
      var h = Math.ceil(hoursWithFleet);
      timeTxt = {
        en: "~" + h + " hours (within 1 day)",
        zh: "约 " + h + " 小时（1 天内）",
        bm: "~" + h + " jam (dalam 1 hari)"
      }[lang];
    } else {
      var d = Math.ceil(hoursWithFleet / MAX_HOURS_PER_DAY);
      timeTxt = {
        en: "~" + d + " working days",
        zh: "约 " + d + " 个工作天",
        bm: "~" + d + " hari bekerja"
      }[lang];
    }

    var svc = serviceLabel();
    document.getElementById("res-service").textContent = svc[lang];
    document.getElementById("res-drones").textContent = drones + droneUnitLabel(drones);
    document.getElementById("res-time").textContent = timeTxt;

    /* Handoff link → contact form pre-filled (PDF: farmer不用重复填写) */
    var q = new URLSearchParams({
      area: String(raw), unit: state.unit, purpose: state.purpose
    });
    if (state.crop) q.set("crop", state.crop);
    document.getElementById("calc-quote-link")
      .setAttribute("href", "contact-us.html?" + q.toString() + "#inquiry");

    resultBox.hidden = false;
  }

  /* Recompute label language when the lang dropdown changes selection */
  new MutationObserver(function () {
    if (!resultBox.hidden) compute();
  }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-lang"] });
})();
