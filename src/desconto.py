"""Regras de negocio para aplicacao de desconto percentual."""


def aplicar_desconto(valor_total: float, percentual: float) -> float:
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual de desconto invalido")

    if valor_total < 0:
        raise ValueError("Valor total invalido")

    valor_com_desconto = valor_total * (1 - percentual / 100)

    if valor_com_desconto < 0:
        raise ValueError("Valor final nao pode ser negativo")

    return round(valor_com_desconto, 2)
