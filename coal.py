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
