import yfinance as yf
def stock_data_stats_for_years(ticker_symbol, years):
    try:
        stock_data = yf.Ticker(ticker_symbol)
        t="{}y".format(years)
        historical_data = stock_data.history(period=t)
        historical_data["Intraday_max_return"] = (historical_data["High"] - historical_data["Low"])/historical_data["Close"]
        # print("Last {} years data:". format(years))
        returns = historical_data['Close'].pct_change()
        average_daily_return_intraday = historical_data["Intraday_max_return"].mean()
        average_daily_volatility_intraday = historical_data["Intraday_max_return"].std()
        average_daily_return = returns.mean()
        volatility = returns.std()
        # print("Average Daily Return:", average_daily_return)
        # print("Volatility (Standard Deviation of Daily Returns):", volatility)
        # print("Average Daily Return for Intraday: ", average_daily_return_intraday)
        # print("Average Daily volatility for intraday: ", average_daily_volatility_intraday)
        return average_daily_return, volatility
    except Exception as e:
        print("Error fetching or analyzing data:", e)

# ticker_symbol = "RELIANCE.NS"  # Change this to the ticker symbol of the Indian stock you want to analyze
# stock_data_stats_for_years(ticker_symbol, 5)
