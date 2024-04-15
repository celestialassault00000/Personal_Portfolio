from src.scrapping_data import scrape_company_data_for_dividend, scrape_company_data_for_earnings, scrape_company_data_for_operating_margin, scrape_company_data_market_cap, scrape_company_data_for_p_e_ratio, combine_csv
def main():
    scrape_company_data_for_p_e_ratio()
    scrape_company_data_for_dividend()
    scrape_company_data_for_earnings()
    scrape_company_data_for_operating_margin()
    scrape_company_data_market_cap()
    combine_csv()
