# Importing necessary libraries 
import sys
import configparser
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Creating option of either taking url input from config file or taking input from user in terminal 
if len(sys.argv) > 1 and sys.argv[1] == "FILE": # If user types py census.py FILE in terminal, input from config file is taken.   
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config['input']['url']
else:
    url = input("Enter website URL: ")  # User is asked to enter the url "https://www.census2011.co.in/states.php"

# Using Beautiful Soup to web scrape census data  
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
data = [] 
table = soup.find("table") #finding the required table on the webpage

# scraping table header
table_headers=table.find_all('th')
data.append([th.text for th in table_headers])

# scraping data in table rows
table_rows=table.find_all('tr')
for tr in table_rows: # for loop is used to scrape data from each row 
    td=tr.find_all('td')
    if(len(td)>0):
        row=[tr.text for tr in td]
        data.append(row)

# Creating dataframe to store data and exporting it into a csv file. 
df=pd.DataFrame(data)
df.to_csv('census_data.csv')