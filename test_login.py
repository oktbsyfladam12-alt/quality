import pytest


@pytest.mark.parametrize("username, password, harus_lulus", [
    ("admin", "12345", True),
    ("admin", "sal", False),
    ("", "", False),
    ("user_desa", "password123", True),
    ("admin", "", False),
])
def test_login_parametrize(username, password, harus_lulus):
    # simulasi login
    login_valid = (username != "" and len(password) >= 5)

    # kita cek apakah hasil robot sama dengan yang kita harapkan
    assert login_valid == harus_lulus