import requests
import pandas as pd
from bs4 import BeautifulSoup
import configparser
import sys


if len(sys.argv) > 1 and sys.argv[1] == "FILE":
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config['input']['url']
else:
    url = input("Enter website URL: ")

#url="https://www.census2011.co.in/states.php"
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
data = []
table = soup.find("table")

#table header
table_headers=table.find_all('th')
data.append([th.text for th in table_headers])

#table row
table_rows=table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    if(len(td)>0):
        row=[tr.text for tr in td]
        data.append(row)

df=pd.DataFrame(data)
df.to_csv('census_data.csv')