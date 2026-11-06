import pytest

from santestats.imc import calculer_imc, classer_imc


def test_calculer_imc():
    assert calculer_imc(70, 175) == 22.9


def test_calculer_imc_refuse_valeurs_negatives():
    with pytest.raises(ValueError):
        calculer_imc(-70, 175)


def test_classer_insuffisance_ponderale():
    assert classer_imc(17.9) == "Insuffisance pondérale"


def test_classer_corpulence_normale():
    assert classer_imc(22.0) == "Corpulence normale"


def test_classer_surpoids():
    assert classer_imc(27.5) == "Surpoids"


def test_classer_obesite():
    assert classer_imc(32.0) == "Obésité"
