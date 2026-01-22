from bs4 import BeautifulSoup
import requests,json

url="https://www.geeksforgeeks.org/html/html-tables"

response=requests.get(url)
response.raise_for_status()

soup=BeautifulSoup(response.text,"lxml")
page_title=soup.title.string.strip() if soup.title else None
print(page_title)

links=[]
for link in soup.find_all('a',href=True):
    links.append(link['href'])

table_data = []
table = soup.find("table")
if table:
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all(["th", "td"])
        row_data = [col.get_text(strip=True) for col in columns]
        if row_data:
            table_data.append(row_data)


extracted_data = {
    "page_title": page_title,
    "total_links": len(links),
    "links": links,
    "table_data": table_data,
}

with open("extracted_data.json", "w", encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4, ensure_ascii=False)

print("data extracted and saved to extracted_data.json")