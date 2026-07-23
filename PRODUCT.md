# Drone X Malaysia — Product Context (V2)

> V2 repositioning per "DroneX_Fully_Website_Content_Planning.pdf" (client amendment, July 2026).
> The previous AirAsia-pitch positioning is retired; legacy site preserved as `legacy-v1-index.html`.

## Product Purpose
Drone X Malaysia is an agriculture-first drone services company. The website's job is to
make Malaysian farmers feel confident enough to submit an inquiry for drone spraying and
fertilizing services. Simple, direct, corporate, understandable at a glance.

## Register
brand

## Users (priority order per client)
**① Farmer / plantation owner / landowner** — primary audience, age 30+, practical and
pragmatic. Needs plain language (no technical jargon), trust signals, and an easy path to
inquiry (form, WhatsApp, calculator).

**② Drone pilot** — second layer. Wants a legal, insured platform with steady jobs.

**③ Manufacturer / technical B2B partner** — third layer, kept in footer pages
(Technology & Data, Partners).

## Brand
- Name: Drone X (displayed "Drone X", code "DroneX")
- Logo: black/white/gray X mark (assets/DroneX_BlackOnWhite_* and WhiteOnBlack_*)
- Design direction: **white background, formal, clean, user-friendly** (client mandate)
- Typography: **Montserrat** (client mandate) + Noto Sans SC for Chinese
- Accent: committed agricultural green for CTAs (Grab-inspired), WhatsApp green for the float button
- References named by client: grab.com/my (super corporate, simple color blocks, clear
  CTA, minimal nav) and aerodyne.group (credibility, certifications, data proof)

## Site structure (V2)
Main nav (6): Home / Farmer Solutions / Become a Pilot / About Us / Media / Contact Us
+ standalone CTA "Get a Free Quote" + EN/中文 toggle.
Footer-only pages: Other Solutions, Technology & Data, Partners.
Global: sticky WhatsApp button on every page (bottom-right).

## Language
Fully bilingual EN/中文 via `<span class="en">/<span class="zh">` pairs and
`html[data-lang]` CSS toggle, persisted in localStorage.

## Tone
Practical, reassuring, farmer-first. Short sentences. No jargon. No hype.

## Pending from client (placeholders in code, marked with ⚠/TODO comments)
- Official WhatsApp Business number (currently +60 12-345 6789)
- Calculator coverage rates (currently sample: 20 acres/drone/hour)
- Team & founder bios/photos
- Real case studies (6-8), gallery photos (10+), videos (3-5)
- Inquiry form receiving email (Shirley's team) — form currently client-side only
- Trust stats (acres served, jobs completed, farmers onboard)
- Certification names/documents, company registration line
