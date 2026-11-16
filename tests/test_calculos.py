import pytest

from ai_fase1.calculos import media, soma


def test_soma():
    assert soma(2, 3) == 5

def test_media_simples():
    assert media([1, 2, 3]) == 2

def test_lista_vazia():
    with pytest.raises(ValueError):
        media([])


@pytest.mark.parametrize("valores, esperado", [([2, 4], 3), ([10], 10)])
def test_varios_casos(valores, esperado):
    assert media(valores) == esperado
