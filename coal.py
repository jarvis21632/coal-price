from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://www.cpc.com.tw/cp.aspx?n=53",
        wait_until="networkidle",
        timeout=120000
    )

    print("TITLE =", page.title())

    content = page.content()

    print("低硫 =", content.find("低硫燃料油"))
    print("0.5 =", content.find("0.5"))
    print("KL =", content.find("KL"))

    browser.close()

然後把 coal.yml 裡的：

- run: python coal.py

改成：

- run: python coal.py

（不用改，其實保持原樣即可）

再 Run Workflow 一次。

我要看結果類似：

TITLE = 汽、柴、燃油歷史價格
低硫 = 12345
0.5 = 12350
KL = 12360

或：

低硫 = -1

如果成功找到：

低硫燃料油

下一步我就直接幫你抓：

最新日期
最新價格

例如：

2026/6/6
20402

之後再接回 LINE。

目前最大的關卡（GitHub、Actions、Playwright、LINE）其實都已經過了。現在只是在從表格裡拿數字而已。
