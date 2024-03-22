import pandas as pd 
def ticker_data_loader(ticker_symbol_data):
    df = pd.read_csv(ticker_symbol_data)
    return df 
    