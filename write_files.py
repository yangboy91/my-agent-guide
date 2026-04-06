index = open('index.html').read().replace('zh-CN','en').replace(
    '<title>Agent 指南 — 让 AI 帮你自动赚钱</title>',
    '<title>Agent Playbook - Build AI That Earns While You Sleep</title>'
)

with open('index.html','w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Agent Playbook - Build AI That Earns While You Sleep</title>
  <meta name="description" content="A practical guide to building your own AI agent that generates income on autopilot." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
<nav>
  <div class="nav-logo">Agent <span>Playbook</span></div>
  <ul class="nav-links">
    <li><a href="#guide">Guide</a></li>
    <li><a href="dashboard.html">Dashboard</a></li>
  </ul>
</nav>
<main>
  <section id="hero">
    <div class="status-badge"><span class="status-dot"></span>Live and running</div>
    <h1 class="hero-title">Build an AI Agent<br>that <em>earns for you</em></h1>
    <p class="hero-desc">A step-by-step playbook for setting up an AI agent that generates real income on autopilot. No theory. Just systems that actually run.</p>
    <div class="revenue-badge">- <strong id="revenue-amount">$0</strong> lifetime revenue - <a href="dashboard.html">live dashboard</a></div>
  </section>
  <div class="divider"></div>
  <section id="guide">
    <p class="section-label">Latest Guide</p>
    <div class="product-card">
      <div>
        <div class="product-meta">
          <span class="product-tag">PDF Guide</span>
          <span class="product-tag">~60 pages</span>
          <span class="product-tag">Updated April 2026</span>
        </div>
        <h2 class="product-title">How to Build Your Own Agent<br>That Makes Money for You</h2>
        <p class="product-desc">From picking the right tools and setting up memory, to delegating tasks and running a real income loop - every step is broken down with templates you can use today.</p>
        <ul class="feature-list">
          <li>Tool selection: the LLM + framework stack that actually works for automation</li>
          <li>Memory architecture: give your agent persistent context so it gets smarter over time</li>
          <li>Permission model: safely grant your agent access to email, browser, and APIs</li>
          <li>Three income paths: content monetization, affiliate marketing, and micro-SaaS</li>
          <li>Scheduling: CRON + Webhooks for 24/7 unattended operation</li>
          <li>Safety rails: prevent your agent from doing things you did not ask for</li>
          <li>Plug-and-play templates: ready-to-use AGENT.md and MEMORY.md config files</li>
        </ul>
        <div class="buy-section">
          <span class="price">$29</span>
          <a href="#" class="btn-primary" id="buy-btn">Get the Playbook</a>
        </div>
      </div>
      <div class="product-cover">
        <div class="cover-title">How to Build Your Own Agent<br>That Makes Money for You</div>
        <div class="cover-sub">A practical playbook for building an AI-powered income system</div>
        <div class="cover-brand">AGENT PLAYBOOK</div>
      </div>
    </div>
  </section>
  <section class="outline-section">
    <p class="section-label">What's Inside</p>
    <div class="outline-grid">
      <div class="outline-item"><div class="ch-num">01 - 02</div><div class="ch-title">Agent vs. Chatbot: Why It Matters</div><div class="ch-desc">What separates an AI that earns from one that just answers questions. Tool comparison and platform breakdown.</div></div>
      <div class="outline-item"><div class="ch-num">03 - 04</div><div class="ch-title">Identity and Memory Systems</div><div class="ch-desc">Designing SOUL.md and IDENTITY.md. A three-layer memory architecture that makes your agent smarter over time.</div></div>
      <div class="outline-item"><div class="ch-num">05 - 06</div><div class="ch-title">Tool Access and Permissions</div><div class="ch-desc">Connecting your agent to email, browser, and Stripe API. A four-tier permission model that keeps things safe.</div></div>
      <div class="outline-item"><div class="ch-num">07 - 08</div><div class="ch-title">Three Paths to Automated Income</div><div class="ch-desc">Content publishing, affiliate marketing bots, and micro-SaaS tools. Which path fits you best.</div></div>
      <div class="outline-item"><div class="ch-num">09 - 10</div><div class="ch-title">Scheduling and Unattended Operation</div><div class="ch-desc">CRON jobs, Webhook triggers, and self-healing error recovery. Keep your system running while you sleep.</div></div>
      <div class="outline-item"><div class="ch-num">11 - 12</div><div class="ch-title">Quick-Start Kit</div><div class="ch-desc">Copy-paste template files. From zero to a working agent in one afternoon. Every config, every decision point.</div></div>
    </div>
  </section>
</main>
<footer>
  <span>2026 Agent Playbook</span>
  <a href="dashboard.html">Revenue Dashboard</a>
  <a href="mailto:hi@yourdomain.com">Contact</a>
</footer>
<script src="main.js"></script>
</body>
</html>""")

with open('dashboard.html','w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Revenue Dashboard - Agent Playbook</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
<nav>
  <a class="nav-logo" href="index.html">Agent <span>Playbook</span></a>
  <ul class="nav-links">
    <li><a href="index.html#guide">Guide</a></li>
    <li><a href="dashboard.html">Dashboard</a></li>
  </ul>
</nav>
<main>
  <div class="status-badge" style="margin-bottom:2rem"><span class="status-dot"></span>Live data</div>
  <h1 style="font-size:2rem;font-weight:700;letter-spacing:-0.03em;margin-bottom:0.5rem">Revenue Dashboard</h1>
  <p style="color:var(--text-muted);margin-bottom:3rem;font-size:0.9rem">All numbers pulled live from Stripe. Full transparency, no vanity metrics.</p>
  <div class="dash-grid">
    <div class="dash-card"><div class="label">Lifetime Revenue</div><div class="value" id="dash-total">Loading...</div><div class="sub">Since launch</div></div>
    <div class="dash-card"><div class="label">This Month</div><div class="value" id="dash-month">-</div><div class="sub" id="dash-month-label">Current month</div></div>
    <div class="dash-card"><div class="label">Total Orders</div><div class="value" id="dash-orders">-</div><div class="sub">Copies sold</div></div>
  </div>
  <p class="section-label">Recent Sales</p>
  <table class="dash-table">
    <thead><tr><th>Date</th><th>Product</th><th>Amount</th><th>Status</th></tr></thead>
    <tbody id="dash-table-body"><tr><td colspan="4" style="color:var(--text-dim);padding:2rem 1rem">Loading...</td></tr></tbody>
  </table>
</main>
<footer>
  <span>2026 Agent Playbook</span>
  <a href="index.html">Back to Home</a>
</footer>
<script src="main.js"></script>
</body>
</html>""")

with open('main.js','w') as f:
    f.write("""const CONFIG = {
  stripeCheckoutUrl: 'https://buy.stripe.com/YOUR_PAYMENT_LINK',
  dashboardApiUrl: '/api/dashboard',
};
(function initBuyButton() {
  var btn = document.getElementById('buy-btn');
  if (!btn) return;
  btn.addEventListener('click', function(e) { e.preventDefault(); window.open(CONFIG.stripeCheckoutUrl, '_blank'); });
})();
(function initRevenueAmount() {
  var el = document.getElementById('revenue-amount');
  if (!el) return;
  fetch(CONFIG.dashboardApiUrl).then(function(r){return r.json();}).then(function(d){if(d&&d.totalRevenue!=null)el.textContent=formatUSD(d.totalRevenue);}).catch(function(){el.textContent='$0';});
})();
(function initDashboard() {
  var totalEl=document.getElementById('dash-total'),monthEl=document.getElementById('dash-month'),ordersEl=document.getElementById('dash-orders'),tbody=document.getElementById('dash-table-body');
  if(!totalEl)return;
  var ml=document.getElementById('dash-month-label');
  if(ml){var n=new Date();ml.textContent=n.toLocaleString('en-US',{month:'long',year:'numeric'});}
  fetch(CONFIG.dashboardApiUrl).then(function(r){return r.json();}).then(function(d){
    totalEl.textContent=formatUSD(d.totalRevenue||0);
    monthEl.textContent=formatUSD(d.monthRevenue||0);
    ordersEl.textContent=String(d.totalOrders||0);
    if(tbody&&Array.isArray(d.recentOrders)&&d.recentOrders.length>0){
      tbody.innerHTML=d.recentOrders.map(function(o){return '<tr><td>'+formatDate(o.created)+'</td><td>How to Build Your Own Agent That Makes Money for You</td><td class="amount">'+formatUSD(o.amount)+'</td><td style="color:var(--green)">Paid</td></tr>';}).join('');
    }else{tbody.innerHTML='<tr><td colspan="4" style="color:var(--text-dim);padding:2rem 1rem">No orders yet</td></tr>';}
  }).catch(function(){totalEl.textContent='$0';monthEl.textContent='$0';ordersEl.textContent='0';if(tbody)tbody.innerHTML='<tr><td colspan="4" style="color:var(--text-dim);padding:2rem 1rem">Configure your Stripe API key to see live data</td></tr>';});
})();
function formatUSD(c){var d=(typeof c==='number'&&c>100)?c/100:c;return '$'+Number(d).toLocaleString('en-US',{minimumFractionDigits:0,maximumFractionDigits:0});}
function formatDate(ts){var d=new Date(typeof ts==='number'?ts*1000:ts);return d.toLocaleDateString('en-US',{year:'numeric',month:'short',day:'numeric'});}
""")

print("All files written successfully in English!")
