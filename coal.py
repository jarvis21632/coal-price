import requests

url = "https://tradingeconomics.com/commodity/coal"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

print("status =", r.status_code)
print(r.text[:3000])
