import bs4
from bs4 import BeautifulSoup
import requests
import re

main_url='http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
resp=requests.get(main_url)
html=resp.content
soup=bs4.BeautifulSoup(html, 'html.parser')

row1=soup.find_all("tr", "election_item")

lastyear= row1[0]
lastyear['id']

for x in row1:
    year=x.td.text
    year_id=x['id'][-5:]
    print(year, year_id, file=open('ELECTION_ID', 'a'))
