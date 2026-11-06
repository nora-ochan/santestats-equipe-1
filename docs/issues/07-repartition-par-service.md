# Bonus : ajouter la répartition par service au rapport

**Pour : qui a terminé** (bonus)

## À faire

- [ ] Dans `santestats/rapport.py`, ajouter à la fin du rapport une section
      « Répartition par service » : nombre de patients et IMC moyen par service.
- [ ] Ajouter un test dans un nouveau fichier `tests/test_rapport.py`.
- [ ] Ajouter une ligne dans `CHANGELOG.md`, section « Non publié ».
- [ ] Avant d'ouvrir la PR, mettre la branche à jour avec `git rebase origin/main`
      plutôt qu'avec un merge, puis pousser (`git push --force-with-lease`).

## Critère de fin

`pytest` passe ; l'historique de la branche est linéaire au-dessus de `main`.
