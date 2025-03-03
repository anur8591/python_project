import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class Stock:
    def __init__(self, name, symbol, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def update_price(self):
        change = random.uniform(-20, 20)
        self.price = round(max(1, self.price + change), 2)

class Market:
    def __init__(self):
        self.stocks = [
            Stock("Apple", "AAPL", 150.0),
            Stock("Tesla", "TSLA", 720.0),
            Stock("Google", "GOOGL", 2800.0),
            Stock("Amazon", "AMZN", 3400.0)
        ]

    def display_stocks(self):
        stock_info = "\nAvailable Stocks:\n"
        for stock in self.stocks:
            stock_info += f"{stock.symbol}: {stock.name} - ${stock.price}\n"
        return stock_info

    def update_market(self):
        for stock in self.stocks:
            stock.update_price()

class Portfolio:
    def __init__(self):
        self.balance = 10000
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
                    return f"Bought {quantity} shares of {stock.name} at ${stock.price} each."
                else:
                    return "Not enough balance!"
        return "Stock not found!"

    def sell_stock(self, market, symbol, quantity):
        if symbol in self.holdings and self.holdings[symbol]['quantity'] >= quantity:
            for stock in market.stocks:
                if stock.symbol == symbol:
                    self.balance += stock.price * quantity
                    self.holdings[symbol]['quantity'] -= quantity
                    if self.holdings[symbol]['quantity'] == 0:
                        del self.holdings[symbol]
                    return f"Sold {quantity} shares of {stock.name} at ${stock.price} each."
        return "Not enough shares to sell or stock not found in holdings!"

    def display_portfolio(self):
        portfolio_info = f"Balance: ${self.balance}\n"
        if not self.holdings:
            portfolio_info += "No stocks owned."
        else:
            for symbol, data in self.holdings.items():
                portfolio_info += f"{symbol}: {data['quantity']} shares at ${data['price']} each\n"
        return portfolio_info

class StockMarketApp:
    def __init__(self, root):
        self.market = Market()
        self.portfolio = Portfolio()
        self.root = root
        self.root.title("Stock Market Simulator")

        self.stock_display = tk.Text(root, height=10, width=50, bg="lightgrey", font=("Arial", 12))
        self.stock_display.pack()

        self.portfolio_display = tk.Text(root, height=10, width=50, bg="lightgrey", font=("Arial", 12))
        self.portfolio_display.pack()

        self.update_button = tk.Button(root, text="Update Market Prices", command=self.update_market, bg="blue", fg="white")
        self.update_button.pack()

        self.buy_button = tk.Button(root, text="Buy Stock", command=self.buy_stock, bg="green", fg="white")
        self.buy_button.pack()

        self.sell_button = tk.Button(root, text="Sell Stock", command=self.sell_stock, bg="red", fg="white")
        self.sell_button.pack()

        self.status_message = tk.Label(root, text="", fg="red")
        self.status_message.pack()

        self.search_entry = tk.Entry(root, width=20)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search Stock", command=self.search_stock)
        self.search_button.pack()

        self.refresh_display()

    def refresh_display(self):
        self.search_entry.delete(0, tk.END)
        self.stock_display.delete(1.0, tk.END)
        self.stock_display.insert(tk.END, self.market.display_stocks())
        self.portfolio_display.delete(1.0, tk.END)
        self.portfolio_display.insert(tk.END, self.portfolio.display_portfolio())

    def update_market(self):
        self.market.update_market()
        self.refresh_display()
        messagebox.showinfo("Info", "Market prices updated!")

    def buy_stock(self):
        self.status_message.config(text="")
        symbol = simpledialog.askstring("Input", "Enter stock symbol to buy:").upper()
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if symbol and quantity:
            result = self.portfolio.buy_stock(self.market, symbol, quantity)
            self.status_message.config(text=result)
            self.refresh_display()

    def sell_stock(self):
        self.status_message.config(text="")
        symbol = simpledialog.askstring("Input", "Enter stock symbol to sell:").upper()
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if symbol and quantity:
            result = self.portfolio.sell_stock(self.market, symbol, quantity)
            self.status_message.config(text=result)
            self.refresh_display()

    def search_stock(self):
        search_term = self.search_entry.get().upper()
        found = False
        for stock in self.market.stocks:
            if stock.symbol == search_term or stock.name.upper() == search_term:
                messagebox.showinfo("Stock Found", f"{stock.symbol}: {stock.name} - ${stock.price}")
                found = True
                break
        if not found:
            messagebox.showinfo("Stock Not Found", "No stock matches your search.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockMarketApp(root)
    root.mainloop()
