# Isoler le seuil d'hyperglycémie dans une fonction

**Pour : membre B** (partie 2)

## Contexte

Le seuil de 126 mg/dL (1,26 g/L, glycémie à jeun) est écrit en dur dans `rapport.py`.
Un seuil clinique doit être nommé et testé à un seul endroit.

## À faire

- [ ] À la **fin** de `santestats/glycemie.py`, ajouter une constante `SEUIL_DIABETE_MG_DL = 126`
      et une fonction `est_hyperglycemie(valeur_mg_dl: float) -> bool`
      (vraie si la valeur est supérieure ou égale au seuil).
- [ ] Dans `santestats/rapport.py`, remplacer `g >= 126` par `est_hyperglycemie(g)`
      (et compléter l'import).
- [ ] À la **fin** de `tests/test_glycemie.py`, ajouter deux tests : 126 est une hyperglycémie,
      125.9 n'en est pas une. Compléter l'import en haut du fichier.
- [ ] Ajouter une ligne dans `CHANGELOG.md`, section « Non publié ».

## Critère de fin

`pytest` passe ; le rapport affiche le même nombre de glycémies >= 126 mg/dL qu'avant.
