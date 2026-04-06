const CONFIG = {
  stripeCheckoutUrl: 'https://buy.stripe.com/fZu14n1VkfCWeVPfyX1ZS00',
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
