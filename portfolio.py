from decimal import Decimal

class Stock():
	def __init__(self, name):
		self.name = name
		self.prices = {}

	def add_price(self, date, price):
		if date not in self.prices:
			self.prices[date] = Decimal(price)

	def price(self, date):
		return self.prices[date]


class Portfolio():
	def __init__(self):
		self.stocks = {}

	def add_stock(self, stock, amount):
		if amount <= 0:
			raise ValueError('The amount must be major to 0')

		if stock not in self.stocks:
			if len(stock.prices) == 0:
				raise ValueError('The stock prices is empty')

			self.stocks[stock] = Decimal(0)
		self.stocks[stock] += amount

	def profit(self, start_date, end_date, is_annualized=False):
		if end_date < start_date:
			raise ValueError('The given end date is before start date')
		if is_annualized:
			return round(self.annualized(start_date, end_date), 2)
		return round(self.cumulative(start_date, end_date), 2)

	def cumulative(self, start, end):
		total_start = Decimal(0)
		total_end = Decimal(0)

		for stock in self.stocks.keys():
			total_stock = self.stocks[stock]
			total_start += (total_stock * stock.price(start))
			total_end += (total_stock * stock.price(end))

		return (total_end - total_start) / total_start

	def annualized(self, start, end):
		cumulative_return = self.cumulative(start, end)
		days_held = Decimal((end - start).days)

		return (1 + cumulative_return) ** (365 / days_held) - 1
