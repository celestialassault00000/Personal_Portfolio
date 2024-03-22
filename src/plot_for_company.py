import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objs as go
def plot_interactive_stock_data(ticker_symbol, years):
    try:
        # Fetch stock data
        stock_data = yf.Ticker(ticker_symbol)
        
        # Get historical market data for the specified number of years
        period = "{}y".format(years)
        historical_data = stock_data.history(period=period)
        
        # If data for the specified number of years is not available, fetch data for the maximum available period
        if historical_data.empty:
            print("Data not found for {} years. Fetching data for maximum available period.".format(years))
            historical_data = stock_data.history(period="max")
        
        # Plot interactive price chart using plotly
        trace = go.Scatter(x=historical_data.index, y=historical_data['Close'], mode='lines', name=ticker_symbol)
        layout = go.Layout(title='Interactive Price Chart for ' + ticker_symbol, xaxis=dict(title='Date'), yaxis=dict(title='Price'))
        fig = go.Figure(data=[trace], layout=layout)
        fig.show()
        
    except Exception as e:
        print("Error fetching or plotting data:", e)

# Example usage:
ticker_symbol = "RELIANCE.NS"  # Change this to the ticker symbol of the Indian stock you want to analyze
years = 100  # Change this to the desired number of years
plot_interactive_stock_data(ticker_symbol, years)
