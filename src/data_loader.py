import pandas as pd 
from src.paths import ticker_symbol_data
def ticker_data_loader(ticker_symbol_data= ticker_symbol_data):
    df = pd.read_excel(ticker_symbol_data)
    return df 
    