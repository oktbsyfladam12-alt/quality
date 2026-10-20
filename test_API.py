from playwright.sync_api import sync_playwright, expect


def test_api_login_erp():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        print("1. tes api login...")
        response = page.request.post("https://dummyjson.com/auth/login",
                                     data={"username": "emilys", "password": "emilyspass"})
        print(f"Status : {response.status}")
        assert response.status == 200

        body = response.json()

        print(f"Token : {body['accessToken'][:30]}...")
        token = body['accessToken']
        print("Login API berhasil")

        print("\n2. ngetes API ambil data...")
        response = page.request.get("https://dummyjson.com/auth/me",
                                    headers={"Authorization": f"Bearer {token}"})
        print(f"Status GET: {response.status}")
        assert response.status == 200

        data = response.json()

        print(f"User: {data['firstName']} {data['lastName']}")
        print(f"Email: {data['email']}")
        print("ambil data berhasil!")

        print("\n3. Ngetes API Input Data Baru...")
        response = page.request.post("https://dummyjson.com/products/add",
                                     data={
                                         "title": "Panen Padi Budi",
                                         "description": "Panen Desa 500kg",
                                         "price": 500
                                     },
                                     headers={"Authorization": f"Bearer {token}"}
                                     )
        print(f"Status CREATE: {response.status}")

        assert response.status in [200, 201]
        created = response.json()
        print(f"Data dibuat! ID: {created['id']}, Title: {created['title']}")
        print("create data berhasil")

        browser.close()
        print("beres")