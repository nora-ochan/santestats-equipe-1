# Détailler l'obésité en trois classes

**Pour : membre D** (partie 2 ; en trinôme, le membre C la prend après l'issue 3)

## Contexte

La classification de l'OMS distingue trois classes d'obésité. Le rapport n'en affiche qu'une.

## À faire

- [ ] Dans `classer_imc` (`santestats/imc.py`), remplacer la catégorie unique `"Obésité"` par :
  - `"Obésité modérée"` pour un IMC de 30 à moins de 35 (classe I) ;
  - `"Obésité sévère"` de 35 à moins de 40 (classe II) ;
  - `"Obésité massive"` à partir de 40 (classe III).
- [ ] Dans `tests/test_imc.py`, mettre à jour `test_classer_obesite` (32.0 donne `"Obésité modérée"`)
      et ajouter un test pour chacune des deux autres classes.
- [ ] Ajouter une ligne dans `CHANGELOG.md`, section « Non publié ».

## Critère de fin

`pytest` passe ; le rapport affiche les trois classes d'obésité.
