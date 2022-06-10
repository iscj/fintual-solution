from datetime import date

from portfolio import Portfolio, Stock

portfolio = Portfolio()
stock = Stock('Amazon')
stock.add_price(date(2022,5,1), 25)
stock.add_price(date(2022,5,2), 26)
stock.add_price(date(2022,5,3), 27)
stock.add_price(date(2022,5,4), 26)
stock.add_price(date(2022,5,5), 25.4)
stock.add_price(date(2022,5,6), 25)
stock.add_price(date(2022,5,7), 26.2)
stock.add_price(date(2022,5,8), 26)
portfolio.add_stock(stock, 6)
portfolio.add_stock(stock, 4)
value_annualized = portfolio.profit(date(2022,5,1), date(2022,5,5), True)
value_cumulaitve = portfolio.profit(date(2022,5,1), date(2022,5,3))
print(f'The value annualized is: {value_annualized}%')
print(f'The value cumulative is: {value_cumulaitve}%')