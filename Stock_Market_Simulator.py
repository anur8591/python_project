import random
import json

class Stock:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def update_price(self):
        """Randomly change stock price to simulate market fluctuations"""
        change = random.uniform(-5, 5)  # Random price change between -5 and +5
        self.price = round(max(1, self.price + change), 2)  # Ensure price doesn't go below 1

class Market:
    def __init__(self):
        self.stocks = [
            Stock("Apple", "AAPL", 150.0),
            Stock("Tesla", "TSLA", 720.0),
            Stock("Google", "GOOGL", 2800.0),
            Stock("Amazon", "AMZN", 3400.0)
        ]

    def display_stocks(self):
        print("\nAvailable Stocks:")
        for stock in self.stocks:
            print(f"{stock.symbol}: {stock.name} - ${stock.price}")

    def update_market(self):
        """Update stock prices randomly"""
        for stock in self.stocks:
            stock.update_price()

class Portfolio:
    def __init__(self):
        self.balance = 10000  # Starting money
        self.holdings = {}

    def buy_stock(self, market, symbol, quantity):
        for stock in market.stocks:
            if stock.symbol == symbol:
                cost = stock.price * quantity
                if self.balance >= cost:
                    self.balance -= cost
                    if symbol in self.holdings:
                        self.holdings[symbol]['quantity'] += quantity
                    else:
                        self.holdings[symbol] = {'quantity': quantity, 'price': stock.price}
                    print(f"Bought {quantity} shares of {stock.name} at ${stock.price} each.")
                else:
                    print("Not enough balance!")
                return
        print("Stock not found!")

    def sell_stock(self, market, symbol, quantity):
        if symbol in self.holdings and self.holdings[symbol]['quantity'] >= quantity:
            for stock in market.stocks:
                if stock.symbol == symbol:
                    self.balance += stock.price * quantity
                    self.holdings[symbol]['quantity'] -= quantity
                    if self.holdings[symbol]['quantity'] == 0:
                        del self.holdings[symbol]
                    print(f"Sold {quantity} shares of {stock.name} at ${stock.price} each.")
                    return
        print("Not enough shares to sell or stock not found in holdings!")

    def display_portfolio(self):
        print("\nYour Portfolio:")
        print(f"Balance: ${self.balance}")
        if not self.holdings:
            print("No stocks owned.")
        else:
            for symbol, data in self.holdings.items():
                print(f"{symbol}: {data['quantity']} shares at ${data['price']} each")

# Sample usage
def main():
    market = Market()
    portfolio = Portfolio()
    while True:
        print("\n1. View Stocks")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View Portfolio")
        print("5. Update Market Prices")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            market.display_stocks()
        elif choice == "2":
            symbol = input("Enter stock symbol to buy: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.buy_stock(market, symbol, quantity)
        elif choice == "3":
            symbol = input("Enter stock symbol to sell: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.sell_stock(market, symbol, quantity)
        elif choice == "4":
            portfolio.display_portfolio()
        elif choice == "5":
            market.update_market()
            print("Market prices updated!")
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
