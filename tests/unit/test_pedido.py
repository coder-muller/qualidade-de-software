import pytest

from src.pedido import calcular_total_pedido


@pytest.mark.unit
def test_total_valido_acima_do_minimo():
    itens = [{"nome": "Hamburguer", "preco": 25.0}, {"nome": "Suco", "preco": 10.0}]
    assert calcular_total_pedido(itens, valor_minimo=30.0) == 35.0


@pytest.mark.unit
def test_total_abaixo_do_minimo_deve_falhar():
    itens = [{"nome": "Agua", "preco": 5.0}]
    with pytest.raises(ValueError, match="Valor minimo"):
        calcular_total_pedido(itens, valor_minimo=20.0)


@pytest.mark.unit
def test_lista_vazia_deve_falhar():
    with pytest.raises(ValueError, match="pelo menos um item"):
        calcular_total_pedido([], valor_minimo=10.0)


@pytest.mark.unit
def test_preco_negativo_deve_falhar():
    itens = [{"nome": "Item", "preco": -5.0}]
    with pytest.raises(ValueError, match="Preco invalido"):
        calcular_total_pedido(itens, valor_minimo=10.0)


@pytest.mark.unit
def test_item_sem_preco_deve_falhar():
    itens = [{"nome": "Item sem preco"}]
    with pytest.raises(ValueError, match="sem preco"):
        calcular_total_pedido(itens, valor_minimo=10.0)
