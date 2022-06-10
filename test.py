import unittest
from datetime import date
from decimal import Decimal

from portfolio import Stock, Portfolio

class TestPortfolio(unittest.TestCase):
	def test_add_stock_negative(self):
		portfolio = Portfolio()
		stock = Stock('Apple')

		self.assertRaises(ValueError, portfolio.add_stock, stock, -1)

	def test_add_stock_witout_prices(self):
		portfolio = Portfolio()
		stock = Stock('Apple')

		self.assertRaises(ValueError, portfolio.add_stock, stock, 2)

	def test_profit_error_dates(self):
		portfolio = Portfolio()
		stock = Stock('Apple')
		stock.add_price(date(2022,5,1), 18)
		stock.add_price(date(2022,5,2), 29)
		stock.add_price(date(2022,5,3), 27)
		stock.add_price(date(2022,5,4), 26)
		stock.add_price(date(2022,5,5), 25.4)
		stock.add_price(date(2022,5,6), 25)
		stock.add_price(date(2022,5,7), 26.2)
		stock.add_price(date(2022,5,8), 26)
		portfolio.add_stock(stock, 6)

		self.assertRaises(ValueError, portfolio.profit, date(2022,5,7), date(2022,5,1))

	def test_profit(self):
		expected = round(Decimal(0.41), 2)
		portfolio = Portfolio()
		stock = Stock('Apple')
		stock.add_price(date(2022,5,1), 18)
		stock.add_price(date(2022,5,2), 29)
		stock.add_price(date(2022,5,3), 27)
		stock.add_price(date(2022,5,4), 26)
		stock.add_price(date(2022,5,5), 25.4)
		stock.add_price(date(2022,5,6), 25)
		stock.add_price(date(2022,5,7), 26.2)
		stock.add_price(date(2022,5,8), 26)
		portfolio.add_stock(stock, 6)
		profit = portfolio.profit(date(2022,5,1), date(2022,5,5))

		self.assertEqual(expected, profit)

	def test_profit_annualized(self):
		expected = round(Decimal(3.26), 2)
		portfolio = Portfolio()
		stock = Stock('Apple')
		stock.add_price(date(2022,5,1), 25)
		stock.add_price(date(2022,5,2), 26)
		stock.add_price(date(2022,5,3), 27)
		stock.add_price(date(2022,5,4), 26)
		stock.add_price(date(2022,5,5), 25.4)
		stock.add_price(date(2022,5,6), 25)
		stock.add_price(date(2022,5,7), 26.2)
		stock.add_price(date(2022,5,8), 26)
		portfolio.add_stock(stock, 6)
		profit = portfolio.profit(date(2022,5,1), date(2022,5,5), True)

		self.assertEqual(expected, profit)

if __name__ == '__main__':
	unittest.main()