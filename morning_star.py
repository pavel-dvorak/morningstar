from bs4 import BeautifulSoup
from urllib.parse import unquote
import requests
import lxml

urls = ["https://www.morningstar.co.uk/uk/etf/snapshot/snapshot.aspx?id=0P0000M7SM"]

for url in urls:
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, "html.parser")
  #print(soup.prettify())
  id = url.split('=')[1]
  f_name = soup.title.text

  allrows = soup.findAll('tr')
  for row in allrows:
    if row.get_text().find('Ongoing Charge') > -1 : # Ongoing Charge #Bid
      cells = row.findAll("td")
      column=(cells[0].text)
      value=(cells[2].text)
      print(id , column, value, f_name )
