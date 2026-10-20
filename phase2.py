from playwright.sync_api import sync_playwright

def test_cari_kampus_desa():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.bing.com", timeout=60000)
        #cari
        page.fill("textarea[name=q]", "kampus desa")
        page.keyboard.press("Enter")
        #tunggu bentar biar keliatan ga langsung close
        page.wait_for_timeout(3000)

        assert "kampus desa" in page.content().lower()
        print("berhasil cari kampus desa")
        browser.close()