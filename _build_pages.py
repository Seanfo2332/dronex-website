# -*- coding: utf-8 -*-
"""Drone X V2 — static page generator for shared header/footer chrome.
Run:  python _build_pages.py
Pages emitted: farmer-solutions, become-a-pilot, about-us, media,
contact-us, other-solutions, technology-data, partners.
index.html is maintained by hand (hero differs)."""
import io, sys

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
# ⚠ Placeholder number (60123456789) — swap in Drone X's real WhatsApp Business
# number before go-live (PDF v3 §A3/A5). Preset message updated per §A5: farmer
# just fills in the blanks instead of writing a message from scratch.
WA_URL = "https://wa.me/60123456789?text=Hi%20Drone%20X%2C%20I%20have%20___%20acres%20of%20___%20%28durian/paddy/oil%20palm%29%20and%20would%20like%20to%20enquire%20about%20spraying%20services.%20/%20%E6%88%91%E6%9C%89___%E8%8B%B1%E4%BA%A9%E7%9A%84___%EF%BC%88%E6%A6%B4%E8%8E%B2/%E7%A8%BB%E7%94%B0/%E6%B2%B9%E6%A3%95%EF%BC%89%EF%BC%8C%E6%83%B3%E4%BA%86%E8%A7%A3%E5%96%B7%E8%8D%AF%E6%9C%8D%E5%8A%A1%E3%80%82"

SHELL = """<!DOCTYPE html>
<html lang="en" data-lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<meta name="description" content="@@DESC@@">
<meta name="keywords" content="@@KEYWORDS@@">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="canonical" href="https://www.dronexmalaysia.com/@@FNAME@@">
<meta property="og:type" content="website">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:image" content="https://www.dronexmalaysia.com/assets/plantation-bg.jpg">
<meta property="og:url" content="https://www.dronexmalaysia.com/@@FNAME@@">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/v2-base.css?v=20260722">
<link rel="stylesheet" href="assets/css/v2-pages.css?v=20260722">
</head>
<body>

<header class="site-header">
  <nav class="nav" aria-label="Main navigation">
    <a class="nav-logo" href="index.html" aria-label="Drone X Malaysia — Home">
      <img src="assets/logo-dark-trim.png" alt="Drone X Malaysia" width="150" height="42">
    </a>
    <ul class="nav-links">
      <li><a href="index.html"@@CUR_home@@><span class="en">Home</span><span class="zh">首页</span></a></li>
      <li><a href="farmer-solutions.html"@@CUR_farmer@@><span class="en">Farmer Solutions</span><span class="zh">农业方案</span></a></li>
      <li><a href="become-a-pilot.html"@@CUR_pilot@@><span class="en">Become a Pilot</span><span class="zh">飞手合作</span></a></li>
      <li><a href="about-us.html"@@CUR_about@@><span class="en">About Us</span><span class="zh">关于我们</span></a></li>
      <li><a href="media.html"@@CUR_media@@><span class="en">Media</span><span class="zh">媒体中心</span></a></li>
      <li><a href="contact-us.html"@@CUR_contact@@><span class="en">Contact Us</span><span class="zh">联系我们</span></a></li>
    </ul>
    <div class="lang-toggle" role="group" aria-label="Language">
      <button type="button" data-lang="en" class="active">EN</button>
      <button type="button" data-lang="zh">中文</button>
    </div>
    <a class="btn btn-primary nav-cta" href="contact-us.html"><span class="en">Get a Free Quote</span><span class="zh">免费询价</span></a>
    <button class="nav-burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </nav>
  <div class="mobile-menu">
    <a href="index.html"><span class="en">Home</span><span class="zh">首页</span></a>
    <a href="farmer-solutions.html"><span class="en">Farmer Solutions</span><span class="zh">农业方案</span></a>
    <a href="become-a-pilot.html"><span class="en">Become a Pilot</span><span class="zh">飞手合作</span></a>
    <a href="about-us.html"><span class="en">About Us</span><span class="zh">关于我们</span></a>
    <a href="media.html"><span class="en">Media</span><span class="zh">媒体中心</span></a>
    <a href="contact-us.html"><span class="en">Contact Us</span><span class="zh">联系我们</span></a>
    <div class="mobile-menu-lang">
      <span class="mobile-menu-lang-label"><span class="en">Language</span><span class="zh">语言</span></span>
      <div class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-lang="en">EN</button>
        <button type="button" data-lang="zh">中文</button>
      </div>
    </div>
    <a class="btn btn-primary" href="contact-us.html"><span class="en">Get a Free Quote</span><span class="zh">免费询价</span></a>
  </div>
</header>

<main>
@@BODY@@
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cta">
      <h2><span class="en">Ready to work with Drone X?</span><span class="zh">准备好与 Drone X 合作了吗？</span></h2>
      <div class="footer-cta-buttons">
        <a class="btn btn-primary" href="@@WA_URL@@" target="_blank" rel="noopener"><span class="en">WhatsApp Free Quote</span><span class="zh">WhatsApp 免费询价</span></a>
        <a class="btn btn-ghost" href="become-a-pilot.html"><span class="en">Become a Pilot</span><span class="zh">加入飞手网络</span></a>
        <a class="btn btn-ghost" href="partners.html"><span class="en">Partner With Drone X</span><span class="zh">商业合作洽谈</span></a>
      </div>
    </div>
    <div class="footer-grid">
      <div>
        <h3><span class="en">Quick Links</span><span class="zh">快速连结</span></h3>
        <ul>
          <li><a href="farmer-solutions.html"><span class="en">Farmer Solutions</span><span class="zh">农业方案</span></a></li>
          <li><a href="become-a-pilot.html"><span class="en">Become a Pilot</span><span class="zh">飞手合作</span></a></li>
          <li><a href="about-us.html"><span class="en">About Us</span><span class="zh">关于我们</span></a></li>
          <li><a href="media.html"><span class="en">Media</span><span class="zh">媒体中心</span></a></li>
          <li><a href="contact-us.html"><span class="en">Contact Us</span><span class="zh">联系我们</span></a></li>
        </ul>
      </div>
      <div>
        <h3><span class="en">More Solutions</span><span class="zh">更多方案</span></h3>
        <ul>
          <li><a href="other-solutions.html"><span class="en">Other Solutions</span><span class="zh">其他领域方案</span></a></li>
          <li><a href="technology-data.html"><span class="en">Technology &amp; Data</span><span class="zh">技术与数据</span></a></li>
          <li><a href="partners.html"><span class="en">Partners</span><span class="zh">合作伙伴</span></a></li>
        </ul>
      </div>
      <div>
        <h3><span class="en">Contact</span><span class="zh">联系方式</span></h3>
        <ul>
          <!-- Phone number removed until a real office/WhatsApp Business number is confirmed (PDF v3 §A3) -->
          <li><a href="@@WA_URL@@" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:hello@dronexmalaysia.com">hello@dronexmalaysia.com</a></li>
          <li><span style="font-size:var(--text-small)"><span class="en">Kuala Lumpur, Malaysia</span><span class="zh">马来西亚吉隆坡</span></span></li>
        </ul>
      </div>
      <div>
        <h3><span class="en">Follow Us</span><span class="zh">社交媒体</span></h3>
        <!-- TikTok/YouTube icons removed until real links exist (PDF v3 launch checklist) -->
        <ul>
          <li><a href="https://www.facebook.com/profile.php?id=61589607842133" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="https://www.instagram.com/dronexmalaysia?igsh=MXdubThoaWRsMXA0bw==" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="https://www.linkedin.com/company/drone-x-mayalsia/about/" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span class="footer-logo"><img src="assets/logo-light-trim.png" alt="Drone X" width="122" height="34"></span>
      <span>© <span data-year>2026</span> Drone X Malaysia. <span class="en">All rights reserved.</span><span class="zh">版权所有。</span></span>
      <span class="lang-toggle" role="group" aria-label="Language">
        <button type="button" data-lang="en" class="active">EN</button>
        <button type="button" data-lang="zh">中文</button>
      </span>
    </div>
  </div>
</footer>

<!-- ⚠ Placeholder WhatsApp number — swap in the real business number before go-live (PDF v3 §A3) -->
<a class="wa-float" target="_blank" rel="noopener" href="@@WA_URL@@" aria-label="Chat with us on WhatsApp">
  <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.2 1.6 6L4 29l8.2-1.5c1.2.5 2.5.8 3.8.8 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.2 0-2.4-.3-3.5-.8l-.6-.3-4.9.9 1-4.7-.4-.6c-1-1.6-1.5-3.4-1.5-5.3 0-5.5 4.4-9.9 9.9-9.9s9.9 4.4 9.9 9.9-4.4 9.8-9.9 9.8zm5.4-7.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.2-.3-.2-.6-.4z"/></svg>
  <span class="wa-label"><span class="en">Chat with Us</span><span class="zh">联系我们</span></span>
</a>

<script src="assets/js/v2-main.js?v=20260722" defer></script>
@@EXTRA_SCRIPTS@@
</body>
</html>
"""

def bi(en, zh):
    return '<span class="en">%s</span><span class="zh">%s</span>' % (en, zh)

# Per-page header media (PDF follow-up: "put images related to content at the
# start of every page" — farmer-solutions already had its own hero video, so
# it's excluded). Reuses real project assets rather than stock/generic art.
def hero_image_media(src, alt, w, h):
    return ('<div class="hero-media"><img src="%s" alt="%s" loading="eager" '
            'fetchpriority="high" width="%d" height="%d"></div>') % (src, alt, w, h)

def hero_video_media(src, poster, alt, w, h):
    return ('<div class="hero-media">'
            '<video autoplay muted loop playsinline preload="metadata" poster="%s" aria-hidden="true">'
            '<source src="%s" type="video/mp4"></video>'
            '<img src="%s" alt="%s" loading="eager" fetchpriority="high" width="%d" height="%d">'
            '</div>') % (poster, src, poster, alt, w, h)

def page(fname, nav_key, title, desc, keywords, body, extra_scripts=""):
    html = (SHELL
        .replace("@@TITLE@@", title)
        .replace("@@DESC@@", desc)
        .replace("@@BODY@@", body)
        .replace("@@FNAME@@", fname)
        .replace("@@WA_URL@@", WA_URL)
        .replace("@@EXTRA_SCRIPTS@@", extra_scripts)
        .replace("@@KEYWORDS@@", keywords))
    for key in ["home", "farmer", "pilot", "about", "media", "contact"]:
        html = html.replace("@@CUR_%s@@" % key,
                            ' aria-current="page"' if key == nav_key else "")
    with io.open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname)

# ════════════════ FARMER SOLUTIONS ════════════════
FAQS = [
    ("Is drone spraying safe? Will it harm crops, animals or people nearby?",
     "无人机喷药安全吗？会不会伤到作物、动物或附近的人？",
     "Yes. Every job is flown by a licensed pilot on a pre-planned route with buffer zones around houses, animals and waterways. Spray volume is controlled precisely, and operations are insured.",
     "安全。每次作业由持牌飞手按预先规划的路线执行，房屋、动物与水源周围设有缓冲区。喷洒量精准控制，作业也有保险保障。"),
    ("How is the cost calculated? By land area or per visit?",
     "费用怎么计算？是按农地面积收费，还是按次数？",
     "Pricing is mainly based on land area (per acre or hectare) and the type of service. After a free site consultation we give you a fixed written quote, with no hidden charges.",
     "费用主要按农地面积（英亩或公顷）与服务类型计算。免费勘察后我们会提供固定的书面报价，没有隐藏收费。"),
    ("How big must my land be? Is there a minimum size?",
     "我的地要多大才可以用无人机服务？有没有最低面积要求？",
     "There is no strict minimum. Smaller plots can be grouped with nearby jobs to keep costs reasonable. Tell us your land size and we will suggest the most economical arrangement.",
     "没有严格的最低面积。较小的地块可以与附近的作业一起安排，以控制成本。告诉我们您的面积，我们会建议最省钱的安排。"),
    ("Which pesticides or fertilizers can be sprayed? Can I use my own?",
     "无人机可以喷哪些农药／肥料？我自己买的农药可以用吗？",
     "Most common liquid pesticides and fertilizers are suitable. You are welcome to supply your own; our team will first check that it is safe and effective for drone application.",
     "大部分常见的液态农药与肥料都适用。您可以使用自己购买的农药，我们的团队会先确认它适合无人机喷洒且安全有效。"),
    ("How soon can you schedule my land?",
     "大概多久可以安排到我的地作业？",
     "Typically within about one week of confirming your quote, depending on season and weather. Urgent jobs can often be arranged sooner. Contact us early during peak seasons.",
     "确认报价后通常约一周内可安排，视季节与天气而定。紧急作业通常可更快安排；旺季建议提早联系。"),
    ("How long does one job take?",
     "一次作业大概需要多长时间才能完成？",
     "A drone covers large areas quickly. As a guide, a 50-acre plot is usually completed within a few hours. Try the calculator below for an estimate based on your own land.",
     "无人机作业速度很快。以 50 英亩为例，通常几个小时内即可完成。可使用下方计算器根据您的农地估算时间。"),
    ("Does drone spraying waste more chemicals than manual spraying?",
     "无人机喷洒会不会比人工喷洒浪费更多农药，还是更省？",
     "It usually saves chemicals. Drones spray evenly at a controlled rate, so most farmers use less than manual spraying while getting better coverage.",
     "通常更省。无人机以受控速率均匀喷洒，多数农夫的用药量比人工喷洒更少，覆盖却更全面。"),
    ("What if it rains or the weather is bad on the day?",
     "如果作业当天下雨／天气不好怎么办？会重新安排吗？",
     "We monitor the weather before every job. If conditions are unsafe or the spray would wash off, we reschedule to the next suitable day at no extra charge.",
     "每次作业前我们都会监测天气。如天气不适合作业或药剂会被雨水冲走，我们会免费改期到下一个合适的日子。"),
    ("Do I need to be present? What should I prepare?",
     "我需要在场吗？需要准备什么（水源、清空农地之类）？",
     "You or a representative should join the first site visit. On spray day we mainly need access to a water source and the area cleared of people and livestock. We will guide you through it.",
     "首次勘察时建议您或代表在场。作业当天主要需要水源，以及确保作业区没有人员和牲畜。我们会一步步指导您准备。"),
    ("My land is hilly or uneven. Can drones still work?",
     "我的地是山坡地／地形不平整，也可以用无人机吗？",
     "Yes. Drones follow the terrain automatically and handle slopes and uneven ground far more easily than manual crews or tractors. Hillside orchards are a common job for us.",
     "可以。无人机会自动跟随地形飞行，处理山坡与不平整地面比人工或拖拉机容易得多。山坡果园是我们常见的作业类型。"),
    ("Are your pilots licensed? Is there insurance if something goes wrong?",
     "你们的飞手有正式牌照吗？作业出问题有保险赔偿吗？",
     "All our pilots hold the required certifications and operate on a compliant platform. Every job is covered by operational insurance, so you are protected if anything goes wrong.",
     "我们所有飞手都持有所需执照，并在合规平台上作业。每次作业都有作业保险，如有意外您都受到保障。"),
    ("I'm not sure how many drones or how much service I need. Can I get an estimate first?",
     "我不确定我的地需要几架无人机／多少服务，可以先估算吗？",
     "Yes, that is exactly what the calculator below is for. Enter your land size and needs to get an instant estimate, then request an exact quote with one click.",
     "可以，下方的计算器正是为此而设。输入农地面积与需求即可立即获得估算，再一键获取精准报价。"),
]

faq_html = "\n".join(
    '<details class="faq-item"%s>\n  <summary>%s</summary>\n  <div class="faq-body"><p>%s</p></div>\n</details>'
    % (" open" if i == 0 else "", bi(q_en, q_zh), bi(a_en, a_zh))
    for i, (q_en, q_zh, a_en, a_zh) in enumerate(FAQS))

farmer_body = """
<section class="page-hero-video" aria-labelledby="fs-heading">
  <div class="hero-media">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/farmer-hero-poster.jpg" aria-hidden="true">
      <source src="assets/farmer-hero.mp4" type="video/mp4">
    </video>
    <img src="assets/farmer-hero-poster.jpg" alt="Agriculture drone spraying a durian orchard and paddy field in Malaysia" loading="eager" fetchpriority="high" width="1280" height="720">
  </div>
  <div class="wrap">
    <h1 id="fs-heading">""" + bi("Agriculture Drone Spraying Solutions for Farmers", "农业无人机喷药服务") + """</h1>
    <p class="lead">""" + bi(
        "Drone X provides drone spraying and fertilizing for farmers, plantation owners and agricultural operators: faster, more even coverage of large fields with less manpower, lower cost and safer operations.",
        "Drone X 为农夫、园主与农业运营商提供无人机喷药与施肥服务，协助更快速、均匀地覆盖大面积农地，减少人力与时间成本，同时提高作业安全性。") + """</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href='""" + WA_URL + """' target="_blank" rel="noopener">""" + bi("WhatsApp Free Quote", "WhatsApp 免费询价") + """</a>
      <a class="btn btn-ghost" href="contact-us.html">""" + bi("Get a Free Quote for Your Farm", "免费为您的农地报价") + """</a>
      <a class="btn btn-ghost" href="#calculator">""" + bi("Try the Spraying Calculator", "试用喷洒需求计算器") + """</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="fs-benefits">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="fs-benefits">""" + bi("Benefits", "服务好处") + """</h2></div>
    <div class="two-col reveal">
      <ul class="offer-list stagger">
        <li>""" + CHECK + """<span><b>""" + bi("Save cost", "省成本") + """</b><span>""" + bi("Less labour and less chemical waste.", "减少人工与农药浪费。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Save manpower", "省人力") + """</b><span>""" + bi("No big work crews, lower physical risk.", "无需大量人手，降低体力劳动风险。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Save time", "省时间") + """</b><span>""" + bi("Large fields finished in a short time.", "大面积农地可在短时间内完成。") + """</span></span></li>
      </ul>
      <ul class="offer-list stagger">
        <li>""" + CHECK + """<span><b>""" + bi("More precise", "更精准") + """</b><span>""" + bi("Even spraying, less waste, better yield.", "均匀喷洒，减少浪费，提高作物产量。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Safer", "更安全") + """</b><span>""" + bi("Licensed pilots and insured operations.", "飞手持牌操作，作业有保险保障。") + """</span></span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section on-surface" aria-labelledby="fs-suitable">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="fs-suitable">""" + bi("Suitable For", "适合对象") + """</h2></div>
    <div class="chip-row reveal">
      <span class="chip" aria-pressed="true">""" + bi("Farms", "农场") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Plantations", "种植园") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Agricultural Operators", "农业运营商") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Landowners", "地主") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Farming Cooperatives", "农业合作社") + """</span>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="fs-how">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="fs-how">""" + bi("How It Works", "服务流程") + """</h2></div>
    <div class="steps stagger">
      <article class="step"><h3>""" + bi("Submit Inquiry", "提交询价") + """</h3><p>""" + bi("Fill in a simple form with your land size and needs.", "填写简单表格，说明农地面积与需求。") + """</p></article>
      <article class="step"><h3>""" + bi("Free Consultation", "免费勘察") + """</h3><p>""" + bi("Our team assesses your land condition, free of charge.", "团队免费评估农地状况。") + """</p></article>
      <article class="step"><h3>""" + bi("Custom Plan", "制定方案") + """</h3><p>""" + bi("A professional plan for routes and chemical volume.", "专业团队规划路线与用量。") + """</p></article>
      <article class="step"><h3>""" + bi("Execution &amp; Report", "执行与报告") + """</h3><p>""" + bi("We complete the job and hand you a work report.", "完成作业后提供工作报告。") + """</p></article>
    </div>
  </div>
</section>

<section class="section on-surface" id="calculator" aria-labelledby="calc-heading">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="calc-heading">""" + bi("Drone Spraying Calculator", "无人机喷洒需求计算器") + """</h2>
      <p class="lead">""" + bi("Enter your land details and get an instant estimate of the service you need.", "输入农地资料，立即估算所需的服务与无人机数量。") + """</p>
    </div>
    <div id="spray-calculator" class="calc-panel reveal">
      <div class="calc-step">
        <label for="calc-area">""" + bi("Step 1 — Land area", "步骤 1 — 农地面积") + """</label>
        <div class="calc-area-row">
          <input type="number" id="calc-area" min="0" step="any" inputmode="decimal" placeholder="e.g. 50">
          <div class="chip-row" data-group="unit">
            <button type="button" class="chip" data-value="acre" aria-pressed="true">""" + bi("Acre", "英亩") + """</button>
            <button type="button" class="chip" data-value="hectare" aria-pressed="false">""" + bi("Hectare", "公顷") + """</button>
            <button type="button" class="chip" data-value="sqft" aria-pressed="false">""" + bi("Square Feet", "平方英尺") + """</button>
          </div>
        </div>
      </div>
      <div class="calc-step">
        <span class="calc-label">""" + bi("Step 2 — Service purpose", "步骤 2 — 服务用途") + """</span>
        <div class="chip-row" data-group="purpose">
          <button type="button" class="chip" data-value="spraying" aria-pressed="true">""" + bi("Pesticide Spraying", "农药喷洒") + """</button>
          <button type="button" class="chip" data-value="fertilizing" aria-pressed="false">""" + bi("Fertilizing", "施肥") + """</button>
          <button type="button" class="chip" data-value="both" aria-pressed="false">""" + bi("Both", "两者都要") + """</button>
        </div>
      </div>
      <div class="calc-step">
        <span class="calc-label">""" + bi("Step 3 — Crop type (optional)", "步骤 3 — 农地类型（可选）") + """</span>
        <div class="chip-row" data-group="crop">
          <button type="button" class="chip" data-value="palm" aria-pressed="false">""" + bi("Oil Palm", "棕榈油") + """</button>
          <button type="button" class="chip" data-value="paddy" aria-pressed="false">""" + bi("Paddy", "水稻") + """</button>
          <button type="button" class="chip" data-value="durian" aria-pressed="false">""" + bi("Durian", "榴莲") + """</button>
          <button type="button" class="chip" data-value="other" aria-pressed="false">""" + bi("Other", "其他") + """</button>
        </div>
      </div>
      <div class="calc-result" id="calc-result" hidden>
        <div class="calc-result-grid">
          <div class="calc-result-item"><span>""" + bi("Recommended service", "建议服务类型") + """</span><b id="res-service">—</b></div>
          <div class="calc-result-item"><span>""" + bi("Estimated drones needed", "预估所需无人机数量") + """</span><b id="res-drones">—</b></div>
          <div class="calc-result-item"><span>""" + bi("Estimated completion time", "预估完成时间") + """</span><b id="res-time">—</b></div>
        </div>
        <a class="btn btn-primary" id="calc-quote-link" href="contact-us.html#inquiry">""" + bi("Get My Exact Quote", "获取精准报价") + """</a>
        <p class="calc-note" style="margin-top:1rem">""" + bi(
            "Estimates use sample coverage rates and will be calibrated with official Drone X operating data before launch.",
            "估算目前采用示例覆盖率，正式上线前将以 Drone X 官方作业数据校准。") + """</p>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="fs-faq">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="fs-faq">""" + bi("Frequently Asked Questions", "常见问题") + """</h2></div>
    <!-- Answers are suggested copy for review; final wording adjustable by the group -->
    <div class="faq-list reveal">
""" + faq_html + """
    </div>
  </div>
</section>

<section class="section on-surface" aria-labelledby="fs-cases">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="fs-cases">""" + bi("Real Results", "实际案例") + """</h2></div>
    <!-- Verified case studies pending from the group; placeholder keeps this honest
         instead of shipping fabricated locations/results (PDF v3 §A3). -->
    <div class="media-placeholder reveal" style="max-width:760px">
      <p style="margin:0">""" + bi(
          "Verified case studies from real Drone X jobs are being prepared and will appear here shortly.",
          "真实作业案例整理中，即将在此上线。") + """</p>
    </div>
    <div class="reveal" style="margin-top:1.2rem;display:flex;flex-wrap:wrap;gap:0.7rem">
      <a class="btn btn-ghost" href="media.html">""" + bi("View More in Media Centre", "前往媒体中心查看更多案例") + """</a>
      <a class="btn btn-primary" href='""" + WA_URL + """' target="_blank" rel="noopener">""" + bi("WhatsApp Us", "WhatsApp 联系我们") + """</a>
    </div>
  </div>
</section>
"""

page("farmer-solutions.html", "farmer",
     "Agriculture Drone Spraying Malaysia | Drone X",
     "Save cost, manpower and time with Drone X's licensed agriculture drone spraying and fertilizing service for farms and plantations across Malaysia.",
     "agriculture drone Malaysia, drone fertilizing Malaysia, drone spraying Malaysia, plantation drone service Malaysia, smart farming drone solution, 无人机喷药马来西亚, 农业无人机服务, drone spraying calculator Malaysia, 无人机喷洒计算器",
     farmer_body,
     '<script src="assets/js/v2-calculator.js" defer></script>')

# ════════════════ BECOME A PILOT ════════════════
pilot_body = """
<section class="page-hero-video" aria-labelledby="bp-heading">
  """ + hero_video_media("assets/commercial-bg.mp4", "assets/commercial-bg-poster.jpg", "Close-up of a Drone X aircraft in flight", 1280, 720) + """
  <div class="wrap">
    <h1 id="bp-heading">""" + bi("Become a Drone X Certified Pilot", "加入 Drone X 飞手合作网络") + """</h1>
    <p class="lead">""" + bi(
        "Drone X welcomes licensed pilots to join our network and serve farmers and businesses across Malaysia. We provide a fully compliant platform, insurance coverage and professional back-end support, so you can focus on flying.",
        "Drone X 欢迎持牌飞手加入我们的合作网络，共同服务马来西亚各地的农夫与企业客户。我们提供合法合规的作业平台、保险保障与专业团队支持，让飞手能专注于飞行作业本身。") + """</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="contact-us.html?service=pilot#inquiry">""" + bi("Apply to Join", "立即申请加入") + """</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="bp-offer">
  <div class="wrap two-col">
    <div class="reveal">
      <h2 id="bp-offer">""" + bi("What We Offer", "我们提供") + """</h2>
      <ul class="offer-list stagger">
        <li>""" + CHECK + """<span><b>""" + bi("Licensed &amp; Compliant Platform", "合法合规的作业平台") + """</b><span>""" + bi("Fly under an approved, regulation-ready operation.", "在获批准、符合法规的平台下作业。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Insurance Coverage", "作业保险保障") + """</b><span>""" + bi("Every job flown under operational insurance.", "每次作业都有作业保险保障。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Steady Job Opportunities", "稳定的项目来源") + """</b><span>""" + bi("A consistent pipeline of agriculture and commercial jobs.", "持续稳定的农业与商业项目来源。") + """</span></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Professional Back-End Support", "专业团队支持") + """</b><span>""" + bi("Planning, approvals and client liaison handled for you.", "规划、审批与客户对接由团队处理。") + """</span></span></li>
      </ul>
    </div>
    <div class="reveal">
      <h2>""" + bi("Requirements", "加入条件") + """</h2>
      <!-- Detailed criteria pending from the group (PDF §5) -->
      <ul class="offer-list stagger">
        <li>""" + CHECK + """<span><b>""" + bi("Valid drone operating licence", "持有相关无人机操作执照") + """</b></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Meets regulatory operating requirements", "符合监管单位的操作要求") + """</b></span></li>
        <li>""" + CHECK + """<span><b>""" + bi("Agriculture spraying experience preferred", "农业喷洒相关经验（优先）") + """</b></span></li>
      </ul>
      <p class="calc-note" style="margin-top:1rem">""" + bi("Full joining criteria will be confirmed by the Drone X team.", "详细加入条件以 Drone X 团队最终确认为准。") + """</p>
      <a class="btn btn-primary" style="margin-top:0.6rem" href="contact-us.html?service=pilot#inquiry">""" + bi("Apply to Join", "立即申请加入") + """</a>
    </div>
  </div>
</section>
"""

page("become-a-pilot.html", "pilot",
     "Become a Drone Pilot | Join Drone X Malaysia",
     "Join Drone X's licensed pilot network — access steady agriculture drone spraying jobs with insurance coverage and professional support.",
     "drone pilot Malaysia, drone pilot job Malaysia, agriculture drone pilot, 无人机飞手招募, drone pilot partnership Malaysia",
     pilot_body)

# ════════════════ ABOUT US ════════════════
# Reordered per PDF v3 §A7: farmer-first — who we are (farming roots) → core
# team → licenses — before the more corporate Vision/Mission content.
about_body = """
<section class="page-hero-video" aria-labelledby="au-heading">
  """ + hero_image_media("assets/about-brand.jpg", "Close-up of a Drone X aircraft propeller in motion with the Drone X wordmark", 1327, 746) + """
  <div class="wrap">
    <h1 id="au-heading">""" + bi("About Drone X Malaysia", "关于 Drone X Malaysia") + """</h1>
    <p class="lead">""" + bi(
        "Drone X Malaysia is a drone technology company with agriculture at its core, extending into industrial and public sector applications. Through compliant operations, a professional team and proven technology, we help Malaysian farmers and businesses work more efficiently.",
        "Drone X Malaysia 是一家以农业为核心、兼顾工业与公共部门应用的无人机科技公司，致力以合法合规、专业团队与先进技术，协助马来西亚农夫与企业提升作业效率。") + """</p>
  </div>
</section>

<section class="section" aria-labelledby="au-team">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="au-team">""" + bi("Drone X Core Team", "Drone X 核心成员") + """</h2>
      <p class="lead">""" + bi(
          "All three core members are durian orchard owners with hands-on farming experience — they understand what farmers actually need.",
          "三位核心成员皆为榴莲园主，深耕农业一线，深知农夫的实际需求。") + """</p>
    </div>
    <!-- Real photos found in assets/team/ (william.jpg, hoi-gor.jpg, datuk-low.jpg) —
         role assignment below is a best guess pending confirmation from the group;
         swap the labels if the mapping is wrong. -->
    <div class="team-grid stagger">
      <div class="team-slot"><div class="ph"><img src="assets/team/datuk-low.jpg" alt="Datuk Low, Drone X Malaysia Founder" loading="lazy" width="400" height="400"></div><b>Datuk Low</b><span class="team-role">""" + bi("Founder", "创办人") + """</span><span>""" + bi("Durian orchard owner.", "榴莲园主。") + """</span></div>
      <div class="team-slot"><div class="ph"><img src="assets/team/william.jpg" alt="William, Drone X Malaysia Head of Operations" loading="lazy" width="400" height="400"></div><b>William</b><span class="team-role">""" + bi("Head of Operations", "运营主管") + """</span><span>""" + bi("Durian orchard owner.", "榴莲园主。") + """</span></div>
      <div class="team-slot"><div class="ph"><img src="assets/team/hoi-gor.jpg" alt="Hoi Gor, Drone X Malaysia Chief Pilot" loading="lazy" width="400" height="400"></div><b>Hoi Gor</b><span class="team-role">""" + bi("Chief Pilot", "首席飞手") + """</span><span>""" + bi("Durian orchard owner.", "榴莲园主。") + """</span></div>
    </div>
  </div>
</section>

<section class="section on-surface" aria-labelledby="au-cert">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="au-cert">""" + bi("Licenses &amp; Certifications", "认证与执照") + """</h2></div>
    <ul class="cred-list reveal" style="max-width:640px">
      <li>""" + CHECK + """<span>""" + bi("Licensed &amp; certified drone pilots", "持牌认证飞手") + """</span></li>
      <li>""" + CHECK + """<span>""" + bi("CAAM-compliant operating platform", "符合 CAAM 规范的作业平台") + """</span></li>
      <li>""" + CHECK + """<span>""" + bi("Operational insurance coverage", "作业保险保障") + """</span></li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="au-vm">
  <div class="wrap two-col">
    <div class="reveal">
      <h2 id="au-vm">""" + bi("Vision", "愿景") + """</h2>
      <p class="lead">""" + bi(
          "To be Malaysia's most trusted drone solutions company, starting from agriculture and extending into industrial and public applications.",
          "成为马来西亚最值得信赖的无人机解决方案公司，从农业出发，延伸至工业与公共领域应用。") + """</p>
    </div>
    <div class="reveal">
      <h2>""" + bi("Mission", "使命") + """</h2>
      <p class="lead">""" + bi(
          "To help farmers and businesses raise efficiency, lower cost and command aerial data through safe, practical and innovative drone solutions.",
          "以安全、实用与创新的无人机方案，协助农夫与企业提升效率、降低成本、掌握空中数据。") + """</p>
    </div>
  </div>
</section>
"""

page("about-us.html", "about",
     "About Us | Drone X Malaysia",
     "Drone X Malaysia is an agriculture-first drone technology company helping Malaysian farmers and businesses work faster and safer with licensed, insured drone operations.",
     "Drone X Malaysia, drone company Malaysia, 无人机公司马来西亚, agriculture drone company",
     about_body)

# ════════════════ MEDIA CENTRE ════════════════
gallery_imgs = chr(10).join(
    '<figure><img src="%s" alt="%s" loading="lazy" width="1200" height="800"><figcaption>%s</figcaption></figure>'
    % (src, alt, bi(cap_en, cap_zh))
    for src, alt, cap_en, cap_zh in [
        ("assets/crops/paddy-aerial.jpg", "Aerial view of green paddy fields from the drone", "Paddy fields from the drone's view", "无人机视角下的稻田"),
        ("assets/crops/palm-road.jpg", "Oil palm plantation with red laterite road", "Oil palm estate operation site", "油棕园作业现场"),
        ("assets/crops/durian.jpg", "Durian fruits ripening on the tree", "Durian orchard spraying job", "榴莲园喷洒作业"),
        ("assets/plantation-bg.jpg", "Drone flying over a palm plantation at sunrise", "Morning flight over the plantation", "清晨种植园上空飞行"),
        ("drone-frames/ezgif-frame-090.jpg", "Drone X drone during a field operation", "Drone in operation", "无人机作业实拍"),
        ("drone-frames/ezgif-frame-150.jpg", "Drone returning after a completed job", "Job completed, returning home", "作业完成返航"),
    ])

media_body = """
<section class="page-hero-video" aria-labelledby="md-heading">
  """ + hero_image_media("assets/plantation-bg.jpg", "Drone X agriculture drone flying over a Malaysian palm plantation at sunrise", 1448, 1086) + """
  <div class="wrap">
    <h1 id="md-heading">""" + bi("Media Centre — See Drone X in Action", "媒体中心 — 看见 Drone X 的真实作业成果") + """</h1>
    <p class="lead">""" + bi(
        "Real photos, videos, case studies and news from our operations across Malaysia.",
        "来自马来西亚各地作业现场的真实照片、影片、案例与新闻。") + """</p>
  </div>
</section>

<section class="section" aria-label="Media categories">
  <div class="wrap">
    <h2 class="sr-only">Media Categories</h2>
    <div class="tabs" role="tablist">
      <button class="tab-btn" role="tab" aria-selected="true"  aria-controls="tab-gallery" id="tabbtn-gallery">""" + bi("Gallery", "相册") + """</button>
      <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-video" id="tabbtn-video">""" + bi("Video", "影片") + """</button>
      <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-cases" id="tabbtn-cases">""" + bi("Case Studies", "案例分享") + """</button>
      <button class="tab-btn" role="tab" aria-selected="false" aria-controls="tab-news" id="tabbtn-news">""" + bi("News", "新闻动态") + """</button>
    </div>

    <div class="tab-panel" id="tab-gallery" role="tabpanel">
      <div class="gallery-grid stagger">
""" + gallery_imgs + """
      </div>
      <p class="calc-note" style="margin-top:1.2rem">""" + bi(
          "More real operation photos will be added as the group provides them (10+ planned for launch).",
          "更多真实作业照片将随集团提供陆续新增（上线首批规划 10 张以上）。") + """</p>
    </div>

    <div class="tab-panel" id="tab-video" role="tabpanel" hidden>
      <div class="media-placeholder">
        <p style="margin:0">""" + bi(
            "Operation clips, farmer testimonials and drone show highlights are being prepared (3-5 short videos planned for launch, each under 1 minute).",
            "作业实录、客户见证与无人机表演花絮影片筹备中（上线首批规划 3-5 支，每支 1 分钟内）。") + """</p>
      </div>
    </div>

    <div class="tab-panel" id="tab-cases" role="tabpanel" hidden>
      <span id="case-studies"></span>
      <!-- Verified case studies pending from the group; placeholder keeps this honest
           instead of shipping fabricated client/location/result details (PDF v3 §A3). -->
      <div class="media-placeholder">
        <p style="margin:0">""" + bi(
            "Verified case studies — client background, challenge, solution and real results — are being prepared and will be published here as the group confirms details (6-8 planned for launch).",
            "详细版真实案例（含客户背景、挑战、方案与成果）整理中，将随集团确认后发布（上线首批规划 6-8 则）。") + """</p>
      </div>
      <a class="btn btn-primary" style="margin-top:1.2rem" href="contact-us.html">""" + bi("Get a Free Quote for Your Farm", "免费为您的农地报价") + """</a>
    </div>

    <div class="tab-panel" id="tab-news" role="tabpanel" hidden>
      <div class="media-placeholder">
        <p style="margin:0">""" + bi(
            "Company news, events and media coverage will be posted here (updated monthly).",
            "公司新闻、活动动态与媒体报导将在此发布（每月更新）。") + """</p>
      </div>
    </div>
  </div>
</section>
"""

media_hash_script = """<script>
/* Open the Case Studies tab when arriving via #case-studies.
   Runs on DOMContentLoaded so the deferred v2-main.js tab handler exists. */
document.addEventListener("DOMContentLoaded", function () {
  if (location.hash === "#case-studies") {
    var btn = document.getElementById("tabbtn-cases");
    if (btn) btn.click();
  }
});
</script>"""

page("media.html", "media",
     "Media Centre | Drone X Malaysia Case Studies & Videos",
     "Explore real farm spraying results, videos and news from Drone X Malaysia — see how our licensed drone pilots help farmers save time and cost.",
     "drone spraying case study Malaysia, 无人机喷洒案例分享, Drone X gallery, Drone X video, 农业无人机成功案例, drone company news Malaysia",
     media_body, media_hash_script)

# ════════════════ CONTACT US ════════════════
contact_body = """
<section class="page-hero-video" aria-labelledby="ct-heading">
  """ + hero_image_media("assets/crops/palm-road.jpg", "Oil palm plantation with a red laterite road under blue sky", 1200, 800) + """
  <div class="wrap">
    <h1 id="ct-heading">""" + bi("Contact Us", "联系我们") + """</h1>
    <p class="lead">""" + bi(
        "Tell us about your land or project and our team will reply within 1-2 working days. Prefer to talk now? WhatsApp us directly.",
        "告诉我们您的农地或项目需求，团队将在 1-2 个工作天内回复。想直接沟通？可立即 WhatsApp 联系。") + """</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href='""" + WA_URL + """' target="_blank" rel="noopener">""" + bi("WhatsApp Us", "WhatsApp 联系我们") + """</a>
    </div>
  </div>
</section>

<section class="section" id="inquiry" aria-labelledby="ct-form-heading">
  <div class="wrap contact-layout">
    <div>
      <h2 id="ct-form-heading">""" + bi("Inquiry Form", "询问表格") + """</h2>
      <!-- Final field list & receiving inbox pending from Shirley's team (PDF §10) -->
      <form id="inquiry-form" class="form-grid" novalidate>
        <div class="form-field">
          <label for="f-name">""" + bi("Name", "姓名") + """</label>
          <input id="f-name" name="name" type="text" autocomplete="name" required>
          <span class="err">""" + bi("Please enter your name.", "请输入姓名。") + """</span>
        </div>
        <div class="form-field">
          <label for="f-phone">""" + bi("Contact Number", "电话号码") + """</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required>
          <span class="err">""" + bi("Please enter a valid phone number.", "请输入有效的电话号码。") + """</span>
        </div>
        <div class="form-field">
          <label for="f-email">""" + bi("Email", "电邮") + """</label>
          <input id="f-email" name="email" type="email" autocomplete="email" required>
          <span class="err">""" + bi("Please enter your email.", "请输入电邮。") + """</span>
        </div>
        <div class="form-field">
          <label for="f-location">""" + bi("Location / Farm Location", "地点／农地地点") + """</label>
          <input id="f-location" name="location" type="text" required>
          <span class="err">""" + bi("Please enter a location.", "请输入地点。") + """</span>
        </div>
        <div class="form-field">
          <label for="f-service">""" + bi("Service Interested In", "我感兴趣的服务") + """</label>
          <select id="f-service" name="service" required>
            <option value="spraying">""" + bi("Drone Spraying Service (Farmer)", "农药喷洒服务（农夫）") + """</option>
            <option value="pilot">""" + bi("Become a Pilot", "加入飞手") + """</option>
            <option value="mapping">""" + bi("Aerial Mapping", "航拍测绘") + """</option>
            <option value="cleaning">""" + bi("Building / Solar Cleaning", "建筑/太阳能清洗") + """</option>
            <option value="public">""" + bi("Public Sector Support", "公共部门支援") + """</option>
            <option value="show">""" + bi("Drone Entertainment", "无人机表演") + """</option>
            <option value="other">""" + bi("Other", "其他") + """</option>
          </select>
        </div>
        <div class="form-field">
          <label for="f-message">""" + bi("Message (optional)", "留言（选填）") + """</label>
          <textarea id="f-message" name="message" rows="4"></textarea>
        </div>
        <div>
          <button type="submit" class="btn btn-primary">""" + bi("Submit Inquiry", "提交询问") + """</button>
        </div>
      </form>
      <div id="form-thanks" class="form-thanks" hidden>
        <p style="margin:0">""" + bi(
            "Thank you for your inquiry. Our team will contact you within 1-2 working days.",
            "感谢您的查询，我们团队将在 1-2 个工作天内与您联系。") + """</p>
      </div>
    </div>
    <aside class="contact-side">
      <h2>""" + bi("Reach Us Directly", "直接联系") + """</h2>
      <div class="contact-quick">
        <!-- Phone number removed until a real office/WhatsApp Business number is confirmed (PDF v3 §A3) -->
        <span class="contact-line">""" + CHECK + """<a href='""" + WA_URL + """' target="_blank" rel="noopener">WhatsApp """ + bi("Chat", "传讯") + """</a></span>
        <span class="contact-line">""" + CHECK + """<a href="mailto:hello@dronexmalaysia.com">hello@dronexmalaysia.com</a></span>
        <span class="contact-line">""" + CHECK + """<span>""" + bi("Kuala Lumpur, Malaysia (full address to be confirmed)", "马来西亚吉隆坡（详细地址待确认）") + """</span></span>
      </div>
      <div class="media-placeholder">""" + bi("Office map will appear here once the address is confirmed.", "地址确认后，办公室地图将显示于此。") + """</div>
    </aside>
  </div>
</section>
"""

page("contact-us.html", "contact",
     "Contact Drone X Malaysia | Get a Free Drone Spraying Quote",
     "Get a free quote for agriculture drone spraying in Malaysia. Call, WhatsApp or submit an inquiry — the Drone X team replies within 1-2 working days.",
     "drone spraying quote Malaysia, contact drone company Malaysia, 无人机喷药报价",
     contact_body)

# ════════════════ OTHER SOLUTIONS ════════════════
def sol_block(anchor, t_en, t_zh, d_en, d_zh):
    return """
    <article class="sol-block" id=\"""" + anchor + """\">
      <div class="benefit-icon">""" + CHECK + """</div>
      <div>
        <h3>""" + bi(t_en, t_zh) + """</h3>
        <p>""" + bi(d_en, d_zh) + """</p>
      </div>
      <a class="btn btn-ghost" href="contact-us.html">""" + bi("Learn More", "了解更多") + """</a>
    </article>"""

other_body = """
<section class="page-hero-video" aria-labelledby="os-heading">
  """ + hero_image_media("assets/drone-wireframe.png", "Technical wireframe render of a Drone X agriculture drone", 666, 375) + """
  <div class="wrap">
    <h1 id="os-heading">""" + bi("Other Solutions", "其他领域方案") + """</h1>
    <p class="lead">""" + bi(
        "Beyond agriculture, Drone X supports commercial, public sector and entertainment applications across Malaysia.",
        "除农业以外，Drone X 也为马来西亚的商业、公共部门与娱乐领域提供无人机方案。") + """</p>
  </div>
</section>
<section class="section" aria-label="Solutions list">
  <h2 class="sr-only">Solutions</h2>
  <div class="wrap sol-blocks stagger">
""" + sol_block("mapping", "Aerial Mapping", "航拍测绘",
    "Aerial mapping and data collection for developers, landowners and contractors, supporting planning, monitoring and reporting.",
    "为发展商、地主、承包商提供航拍测绘与数据收集服务，支援规划、监测与报告。") + \
sol_block("cleaning", "Building / Solar Cleaning", "建筑与太阳能清洗",
    "Drone-assisted cleaning for building facades, roofs and solar panels, raising efficiency and work safety.",
    "无人机辅助的建筑外墙、屋顶与太阳能板清洗方案，提升作业效率与安全性。") + \
sol_block("public", "Public Sector Support", "公共部门支援",
    "Aerial monitoring and support for public sector and emergency-related agencies, always within relevant approvals and regulations.",
    "为公共部门与紧急事件相关单位提供空中监测与支援，一切须符合相关审批与法规。") + \
sol_block("delivery", "Drone Delivery", "无人机送货探索",
    "Exploring drone delivery for suitable commercial and logistics use cases.",
    "探索适合的商业与物流应用场景的无人机送货方案。") + \
sol_block("esport", "Drone E-Sport", "无人机竞速",
    "Advancing drone racing and e-sport concepts that combine technology and entertainment.",
    "推动无人机竞速与电竞概念发展，结合科技与娱乐。") + \
sol_block("entertainment", "Drone Entertainment", "无人机表演／互动体验",
    "Drone light shows and interactive experience zones for events, brands and tourism.",
    "包括无人机灯光表演（Drone Show）与互动体验区（Drone Spot），适合活动、品牌与旅游用途。") + """
  </div>
</section>
"""

page("other-solutions.html", "none",
     "Drone Mapping, Cleaning & Aerial Solutions Malaysia | Drone X",
     "Drone X Malaysia offers aerial mapping, building and solar cleaning, public sector support, drone delivery, racing and drone light shows.",
     "drone mapping Malaysia, drone solar panel cleaning Malaysia, public safety drone Malaysia, drone show Malaysia, drone racing Malaysia",
     other_body)

# ════════════════ TECHNOLOGY & DATA ════════════════
tech_body = """
<section class="page-hero-video" aria-labelledby="td-heading">
  """ + hero_video_media("assets/spray-mist.mp4", "assets/spray-mist-poster.jpg", "Close-up macro shot of precision spray mist", 1280, 720) + """
  <div class="wrap">
    <h1 id="td-heading">""" + bi("Technology &amp; Data", "技术与数据能力") + """</h1>
    <p class="lead">""" + bi(
        "For enterprises and technical partners: the capabilities behind every Drone X operation, explained simply.",
        "面向企业与技术合作伙伴：以简单的方式介绍 Drone X 每次作业背后的技术能力。") + """</p>
  </div>
</section>
<section class="section" aria-label="Capabilities">
  <h2 class="sr-only">Capabilities</h2>
  <div class="wrap sol-blocks stagger">
""" + sol_block("capture", "Aerial Data Capture", "航拍数据采集",
    "High-quality aerial imagery and field data captured during every flight.",
    "每次飞行采集高品质航拍影像与田间数据。") + \
sol_block("dmapping", "Drone Mapping", "无人机测绘",
    "Accurate maps and models of land, crops and structures.",
    "为土地、作物与建筑生成精准的地图与模型。") + \
sol_block("processing", "Data Processing Support", "数据处理支援",
    "Turning raw flight data into reports and insights businesses can act on.",
    "将原始飞行数据转化为企业可用的报告与洞察。") + \
sol_block("workflow", "Technology-Enabled Workflows", "技术化作业流程",
    "Planned routes, controlled application rates and documented results on every job.",
    "每次作业都有规划航线、受控施用率与完整记录。") + """
  </div>
</section>
"""

page("technology-data.html", "none",
     "Drone Technology & Aerial Data Malaysia | Drone X",
     "Drone X Malaysia's technology capabilities: aerial data capture, drone mapping, data processing support and technology-enabled workflows.",
     "drone technology Malaysia, aerial data Malaysia, drone data processing",
     tech_body)

# ════════════════ PARTNERS ════════════════
partners_body = """
<section class="page-hero-video" aria-labelledby="pt-heading">
  """ + hero_image_media("assets/drone-real.png", "Studio product shot of a Drone X agriculture drone", 1672, 941) + """
  <div class="wrap">
    <h1 id="pt-heading">""" + bi("Partner With Drone X", "合作伙伴／商业合作") + """</h1>
    <p class="lead">""" + bi(
        "We welcome businesses and organisations to explore drone applications together across these areas.",
        "我们欢迎企业与机构在以下领域与我们共同探索无人机应用。") + """</p>
  </div>
</section>
<section class="section" aria-label="Partnership areas">
  <div class="wrap">
    <div class="chip-row reveal" style="margin-bottom:2.2rem">
      <span class="chip" aria-pressed="true">""" + bi("Agriculture Projects", "农业种植项目") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Aerial Mapping", "航拍测绘") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Building Cleaning", "建筑清洗") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Delivery Pilots", "送货试点") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Public Sector Support", "公共部门支援") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Drone Shows", "无人机表演") + """</span>
      <span class="chip" aria-pressed="true">""" + bi("Technology Collaboration", "技术合作") + """</span>
    </div>
    <a class="btn btn-primary reveal" href="contact-us.html">""" + bi("Let's Explore Together", "立即联系洽谈合作") + """</a>
  </div>
</section>
"""

page("partners.html", "none",
     "Partners | Drone X Malaysia",
     "Partner with Drone X Malaysia on agriculture projects, aerial mapping, building cleaning, delivery pilots, public sector support and drone shows.",
     "drone partnership Malaysia, drone collaboration Malaysia, 无人机商业合作",
     partners_body)

print("All pages generated.")
