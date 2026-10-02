```python
from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://www.saucedemo.com/"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_login_add_remove_product():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(LOGIN_URL)
        page.wait_for_timeout(2000)

        page.locator("input[type='text']").fill(USERNAME)
        page.wait_for_timeout(2000)

        page.locator("input[type='password']").fill(PASSWORD)
        page.wait_for_timeout(2000)

        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(3000)

        expect(page.locator(".title")).to_have_text("Products")
        print("Login successful")

        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.wait_for_timeout(3000)

        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
        print("Product added to cart")

        page.locator(".shopping_cart_link").click()
        page.wait_for_timeout(3000)

        page.get_by_role("button", name="Remove").click()
        page.wait_for_timeout(3000)

        expect(page.locator(".cart_item")).to_have_count(0)
        print("Product removed from cart")

        page.wait_for_timeout(5000)

        browser.close()
```
