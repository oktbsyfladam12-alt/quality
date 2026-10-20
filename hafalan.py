def test_nama_test():
    # 1. SIAPIN DATA
    username = "admin"
    password = "12345"

    # 2. JALANIN AKSI / LOGIKA
    boleh_login = (username != "" and len(password) >= 5)

    # 3. BUKTIIN PAKE ASSERT
    assert boleh_login == True

