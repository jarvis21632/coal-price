from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://en.macromicro.me/series/3617/ice-newcastle-coal-futures",
        wait_until="domcontentloaded",
        timeout=30000
    )

    print("TITLE =", page.title())

    print(page.content()[:3000])

    browser.close()
