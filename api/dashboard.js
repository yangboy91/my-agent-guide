const Stripe = require('stripe');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (!process.env.STRIPE_SECRET_KEY) {
    return res.json({ totalRevenue: 0, monthRevenue: 0, totalOrders: 0, recentOrders: [] });
  }
  const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
  try {
    const charges = await stripe.charges.list({ limit: 20 });
    const succeeded = charges.data.filter(c => c.status === 'succeeded');
    const totalRevenue = succeeded.reduce((sum, c) => sum + c.amount, 0);
    const now = new Date();
    const startOfMonth = new Date(now.getFullYear(), now.getMonth(), 1).getTime() / 1000;
    const monthRevenue = succeeded.filter(c => c.created >= startOfMonth).reduce((sum, c) => sum + c.amount, 0);
    const recentOrders = succeeded.slice(0, 10).map(c => ({ created: c.created, amount: c.amount, status: c.status }));
    res.json({ totalRevenue, monthRevenue, totalOrders: succeeded.length, recentOrders });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
