# Drone X Malaysia — Design System (V2)

> Implemented in `assets/css/v2-base.css` (tokens + chrome) and
> `assets/css/v2-pages.css` (page components). The old navy/Geist system is retired
> with the legacy site (`legacy-v1-index.html`).

## Color Tokens (OKLCH)
```
--bg:         oklch(100% 0 0)          /* pure white body            */
--surface:    oklch(96.5% 0.004 150)   /* light section block        */
--surface-2:  oklch(93.5% 0.006 150)   /* deeper block               */
--ink:        oklch(21% 0.01 250)      /* near-black text            */
--ink-2:      oklch(42% 0.012 250)     /* secondary text             */
--green:      oklch(56% 0.155 152)     /* CTA / brand accent         */
--green-deep: oklch(46% 0.13 152)      /* hover, trust bar, results  */
--green-tint: oklch(95% 0.03 152)      /* soft green washes          */
--line:       oklch(88% 0.004 250)     /* hairline borders           */
--wa:         #25d366                  /* WhatsApp float only        */
```
Strategy: white base + ink, one committed green accent (~10-15% of surface).
Footer and secondary buttons use ink. Never introduce new hues.

## Typography
```
--font: "Montserrat", "Noto Sans SC", "Segoe UI", sans-serif
--text-hero: clamp(2.1rem, 4.6vw, 3.9rem)   weight 800, tracking -0.02em
--text-h2:   clamp(1.6rem, 3vw, 2.5rem)     weight 800
--text-h3:   clamp(1.15rem, 1.8vw, 1.45rem) weight 700
--text-lead: clamp(1.02rem, 1.3vw, 1.2rem)  color --ink-2
body 1rem / 1.7
```
Montserrat is a client mandate (registered as impeccable ignore-value).
Chinese renders through Noto Sans SC fallback automatically.

## Shape & Rhythm
- Radius: 14px cards/panels, pill (999px) buttons and chips (Grab-style friendly rounding)
- Section padding: `--space-section: clamp(4rem, 8vw, 7.5rem)`; alternate white / --surface blocks
- Wrap: 1180px

## Key Components
- **Header**: sticky, solid white (NO backdrop-filter — it becomes the containing block
  for the fixed mobile menu and breaks it), 6 nav links + lang toggle + green pill CTA
- **Lang toggle**: `.lang-toggle` buttons set `html[data-lang]`; content pairs
  `<span class="en">/<span class="zh">`
- **Sticky WhatsApp float**: `.wa-float`, z-index --z-toast, label hides ≤600px
- **Buttons**: `.btn-primary` (green), `.btn-secondary` (ink), `.btn-ghost`, `.btn-light`
- **Steps**: CSS counter circles (real numbered sequence, per PDF workflow)
- **FAQ**: native `<details>` accordion, plus-icon rotates
- **Calculator**: `.calc-panel` chips + result grid, JS in `assets/js/v2-calculator.js`
- **Tabs** (Media): `.tabs` + `.tab-panel[hidden]`, aria-selected driven
- **Reveal**: `.reveal` opacity/translate, IntersectionObserver, gated behind
  `html.js` + `prefers-reduced-motion: no-preference`; content visible without JS

## Motion
Minimal and purposeful (Grab-style): 200ms hovers, 480ms ease-out-quint reveals,
no scroll-driven canvas sequences (V1 frame animation retired per client request).

## z-scale
100 sticky header · 200 mobile menu overlay · 300 modal · 400 WhatsApp float/toast

## Page generation
Shared header/footer chrome lives in `_build_pages.py`; run `python _build_pages.py`
after editing it to regenerate the 8 inner pages. `index.html` is maintained by hand.
