from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://en.macromicro.me/series/3617/ice-newcastle-coal-futures",
        wait_until="networkidle",
        timeout=120000
    )

    print(page.locator("span.val").all_inner_texts())

    browser.close()
