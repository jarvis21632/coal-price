import requests
from bs4 import BeautifulSoup

url = "https://vipmbr.cpc.com.tw/mbwebs/showhistoryprice_oil.aspx"

r = requests.get(
    url,
    timeout=60,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

soup = BeautifulSoup(r.text, "html.parser")

table = soup.find("table", {"id": "MyGridView"})

rows = table.find_all("tr")

headers = []

for th in rows[0].find_all("th"):
    headers.append(th.get_text(strip=True))

target_col = None

for i, h in enumerate(headers):
    if "低硫燃料油(0.5%)(KL)" in h:
        target_col = i
        break

print("欄位位置 =", target_col)

for row in rows[1:]:

    cols = row.find_all(["td", "th"])

    if len(cols) <= target_col:
        continue

    date = cols[0].get_text(strip=True)
    value = cols[target_col].get_text(strip=True)

    if value:
        print("日期 =", date)
        print("價格 =", value)
        break
