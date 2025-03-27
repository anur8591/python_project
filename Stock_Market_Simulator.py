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

    def set_alert(self):
        symbol = simpledialog.askstring("Set Alert", "Enter stock symbol:")
        target_price = simpledialog.askfloat("Set Alert", "Enter target price:")
        if self.portfolio.set_alert(self.market, symbol, target_price):
            messagebox.showinfo("Success", f"Alert set for {symbol} at ${target_price}.")
        else:
            messagebox.showerror("Error", "Failed to set alert.")

        
    def buy_stock(self, market, symbol, quantity, order_type='market'):

        if order_type == 'limit':
            limit_price = simpledialog.askfloat("Limit Order", "Enter limit price:")
            for stock in market.stocks:
                if stock.symbol == symbol and stock.price <= limit_price:
                    cost = limit_price * quantity
                    if self.balance >= cost:
                        self.balance -= cost
                        if symbol in self.holdings:
                            self.holdings[symbol]['quantity'] += quantity
                        else:
                            self.holdings[symbol] = {'quantity': quantity, 'price': stock.price}
                        return f"Limit order placed for {quantity} shares of {stock.name} at ${limit_price} each."
                    else:
                        return "Not enough balance!"
        else:
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
        return "Stock not found!" if order_type == 'market' else "Limit order placed!"

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
        total_value = self.balance

        portfolio_info = f"Balance: ${self.balance}\n"
        if not self.holdings:
            portfolio_info += "No stocks owned."
        else:
            for symbol, data in self.holdings.items():
                portfolio_info += f"{symbol}: {data['quantity']} shares at ${data['price']} each\n"
        for symbol, data in self.holdings.items():
            total_value += data['quantity'] * data['price']
        portfolio_info += f"Total Portfolio Value: ${total_value}\n"
        return portfolio_info


class Bitcoin:
    def __init__(self, price):
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class StockMarketApp:
    def __init__(self, root):
        self.users = []  # List to store user accounts

    def __init__(self, root):
        self.bitcoin = Bitcoin(40000)  # Initial Bitcoin price
        self.market = Market()
        self.portfolio = Portfolio()
        self.root = root
        self.root.title("Stock Market Simulator")

        self.stock_display = tk.Text(root, height=10, width=50, bg="lightgrey", font=("Arial", 12))
        self.stock_display.pack()

        self.portfolio_display = tk.Text(root, height=10, width=50, bg="lightgrey", font=("Arial", 12))
        self.portfolio_display.pack()

        self.trade_bitcoin_button = tk.Button(root, text="Trade Bitcoin", command=self.trade_bitcoin, bg="purple", fg="white")
        self.trade_bitcoin_button.pack()
        
        self.login_button = tk.Button(root, text="Login", command=self.login, bg="orange", fg="white")
        self.login_button.pack()
        
        self.signup_button = tk.Button(root, text="Signup", command=self.signup, bg="cyan", fg="white")
        self.signup_button.pack()

        self.update_button = tk.Button(root, text="Update Market Prices", command=self.update_market, bg="blue", fg="white")
        self.refresh_button = tk.Button(root, text="Refresh Data", command=self.refresh_data, bg="green", fg="white")
        self.refresh_button.pack()

        self.update_button.pack()

        self.buy_button = tk.Button(root, text="Buy Stock", command=self.buy_stock, bg="green", fg="white")
        self.buy_button.pack()

        self.sell_button = tk.Button(root, text="Sell Stock", command=self.sell_stock, bg="red", fg="white")
        self.alert_button = tk.Button(root, text="Set Alert", command=self.set_alert, bg="yellow", fg="black")
        self.alert_button.pack()

        self.alert_button.pack()

        self.sell_button.pack()

        self.status_message = tk.Label(root, text="", fg="red")
        self.status_message.pack()

        self.search_entry = tk.Entry(root, width=20)
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search Stock", command=self.search_stock)
        self.search_button.pack()

        self.refresh_display()

    def signup(self):
        username = simpledialog.askstring("Signup", "Enter username:")
        password = simpledialog.askstring("Signup", "Enter password:", show='*')
        if username and password:
            new_user = User(username, password)
            self.users.append(new_user)
            messagebox.showinfo("Success", "User registered successfully!")

    def login(self):
        username = simpledialog.askstring("Login", "Enter username:")
        password = simpledialog.askstring("Login", "Enter password:", show='*')
        for user in self.users:
            if user.username == username and user.password == password:
                messagebox.showinfo("Success", "Login successful!")
                return
        messagebox.showerror("Error", "Invalid username or password.")

    def refresh_display(self):
        self.search_entry.delete(0, tk.END)
        self.stock_display.delete(1.0, tk.END)
        self.stock_display.insert(tk.END, self.market.display_stocks())
        self.portfolio_display.delete(1.0, tk.END)
        self.portfolio_display.insert(tk.END, self.portfolio.display_portfolio())
        self.status_message.config(text=f"Bitcoin Price: ${self.bitcoin.price}")

    def refresh_data(self):
        # Logic to refresh market data from the API
        self.market.update_market()
        self.refresh_display()
        messagebox.showinfo("Info", "Market data refreshed!")
        
    def update_market(self):
        self.market.update_market()
        self.refresh_display()
        messagebox.showinfo("Info", "Market prices updated!")

    def trade_bitcoin(self):
        self.status_message.config(text="")
        action = simpledialog.askstring("Input", "Enter 'buy' to buy or 'sell' to sell Bitcoin:").lower()
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        if action == 'buy':
            cost = self.bitcoin.price * quantity
            if self.portfolio.balance >= cost:
                self.portfolio.balance -= cost
                messagebox.showinfo("Success", f"Bought {quantity} Bitcoin at ${self.bitcoin.price} each.")
            else:
                messagebox.showinfo("Error", "Not enough balance to buy Bitcoin.")
        elif action == 'sell':
            # Implement selling logic here (for simplicity, assume user has Bitcoin)
            self.portfolio.balance += self.bitcoin.price * quantity
            messagebox.showinfo("Success", f"Sold {quantity} Bitcoin at ${self.bitcoin.price} each.")
        else:
            messagebox.showinfo("Error", "Invalid action. Please enter 'buy' or 'sell'.")

    def buy_stock(self):
        self.status_message.config(text="")
        symbol = simpledialog.askstring("Input", "Enter stock symbol to buy:").upper()
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        order_type = simpledialog.askstring("Order Type", "Enter 'market' for market order or 'limit' for limit order:").lower()
        if symbol and quantity:
            result = self.portfolio.buy_stock(self.market, symbol, quantity, order_type)
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
