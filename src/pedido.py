"""Regras de negocio para calculo do total do pedido."""


def calcular_total_pedido(itens: list[dict], valor_minimo: float) -> float:
    if not itens:
        raise ValueError("O pedido deve ter pelo menos um item")

    total = 0.0

    for item in itens:
        if "preco" not in item:
            raise ValueError("Item sem preco")

        preco = item["preco"]

        if preco < 0:
            raise ValueError("Preco invalido")

        total += preco

    if total < valor_minimo:
        raise ValueError("Valor minimo do pedido nao atingido")

    return total
