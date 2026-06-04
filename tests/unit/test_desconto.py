import pytest

from src.desconto import aplicar_desconto


@pytest.mark.unit
def test_sem_desconto():
    assert aplicar_desconto(100.0, 0) == 100.0


@pytest.mark.unit
def test_desconto_parcial():
    assert aplicar_desconto(100.0, 50) == 50.0


@pytest.mark.unit
def test_desconto_total():
    assert aplicar_desconto(80.0, 100) == 0.0


@pytest.mark.unit
def test_percentual_acima_de_cem_deve_falhar():
    with pytest.raises(ValueError, match="Percentual"):
        aplicar_desconto(100.0, 110)


@pytest.mark.unit
def test_percentual_negativo_deve_falhar():
    with pytest.raises(ValueError, match="Percentual"):
        aplicar_desconto(100.0, -10)
