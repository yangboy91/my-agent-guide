const CONFIG = {
  stripeCheckoutUrl: 'https://buy.stripe.com/YOUR_PAYMENT_LINK',
  dashboardApiUrl: '/api/dashboard',
};

(function initBuyButton() {
  const btn = document.getElementById('buy-btn');
  if (!btn) return;
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    window.open(CONFIG.stripeCheckoutUrl, '_blank');
  });
})();

(function initRevenueAmount() {
  const el = document.getElementById('revenue-amount');
  if (!el) return;
  fetch(CONFIG.dashboardApiUrl)
    .then(r => r.json())
    .then(data => { if (data && data.totalRevenue != null) el.textContent = formatCNY(data.totalRevenue); })
    .catch(() => { el.textContent = '¥0'; });
})();

(function initDashboard() {
  const totalEl = document.getElementById('dash-total');
  const monthEl = document.getElementById('dash-month');
  const ordersEl = document.getElementById('dash-orders');
  const tbody = document.getElementById('dash-table-body');
  if (!totalEl) return;
  const monthLabel = document.getElementById('dash-month-label');
  if (monthLabel) { const now = new Date(); monthLabel.textContent = now.getFullYear() + ' 年 ' + (now.getMonth() + 1) + ' 月'; }
  fetch(CONFIG.dashboardApiUrl)
    .then(r => r.json())
    .then(data => {
      totalEl.textContent = formatCNY(data.totalRevenue ?? 0);
      monthEl.textContent = formatCNY(data.monthRevenue ?? 0);
      ordersEl.textContent = String(data.totalOrders ?? 0);
      if (tbody && Array.isArray(data.recentOrders) && data.recentOrders.length > 0) {
        tbody.innerHTML = data.recentOrders.map(o => '<tr><td>' + formatDate(o.created) + '</td><td>如何搭建自己的 Agent 帮你自动赚钱</td><td class="amount">' + formatCNY(o.amount) + '</td><td style="color:var(--green)">✓ 成功</td></tr>').join('');
      } else {
        tbody.innerHTML = '<tr><td colspan="4" style="color:var(--text-dim);padding:2rem 1rem">暂无订单数据</td></tr>';
      }
    })
    .catch(() => {
      totalEl.textContent = '¥0'; monthEl.textContent = '¥0'; ordersEl.textContent = '0';
      if (tbody) tbody.innerHTML = '<tr><td colspan="4" style="color:var(--text-dim);padding:2rem 1rem">请配置 Stripe API</td></tr>';
    });
})();

function formatCNY(cents) {
  const yuan = typeof cents === 'number' && cents > 1000 ? cents / 100 : cents;
  return '¥' + Number(yuan).toLocaleString('zh-CN', { minimumFractionDigits: 0, maximumFractionDigits: 0 });
}
function formatDate(ts) {
  const d = new Date(typeof ts === 'number' ? ts * 1000 : ts);
  return d.getFullYear() + '-' + String(d.getMonth()+1).padStart(2,'0') + '-' + String(d.getDate()).padStart(2,'0');
}
