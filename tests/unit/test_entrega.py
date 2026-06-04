import pytest

from src.entrega import calcular_taxa_entrega


@pytest.mark.unit
def test_distancia_ate_tres_km_taxa_fixa():
    assert calcular_taxa_entrega(2.0) == 5.0


@pytest.mark.unit
def test_distancia_exatamente_tres_km_taxa_fixa():
    assert calcular_taxa_entrega(3.0) == 5.0


@pytest.mark.unit
def test_distancia_acima_de_tres_km_com_adicional():
    assert calcular_taxa_entrega(5.0) == 9.0


@pytest.mark.unit
def test_distancia_negativa_deve_falhar():
    with pytest.raises(ValueError, match="Distancia invalida"):
        calcular_taxa_entrega(-1.0)
