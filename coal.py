import requests

url = "https://vipmbr.cpc.com.tw/mbwebs/showhistoryprice_oil.aspx"

r = requests.get(
    url,
    timeout=60,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("status =", r.status_code)

html = r.text

print("MyGridView =", html.find("MyGridView"))
print("低硫 =", html.find("低硫"))
print("0.5 =", html.find("0.5"))
