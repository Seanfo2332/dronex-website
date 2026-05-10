# DroneX — Design System

## Color Tokens
```
--navy:      oklch(18% 0.025 240)   /* #151F27 — primary dark surface */
--slate:     oklch(40% 0.035 240)   /* #495F77 — midtone, rules, secondary text */
--sky:       oklch(76% 0.09 240)    /* #9DC1F5 — precision accent, use sparingly */
--cloud:     oklch(93% 0.008 240)   /* #E8ECEF — light surface */
--white:     oklch(99% 0.003 240)   /* #FFFFFF — primary light */
--black:     oklch(5% 0.006 240)    /* #000000 — footer, maximum contrast */

/* Derived */
--navy-1:    oklch(20% 0.025 240)   /* #1B262F — one step lighter than navy */
--rule:      rgba(73,95,119,0.35)
--rule-soft: rgba(73,95,119,0.18)
--sky-glow:  rgba(157,193,245,0.08)
```

## Typography Scale
```
--font-display: "Geist", "Helvetica Neue", sans-serif
--font-mono:    "JetBrains Mono", ui-monospace, monospace

/* Display (hero, section headings) */
--text-hero:    clamp(3.4rem, 8.5vw, 10rem)   /* line-height: 0.88, tracking: -0.04em */
--text-display: clamp(2.2rem, 4.5vw, 5rem)    /* line-height: 0.96, tracking: -0.03em */
--text-title:   clamp(1.6rem, 3vw, 2.8rem)    /* line-height: 1.1,  tracking: -0.02em */

/* Body */
--text-lead:    clamp(15px, 1.1vw, 18px)      /* weight: 300, max-width: 52ch */
--text-body:    16px                            /* weight: 400, line-height: 1.65 */
--text-small:   14px                            /* weight: 300 */

/* Mono labels */
--text-label:   11px                            /* letter-spacing: 0.22em, uppercase */
--text-micro:   10px                            /* letter-spacing: 0.2em, uppercase */
--text-data:    14px                            /* letter-spacing: 0.04em */
```

## Spacing Rhythm
```
--section-pad:  clamp(80px, 9vw, 144px)
--gutter:       clamp(20px, 3.5vw, 60px)
--maxw:         1440px
```

## Elevation / Depth
Dark sections use subtle grid overlays (1px lines at 4% sky opacity) for depth without actual elevation. No box shadows on dark surfaces. On light surfaces: `box-shadow: 0 0 0 1px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)`.

## Motion Tokens
```
--ease-aerial:  cubic-bezier(0.25, 0.46, 0.45, 0.94)  /* primary easing */
--ease-sharp:   cubic-bezier(0.76, 0, 0.24, 1)         /* dramatic transitions */
--dur-fast:     180ms
--dur-mid:      320ms
--dur-reveal:   700ms
--dur-sweep:    8s     /* radar rotation */
--dur-draw:     4s     /* SVG path draw */
```

## Section Rhythm (background sequence)
1. Hero: navy
2. About: white
3. Stats band: navy
4. Pillars: navy (with navy-1 right pillar)
5. Services: navy
6. Entertainment: navy-1
7. Technology: cloud
8. Partners: white
9. CTA: slate
10. Footer: black

## Key Components

### 1px Rule System
Horizontal and vertical 1px rules at `var(--rule)`. Sections divided by rules. Columns separated by rules. Never thicker.

### Mono Label System
Every section has: `[NN] —` section number in sky, `TITLE` in cloud/navy, a flex-1 rule, and a meta note. All in JetBrains Mono 11px 0.22em tracking.

### Operational Data Pattern
Coordinates, flight numbers, spec IDs, waypoint codes — always JetBrains Mono, always `var(--slate)` or `var(--sky)`, always 10-11px.

### Emblem Watermark
The X emblem SVG or PNG at 4-6% opacity, edge-bleed positioned (partially off-canvas). Used in hero (top-right), CTA section (bottom-right). Creates spatial anchor without dominating.

### Reveal Animation
```css
.reveal {
  opacity: 0;
  transform: translateY(28px);
  filter: blur(6px);
  transition:
    opacity var(--dur-reveal) var(--ease-aerial),
    transform var(--dur-reveal) var(--ease-aerial),
    filter var(--dur-reveal) var(--ease-aerial);
  will-change: transform, opacity;
}
.reveal.in {
  opacity: 1;
  transform: none;
  filter: none;
}
```

### Stagger Pattern
Child elements with `.reveal` get `transition-delay` via nth-child or inline `style="--delay: Xms"`.

### Border Radius
Maximum 2px. Aviation precision requires hard corners. Never round.

### Button Anatomy
Primary: sky fill, navy text, 2px radius, 16px vertical / 24px horizontal padding, mono 11px 0.22em tracking, animated arrow (→) grows 18px→26px on hover.
Ghost: slate border, cloud text, same sizing.
Hover transitions: 200ms ease.
