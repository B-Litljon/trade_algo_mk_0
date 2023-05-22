import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def gecko_scrapr():
    headers= {
        'User-Agent': 'Mozilla/5.0 (Mac NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    base_url = "https://www.coingecko.com"

    tables = []

    while True:
        print(f'requesting data from: {base_url}')
        # the first 3 tables on coingecko
        for i in range(1, 4):
            print('Processing page {0}'.format(i))
            params = {
                'page': i
            }
            response = requests.get(base_url, headers=headers, params=params)
            soup = BeautifulSoup(response.content, 'html.parser')
        
            table = soup.find('table', {'class': 'table-scrollable'})
            table_list = pd.read_html(str(table))
        
            tables.extend(table_list) 

        master_table = pd.concat(tables)
        master_table = master_table.loc[:, master_table.columns[1:-1]]
        #master_table.to_csv('Gecko_data.csv', index=False)
        print(master_table)

        for remaining in range(300, 0, -1):
            print(f'Next request in {remaining} seconds...', end ='\r')
            time.sleep(1)

gecko_scrapr()