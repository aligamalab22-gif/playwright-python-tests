from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    
    page.fill("user-name", "standard_user")
    page.fill("password", "secret_sauce")
    page.click("login-button")
    
    page.wait_for_timeout(200)  # تستنى شوية تشوف النتيجة
    browser.close()
    page.wait_for_selector(".inventory_list")