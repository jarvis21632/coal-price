import requests
import re
import os
from bs4 import BeautifulSoup
from datetime import datetime

# 抓 TradingEconomics 煤價
def get_coal_price():

    url = "https://tradingeconomics.com/commodity/coal"

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    html = r.text

    # print("開始找煤價...")

    matches = re.findall(
        r'([0-9]+\.[0-9]+)\s*USD/T',
        html
    )

    # print("找到的價格:", matches[:10])

    if matches:
        return matches[0]

    return "N/A"


# 抓中油低硫燃料油
def get_cpc_price():
    url = "https://vipmbr.cpc.com.tw/mbwebs/showhistoryprice_oil.aspx"

    r = requests.get(
        url,
        timeout=60,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table", {"id": "MyGridView"})

    if table is None:
        return "N/A", "N/A"

    rows = table.find_all("tr")

    headers = []
    for th in rows[0].find_all("th"):
        headers.append(th.get_text(strip=True))

    target_col = None
    for i, h in enumerate(headers):
        if "低硫燃料油(0.5%)(KL)" in h:
            target_col = i
            break

    if target_col is None:
        return "N/A", "N/A"

    for row in rows[1:]:
        cols = row.find_all(["td", "th"])

        if len(cols) <= target_col:
            continue

        date = cols[0].get_text(strip=True)
        value = cols[target_col].get_text(strip=True)

        if value:
            return date, value

    return "N/A", "N/A"


# LINE 推播
def send_line(message):
    token = os.environ["LINE_TOKEN"]
    user_id = os.environ["LINE_USER_ID"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    r = requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=payload
    )

    print("LINE status =", r.status_code)
    print(r.text)


# 主程式
coal_price = get_coal_price()
oil_date, oil_price = get_cpc_price()

now = datetime.now().strftime("%Y-%m-%d %H:%M")

message = f"""📊 能源價格每日快報

🌑 澳洲煤價
{coal_price} USD/T

⛽ 低硫燃料油(0.5%)(KL)
{oil_price} 元/KL
({oil_date})

⏰ 更新時間
{now}
"""

print(message)
send_line(message)
