import pytest

from pages.login_page import LoginPage


@pytest.mark.e2e
def test_login_com_credenciais_validas(page, credenciais):
    login = LoginPage(page)

    login.acessar()
    login.realizar_login(credenciais["email"], credenciais["password"])

    assert login.usuario_logado()
