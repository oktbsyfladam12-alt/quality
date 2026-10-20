from playwright.sync_api import sync_playwright, expect


def test_dengan_bukti_video():
    with sync_playwright() as p:
        # NYALAIN KAMERA BOS! RECORD VIDEO!
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="videos/",  # video bakal kesimpen di folder videos/
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()

        # NYALAIN TRACE - buat liat step by step kalo gagal
        context.tracing.start(screenshots=True, snapshots=True)

        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        expect(page.get_by_text("Products")).to_be_visible()

        # SCREENSHOT BUKTI 1: Udah login
        page.screenshot(path="bukti_1_login.png", full_page=True)
        print("📸 Screenshot 1: Bukti login berhasil!")

        page.get_by_role("button", name="Add to cart").first.click()
        page.locator(".shopping_cart_link").click()
        page.get_by_role("button", name="Checkout").click()

        page.get_by_placeholder("First Name").fill("Budi")
        page.get_by_placeholder("Last Name").fill("Desa")
        page.get_by_placeholder("Zip/Postal Code").fill("12345")
        page.get_by_role("button", name="Continue").click()

        # SCREENSHOT BUKTI 2: Sebelum finish, cek total harga
        page.screenshot(path="bukti_2_checkout.png")
        print("📸 Screenshot 2: Bukti checkout!")

        page.get_by_role("button", name="Finish").click()

        expect(page.get_by_text("Thank you for your order!")).to_be_visible()

        # SCREENSHOT BUKTI 3: Final
        page.screenshot(path="bukti_3_sukses.png")
        print("📸 Screenshot 3: Bukti order sukses!")

        # SIMPEN TRACE + VIDEO
        context.tracing.stop(path="trace.zip")
        print("🎬 Video kesimpen di folder videos/")
        print("🔍 Trace kesimpen di trace.zip - bisa di upload ke https://trace.playwright.dev")

        page.wait_for_timeout(2000)
        browser.close()
        context.close()