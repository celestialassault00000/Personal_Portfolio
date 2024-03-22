import time 
import pandas as pd 
from datetime import date
from src.f_get_stats_for_stock_based_on_y_years_past_data import stock_data_stats_for_years
from data_loader import loader
from paths import ticker_symbol_path
def top_companies_based_on_returns(number_of_companies, number_of_years):
    df = loader(ticker_symbol_path)
    x= date.today()
    company_name = []
    daily_return =[]
    risk=[]
    for i in range(len(df)):
        company_name.append(df["Company Name"][i])
        a,b = stock_data_stats_for_years(str(df["Symbol"][i])+ ".NS",number_of_years)
        daily_return.append(a)
        risk.append(b)
    dict= pd.DataFrame({"company_name": company_name, "return": daily_return, "risk": risk})
    df2 = dict.sort_values(by=["return"], ascending= False)
    dict = df2.iloc[:number_of_companies]
    dict.to_csv(x+".csv", index= False)