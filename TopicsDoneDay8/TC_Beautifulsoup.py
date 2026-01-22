import requests
from bs4 import BeautifulSoup
import json

url="https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url, timeout=10)

soup = BeautifulSoup(response.text, "lxml")

title = soup.title.string.strip() if soup.title else None

print(title)

links = []
for link in soup.find_all("a", href=True):
    links.append(link["href"])

print("Total Links:", len(links))

tabledata=[]
table= soup.find("table")
if table:
    rows= table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        rowdata= [col.string for col in columns]
        print(rowdata)
        tabledata.append(rowdata)
ext_data={
    "Page_title":title,
    "Total Links":len(links),
    "Links":links,
    "table_data":tabledata
}
with open("ext_data.json","w") as f:
    json.dump(ext_data,f,indent=4)


