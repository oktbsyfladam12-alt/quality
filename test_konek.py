def test_koneksi():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com") # ini web paling ringan di dunia
        print(page.title())
        assert "Example" in page.title()
        browser.close()