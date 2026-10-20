from playwright.sync_api import sync_playwright

def test_buka_google():
    with sync_playwright() as p:

        #1. buka chrome
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        #2. pergi ke google
        page.goto("https://www.google.com")

        #3. buktiin judulnya ada kata Google
        assert "Google" in page.title()

        print("Berhasil Buka google bosss!")
        browser.close()