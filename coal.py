import requests

url = "https://www.cpc.com.tw/cp.aspx?n=41"

r = requests.get(
    url,
    timeout=60,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

html = r.text

print("status =", r.status_code)

keyword = "低硫"

idx = html.find(keyword)

print("keyword position =", idx)

if idx == -1:
    print("找不到關鍵字")
else:
    start = max(0, idx - 2000)
    end = min(len(html), idx + 5000)
    print(html[start:end])
