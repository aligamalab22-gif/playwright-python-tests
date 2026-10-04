from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://www.saucedemo.com/"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,
    slow_mo=500)
    page = browser.new_page()

    # 1. Open website
    page.goto(LOGIN_URL)

    # 2. Login
    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    # Verify login
    expect(page.locator(".title")).to_have_text("Products")

    # 3. Add product to cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Verify cart badge
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # 4. Open cart
    page.locator(".shopping_cart_link").click()

    # Verify product is in cart
    expect(page.locator(".inventory_item_name")).to_have_text(
        "Sauce Labs Backpack"
    )

    # 5. Checkout
    page.locator("#checkout").click()

    # 6. Fill checkout information
    page.locator("#first-name").fill("Ali")
    page.locator("#last-name").fill("Gamal")
    page.locator("#postal-code").fill("35511")

    page.locator("#continue").click()

    # 7. Verify checkout overview
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # 8. Finish purchase
    page.locator("#finish").click()

    # 9. Verify successful order
    expect(page.locator(".complete-header")).to_have_text(
        "Thank you for your order!"
    )

    print("✅ Test Passed: Order completed successfully")

    browser.close()
