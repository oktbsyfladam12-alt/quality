from playwright.sync_api import sync_playwright, expect


def test_level_dewa():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        # LEVEL 4 BOS! GAK PAKE TITIK PAGAR LAGI!

        # 1. LOGIN - Cari input berdasarkan placeholder / label, bukan id
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        # Cari tombol berdasarkan peran (role=button) dan namanya
        page.get_by_role("button", name="Login").click()

        # 2. CEK MASUK - Cari judul berdasarkan teks
        expect(page.get_by_text("Products")).to_be_visible()
        print("1. LOGIN DEWA BERHASIL!")

        # 3. TAMBAH BARANG - Cari tombol yang namanya Add to cart
        page.get_by_role("button", name="Add to cart").first.click()
        print("2. BARANG MASUK!")

        # 4. KE KERANJANG - Cari link keranjang
        # 4. KE KERANJANG - Badge "1" itu bukan link, dia di dalam link
        # Jadi kita klik wadahnya aja yang pasti ada
        page.locator(".shopping_cart_link").click()
        # atau lebih aman:
        # page.locator(".shopping_cart_link").click()

        page.get_by_role("button", name="Checkout").click()

        # 5. ISI FORM - Pake placeholder lagi, anti id!
        page.get_by_placeholder("First Name").fill("Budi")
        page.get_by_placeholder("Last Name").fill("Desa")
        page.get_by_placeholder("Zip/Postal Code").fill("12345")

        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Finish").click()

        # 6. CEK SUKSES
        expect(page.get_by_text("Thank you for your order!")).to_be_visible()
        print("3. E2E DEWA SELESAI BOS! LU UDAH LEVEL SENIOR!")

        page.wait_for_timeout(3000)
        browser.close()