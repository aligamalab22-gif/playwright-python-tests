
from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://www.saucedemo.com/"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login_and_add_product_to_cart():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        page.goto(
            LOGIN_URL,
            wait_until="domcontentloaded",
            timeout=30000
        )

        page.locator("#user-name").fill(USERNAME)
        page.locator("#password").fill(PASSWORD)
        page.locator("#login-button").click()

        page.wait_for_url(
            "**/inventory.html",
            timeout=30000
        )

        expect(page.locator(".title")).to_have_text("Products")

        print("Login successful")

        page.locator(".inventory_item").first.locator(
            "button"
        ).click()

        print("Product added to cart")

        cart_badge = page.locator(".shopping_cart_badge")
        expect(cart_badge).to_have_text("1")

        print("Cart contains one product")

        page.locator(".shopping_cart_link").click()

        expect(page.locator(".title")).to_have_text("Your Cart")

        print("Cart page opened")

        page.wait_for_timeout(10000)

        browser.close()


if __name__ == "__main__":
    login_and_add_product_to_cart()
