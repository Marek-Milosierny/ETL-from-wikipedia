from bs4 import BeautifulSoup
import pandas as pd
import requests

wiki_url = 'https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2022-01-01'


def gather_webpage_content(url):
    html_data = requests.get(url).text
    return html_data


def table_scraper():
    soup=BeautifulSoup(gather_webpage_content(wiki_url), "html.parser")
    body = soup.body
    tables = body.find_all("table")
    return tables


def extract():
    tables_list = table_scraper()
    table_index = 3
    data = pd.read_html(str(tables_list[table_index]), flavor="bs4")[0]
    return data


def extract_currency(currency):
    url = "https://api.apilayer.com/exchangerates_data/latest?&base=USD"

    payload = {}
    headers= {
    "apikey": "****************" # apikey from apilayer.com
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    data = pd.DataFrame.from_dict(result)
    exchange_rates = data.drop(data.columns[[0,1,2,3]], axis=1)
    exchange_rate = exchange_rates.loc[currency, "rates"]
    return exchange_rate


