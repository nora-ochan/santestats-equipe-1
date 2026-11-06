# Distinguer l'obésité morbide (IMC >= 40)

**Pour : membre C** (partie 2)

## Contexte

Le service d'endocrinologie veut repérer à part les patients dont l'IMC atteint 40 ou plus.

## À faire

- [ ] Dans `classer_imc` (`santestats/imc.py`), renvoyer `"Obésité morbide"` quand l'IMC est
      supérieur ou égal à 40 ; les IMC de 30 à 40 restent `"Obésité"`.
- [ ] À la fin de `tests/test_imc.py`, ajouter un test : un IMC de 41.0 donne `"Obésité morbide"`.
- [ ] Ajouter une ligne dans `CHANGELOG.md`, section « Non publié ».

## Critère de fin

`pytest` passe ; le rapport affiche une ligne `Obésité morbide`.
