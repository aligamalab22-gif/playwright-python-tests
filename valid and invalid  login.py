
from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://www.saucedemo.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    page = browser.new_page()

    # Scenario 1: Invalid Login
    page.goto(LOGIN_URL)

    page.locator("#user-name").fill("invalid_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    expect(page.locator('[data-test="error"]')).to_be_visible()

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )

    print("Scenario 1 Passed: Invalid Login")

    # Scenario 2: Valid Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.locator(".title")).to_have_text("Products")

    print("Scenario 2 Passed: Valid Login")

    # Scenario 3: Add Product to Cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    print("Scenario 3 Passed: Add Product to Cart")

    # Scenario 4: Verify Product in Cart
    page.locator(".shopping_cart_link").click()

    expect(page.locator(".inventory_item_name")).to_have_text(
        "Sauce Labs Backpack"
    )

    print("Scenario 4 Passed: Product Found in Cart")

    browser.close()
