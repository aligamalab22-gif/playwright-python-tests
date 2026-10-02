"""
اختبار: تسجيل الدخول ثم التأكد إن عنصري "Search" و "Sell your product" ظاهرين في صفحة الإشعارات
"""

import os
from playwright.sync_api import sync_playwright, expect

LOGIN_URL = "https://on-ruf-uat.vercel.app/login" 
NOTIFICATIONS_URL = "https://on-ruf-uat.vercel.app/notifications"

EMAIL = os.environ.get("TEST_EMAIL", "your_email@example.com")
PASSWORD = os.environ.get("TEST_PASSWORD", "your_password")


def test_login_then_search_and_sell_product_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()

        # افتح صفحة تسجيل الدخول
        page.goto(LOGIN_URL)
        page.wait_for_load_state("domcontentloaded")

        page.locator("input[type='email']").fill(EMAIL)
        page.locator("input[type='password']").fill(PASSWORD)

        # دوس على زرار "Sign In"
        page.get_by_role("button", name="Sign In").click()

        page.wait_for_timeout(3000)

        
        page.goto(NOTIFICATIONS_URL)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(2000)

        search_element = page.get_by_text("Search", exact=False)
        expect(search_element.first).to_be_visible()
        print("✅ عنصر 'Search' ظاهر في الصفحة")

        "Sell your product"
        sell_element = page.get_by_text("Sell your product", exact=False)
        expect(sell_element.first).to_be_visible()
        print("✅ عنصر 'Sell your product' ظاهر في الصفحة")

        auction_element = page.get_by_text("Auction", exact=False)
        expect(auction_element.first).to_be_visible()
        print("✅ زرار 'Auction' ظاهر في الصفحة")

        browser.close()
