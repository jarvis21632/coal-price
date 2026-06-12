import requests
import re

url = "https://tradingeconomics.com/commodity/coal"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = r.text

match = re.search(
    r'Coal rose to ([0-9.]+) USD/T',
    html
)

if match:
    print("煤價 =", match.group(1))
else:
    print("找不到煤價")
