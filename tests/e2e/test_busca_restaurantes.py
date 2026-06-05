import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.e2e
def test_busca_por_termo_retorna_restaurantes(page, credenciais):
    login = LoginPage(page)
    home = HomePage(page)

    login.acessar()
    login.realizar_login(credenciais["email"], credenciais["password"])

    home.buscar("Sabor")
    home.aguardar_restaurantes()

    assert home.quantidade_restaurantes_visiveis() > 0
    assert home.restaurantes_contem_texto("Sabor")


@pytest.mark.e2e
def test_filtro_por_culinaria_italiana(page, credenciais):
    login = LoginPage(page)
    home = HomePage(page)

    login.acessar()
    login.realizar_login(credenciais["email"], credenciais["password"])

    home.filtrar_por_culinaria("Italiana")
    home.aguardar_restaurantes()

    assert home.quantidade_restaurantes_visiveis() > 0
    assert home.restaurantes_contem_texto("Italiana")
