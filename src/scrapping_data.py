import requests
import os 
from bs4 import BeautifulSoup
import pandas as pd
from src.paths import data_directory_scrapped
from src.base_urls import market_cap, earnings, revenue, p_e_ratio, dividend, operating_margin
def scrape_company_data_market_cap(base_url = market_cap, num_pages = 20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "market_cap": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/market_cap.csv", index= False)
    else:
        return None

def scrape_company_data_for_earnings(base_url = earnings, num_pages= 20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "earnings": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/earnings.csv", index= False)
    else:
        return None

# Example usage:




def scrape_company_data_for_revenue(base_url= revenue, num_pages= 20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "revenue": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/revenue.csv", index= False)
    else:
        return None






def scrape_company_data_for_p_e_ratio(base_url= p_e_ratio, num_pages=20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "p/e_ratio": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/p_e_ratio.csv", index= False)
    else:
        return None



def scrape_company_data_for_dividend(base_url= dividend, num_pages= 20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "Dividend": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/dividend.csv", index= False)
    else:
        return None





def scrape_company_data_for_operating_margin(base_url = operating_margin, num_pages= 20):
    all_data = []  # List to store data from all pages
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'default-table table marketcap-table dataTable'})

        if table:
            name_tds = table.find_all('td', {'class': 'name-td'})
            td_right_elements = table.find_all(lambda tag: tag.name == 'td' and 'td-right' in tag.get('class', []))
            
            td_right_text = [td.text.strip() for td in td_right_elements]
            market_cap =[]
            for i in range(1,len(td_right_text),3):
                market_cap.append(td_right_text[i])
            
            company_names = [td.find('div', {'class': 'company-name'}).text.strip() for td in name_tds]
            company_code = [td.find('div', {'class': 'company-code'}).text.strip() for td in name_tds]
            
            dic = pd.DataFrame({"company_names":  company_names, "company_code": company_code, "operating_margin": market_cap})
            all_data.append(dic)
        else:
            print(f"Table not found on page {page}.")
    
    if all_data:
        df= pd.concat(all_data, ignore_index=True)
        df.to_csv(data_directory_scrapped + "/operating_margin.csv", index= False)
    else:
        return None
    
    
    


def combine_csv(folder_path):
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    merged_df = pd.DataFrame()
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on=['company_names', "company_code"], how='left')
    merged_df.to_csv(data_directory_scrapped + '/merged_data.csv', index=False)
    
    

