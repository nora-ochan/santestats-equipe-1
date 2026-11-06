# Règles de contribution

Ces règles décrivent le workflow de l'équipe. Elles sont volontairement simples :
c'est le **GitHub flow** (une branche par tâche, fusion dans `main` par pull request).

## 1. Une tâche = une issue = une branche

- Toute modification part d'une **issue** GitHub, assignée à une personne.
- La branche porte le numéro de l'issue et une description courte, en minuscules :
  `1-conversion-g-l`, `4-classes-obesite-oms`.
- On part toujours d'un `main` à jour :

```bash
git switch main
git pull
git switch -c 1-conversion-g-l
```

## 2. Des commits petits et bien nommés

Un commit = un changement cohérent. Le message suit la convention *Conventional Commits* :

```
<type>: <description à l'infinitif, en minuscules>
```

| Type | Usage |
|---|---|
| `feat` | nouvelle fonctionnalité |
| `fix` | correction de bug |
| `test` | ajout ou correction de tests |
| `docs` | documentation, CHANGELOG |
| `refactor` | réécriture sans changement de comportement |
| `chore` | configuration, dépendances, CI |

Exemples : `feat: convertir les glycémies exprimées en g/L`, `test: couvrir la classe obésité sévère`.

## 3. Pull request et revue

1. `pytest` passe en local avant de pousser.
2. On pousse la branche (`git push -u origin <branche>`) et on ouvre une pull request vers `main`.
3. La description contient `Closes #<numéro>` : l'issue se fermera à la fusion.
4. **Une approbation** d'un autre membre est obligatoire. Le relecteur lit le diff, lance les tests
   si besoin, et commente précisément (ligne par ligne).
5. La CI (onglet *Actions*) doit être verte.
6. C'est l'**auteur** qui fusionne, une fois la PR approuvée, puis supprime la branche.

## 4. Conflits

Un conflit n'est pas une erreur : c'est Git qui demande une décision humaine.
Si votre PR affiche *This branch has conflicts* :

```bash
git switch <ma-branche>
git fetch origin
git merge origin/main          # Git signale les fichiers en conflit
# éditer les fichiers, garder la bonne version, supprimer les marqueurs <<<<<<< ======= >>>>>>>
pytest
git add <fichiers résolus>
git commit                     # message de merge proposé par Git
git push
```

Si le conflit touche le travail de quelqu'un d'autre : **on en parle avec lui avant de trancher**.

## 5. CHANGELOG

Chaque PR ajoute une ligne dans `CHANGELOG.md`, section `## [Non publié]`.

## 6. Données

- **Jamais de données réelles de patients** dans le dépôt, même privé : données de santé
  (RGPD, article 9), et l'historique Git conserve tout, même un fichier supprimé ensuite.
- Jamais de mot de passe, jeton ou clé d'API. Les fichiers locaux sensibles vont dans `data/prive/`
  ou `.env`, ignorés par `.gitignore`.

## 7. Règles propres à l'équipe

_À compléter par l'équipe en fin de TD (partie 3) : ce que vous avez décidé de garder, changer ou ajouter._

-
