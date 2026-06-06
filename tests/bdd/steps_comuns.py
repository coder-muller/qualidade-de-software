from pytest_bdd import given

from pages.login_page import LoginPage


@given("que o usuario esta autenticado no sistema")
def usuario_autenticado_no_sistema(page, credenciais):
    login = LoginPage(page)
    login.acessar()
    login.realizar_login(credenciais["email"], credenciais["password"])
    assert login.usuario_logado()
