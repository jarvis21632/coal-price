import requests

url = "https://www.cpc.com.tw/cp.aspx?n=53"

r = requests.get(url, timeout=30)

html = r.text

print("status =", r.status_code)

keyword = "低硫燃料油"

idx = html.find(keyword)

print("keyword position =", idx)

if idx == -1:
    print("找不到關鍵字")
else:
    start = max(0, idx - 1000)
    end = min(len(html), idx + 3000)
    print(html[start:end])
