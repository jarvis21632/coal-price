import requests

url = "https://www.cpc.com.tw/cp.aspx?n=53"

r = requests.get(
    url,
    timeout=30
)

print("status =", r.status_code)
print(r.text[:5000])
