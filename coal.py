import requests

try:
    url = "https://www.cpc.com.tw/cp.aspx?n=53"

    r = requests.get(
        url,
        timeout=60,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("status =", r.status_code)

    html = r.text

    keyword = "低硫燃料油"

    idx = html.find(keyword)

    print("keyword position =", idx)

    if idx == -1:
        print("找不到關鍵字")
    else:
        start = max(0, idx - 1000)
        end = min(len(html), idx + 3000)
        print(html[start:end])

except Exception as e:
    print("ERROR =", str(e))
