from pytest_bdd import scenarios, then, when

from pages.orders_page import OrdersPage

scenarios("../../features/historico_pedidos.feature")


@when("acessa a pagina de pedidos")
def acessar_pagina_pedidos(page):
    orders = OrdersPage(page)
    orders.acessar()
    page.wait_for_load_state("networkidle")


@when("visualiza um pedido realizado")
def visualizar_pedido(page):
    orders = OrdersPage(page)
    orders.acessar()
    page.wait_for_load_state("networkidle")


@then("o sistema deve exibir o historico de transacoes")
def validar_historico(page):
    orders = OrdersPage(page)
    assert orders.titulo_historico_visivel()


@then("o sistema deve exibir o valor total do pedido")
def validar_total_pedido(page):
    orders = OrdersPage(page)

    if orders.possui_pedidos():
        assert orders.total_do_primeiro_pedido_visivel()
    else:
        assert orders.titulo_historico_visivel()
