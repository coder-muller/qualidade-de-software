"""Regras de negocio para calculo da taxa de entrega."""

TAXA_FIXA = 5.0
TAXA_POR_KM = 2.0
LIMITE_KM_TAXA_FIXA = 3.0


def calcular_taxa_entrega(distancia_km: float) -> float:
    if distancia_km < 0:
        raise ValueError("Distancia invalida")

    if distancia_km <= LIMITE_KM_TAXA_FIXA:
        return TAXA_FIXA

    km_adicionais = distancia_km - LIMITE_KM_TAXA_FIXA
    return round(TAXA_FIXA + (km_adicionais * TAXA_POR_KM), 2)
