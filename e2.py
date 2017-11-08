import requests
import bs4
import csv

main_url = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
resp = requests.get(main_url)
html = resp.content
soup = bs4.BeautifulSoup(html, 'html.parser')

row1 = soup.find_all("tr", "election_item")

lastyear= row1[0]

url_template = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for x in row1:
    year=x.td.text
    year_id=x['id'][-5:]

    url_download = url_template.replace("{}", year_id)

    resp = requests.get(url_download)

    file_name = "president_general_" + year + ".csv"
    with open (file_name, "w") as out:
        out.write(resp.text)
