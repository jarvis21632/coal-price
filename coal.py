import requests

url = "https://www.cpc.com.tw/cp.aspx?n=53"

r = requests.get(url, timeout=60)

html = r.text

print("table =", html.find("<table"))
print("tbody =", html.find("<tbody"))
print("低硫 =", html.find("低硫"))
print("燃料油 =", html.find("燃料油"))
print("KL =", html.find("KL"))
