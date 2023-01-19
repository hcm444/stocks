import yfinance as yf
import tkinter as tk
import matplotlib.pyplot as plt

class PortfolioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Portfolio")
        self.portfolio = {}

        self.tickers_label = tk.Label(self, text="Enter tickers (comma-separated):")
        self.tickers_label.pack()
        self.tickers_entry = tk.Entry(self)
        self.tickers_entry.pack()

        self.shares_label = tk.Label(self, text="Enter shares (comma-separated):")
        self.shares_label.pack()
        self.shares_entry = tk.Entry(self)
        self.shares_entry.pack()

        self.start_date_label = tk.Label(self, text="Enter start date (yyyy-mm-dd):")
        self.start_date_label.pack()
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.pack()

        self.end_date_label = tk.Label(self, text="Enter end date (yyyy-mm-dd):")
        self.end_date_label.pack()
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.pack()

        self.build_portfolio_button = tk.Button(self, text="Build Portfolio", command=self.build_portfolio)
        self.build_portfolio_button.pack()

        self.display_portfolio_button = tk.Button(self, text="Display Portfolio", command=self.display_portfolio)
        self.display_portfolio_button.pack()

        self.portfolio_display = tk.Text(self)
        self.portfolio_display.pack()

        self.display_portfolio_button = tk.Button(self, text="Display Portfolio", command=self.display_portfolio)
        self.display_portfolio_button.pack()


    def get_stock_info(self, ticker, start_date, end_date):
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        historical_prices = stock.history(start=start_date, end=end_date)
        return stock_info, historical_prices

    def build_portfolio(self):
        tickers = self.tickers_entry.get().split(",")
        shares = self.shares_entry.get().split(",")
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        for i, ticker in enumerate(tickers):
            stock_info, historical_prices = self.get_stock_info(ticker, start_date, end_date)
            self.portfolio[ticker] = {'info': stock_info, 'history': historical_prices, 'shares': shares[i]}

    def display_portfolio(self):
        plt.figure()
        for ticker, data in self.portfolio.items():
            historical_prices = data['history']
            plt.plot(historical_prices.index, historical_prices['Close'], label=ticker)
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title('Stock Prices')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    app = PortfolioApp()
    app.mainloop()
