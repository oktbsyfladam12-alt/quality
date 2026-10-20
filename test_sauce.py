from playwright.sync_api import sync_playwright, expect


def test_beli_baju_di_sauce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        # 1. LOGIN
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # FIX INI BOS - TUNGGUIN JUDULNYA MUNCUL!
        # Jangan pake content(), pake locator yang pinter nunggu
        expect(page.locator(".title")).to_have_text("Products")
        print("1. LOGIN BERHASIL BOS!")

        # 2. TAMBAH BARANG
        page.click("#add-to-cart-sauce-labs-backpack")
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
        print("2. BARANG MASUK KERANJANG!")

        # 3. CHECKOUT
        page.click(".shopping_cart_link")
        page.click("#checkout")

        page.fill("#first-name", "Budi")
        page.fill("#last-name", "Desa")
        page.fill("#postal-code", "12345")
        page.click("#continue")

        # 4. FINISH
        page.click("#finish")

        # 5. BUKTI
        expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
        print("3. ORDER BERHASIL BOS! E2E ERP SELESAI!")

        page.wait_for_timeout(3000)
        browser.close()