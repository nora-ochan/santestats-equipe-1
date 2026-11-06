import pytest

from santestats.glycemie import convertir_en_mg_dl


def test_mg_dl_inchange():
    assert convertir_en_mg_dl(110, "mg/dL") == 110.0


def test_mmol_vers_mg_dl():
    assert convertir_en_mg_dl(7.0, "mmol/L") == 126.1


def test_unite_inconnue():
    with pytest.raises(ValueError):
        convertir_en_mg_dl(1.1, "unités")
