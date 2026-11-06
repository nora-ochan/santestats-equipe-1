# Convertir les glycémies exprimées en g/L

**Pour : membre A** (partie 2)

## Contexte

Le rapport signale 6 glycémies « dans une unité non prise en charge » : certains laboratoires
rendent la glycémie en **g/L**. Elles sont aujourd'hui ignorées.

## À faire

- [ ] Dans `santestats/glycemie.py`, ajouter l'unité `"g/L"` au dictionnaire `FACTEURS_VERS_MG_DL`
      (1 g/L = 100 mg/dL).
- [ ] Dans `tests/test_glycemie.py`, ajouter un test `test_g_l_vers_mg_dl`
      **juste après** `test_mmol_vers_mg_dl` : 1,26 g/L doit donner 126.0 mg/dL.
- [ ] Ajouter une ligne dans `CHANGELOG.md`, section « Non publié ».

## Critère de fin

`pytest` passe et `python -m santestats` affiche `Glycémies converties en mg/dL : 40 / 40`,
sans ligne « Attention ».
