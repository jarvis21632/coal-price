import requests

url = "https://www.cpc.com.tw/cp.aspx?n=53"

r = requests.get(
    url,
    timeout=60,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

html = r.text

idx = html.find("燃料油")

print("position =", idx)

if idx >= 0:
    start = max(0, idx - 2000)
    end = min(len(html), idx + 4000)
    print(html[start:end])
else:
    print("找不到")
