
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )

    print("Test Passed: Invalid Login")

    browser.close()
