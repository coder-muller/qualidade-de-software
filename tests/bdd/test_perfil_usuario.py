from pytest_bdd import scenarios, then, when

from pages.profile_page import ProfilePage

scenarios("../../features/perfil_usuario.feature")


@when("acessa a pagina de perfil")
def acessar_perfil(page):
    profile = ProfilePage(page)
    profile.acessar()
    page.wait_for_load_state("networkidle")


@then("o sistema deve exibir o nome do usuario")
def validar_nome_usuario(page):
    profile = ProfilePage(page)
    assert profile.nome_usuario_visivel()


@then("o sistema deve exibir a secao de restaurantes favoritos")
def validar_secao_favoritos(page):
    profile = ProfilePage(page)
    assert profile.secao_favoritos_visivel()
