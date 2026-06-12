import os
import requests

LINE_TOKEN = os.environ["LINE_TOKEN"]
LINE_USER_ID = os.environ["LINE_USER_ID"]

message = "🚀 GitHub Actions 測試成功"

url = "https://api.line.me/v2/bot/message/push"

headers = {
"Authorization": f"Bearer {LINE_TOKEN}",
"Content-Type": "application/json"
}

payload = {
"to": LINE_USER_ID,
"messages": [
{
"type": "text",
"text": message
}
]
}

r = requests.post(
url,
headers=headers,
json=payload,
timeout=30
)

print("Status:", r.status_code)
print(r.text)
