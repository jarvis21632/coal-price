import os
import requests

token = os.environ["LINE_TOKEN"]
user_id = os.environ["LINE_USER_ID"]

url = "https://api.line.me/v2/bot/message/push"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

payload = {
    "to": user_id,
    "messages": [
        {
            "type": "text",
            "text": "🚀 GitHub 發送 LINE 測試成功"
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
