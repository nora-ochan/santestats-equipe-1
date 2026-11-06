# santestats — dépôt du TD « Gestion collaborative avec Git et GitHub »

Petit projet Python qui analyse une cohorte de **40 patients entièrement synthétiques** :
calcul et classification de l'IMC, harmonisation des glycémies en mg/dL, rapport en ligne de commande.
Le code est volontairement court : l'objet du TD n'est pas Python, c'est **Git et le travail en équipe**.

> **Consignes du TD : [`SUJET.md`](SUJET.md).** Commencez par la partie 0.
> Support du cours magistral : [`cours/CM-Git-GitHub.pdf`](cours/CM-Git-GitHub.pdf).

> Aucune donnée de ce dépôt ne concerne une personne réelle. Ne déposez jamais de données réelles
> de patients dans un dépôt Git, même privé (voir `CONTRIBUTING.md`).

## Deux façons d'utiliser ce dépôt

| Moment du TD | Ce que vous faites | Droits nécessaires |
|---|---|---|
| Partie 1, en solo | `git clone` de ce dépôt, exercices en local sur les branches `exercice/*` | aucun : vous ne poussez rien ici |
| Parties 2 et 3, en équipe | un membre crée le dépôt de l'équipe avec **Use this template**, invite les autres ; tout le monde clone ce nouveau dépôt et pousse dessus | collaborateur du dépôt d'équipe |

## Installation

Il faut Git (2.40 ou plus récent) et Python 3.10 ou plus récent.

```bash
git clone https://github.com/Lille-Health-Data-Science/td-git-sante.git
cd td-git-sante
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

Sans installation possible sur votre machine : ouvrez le dépôt dans **GitHub Codespaces**
(bouton vert *Code* → onglet *Codespaces*). L'environnement est déjà configuré (`.devcontainer/`).

## Lancer le projet

```bash
pytest                    # lance les tests
python -m santestats      # affiche le rapport de la cohorte
```

## Organisation du code

```
santestats/
  imc.py          calcul et classification de l'IMC
  glycemie.py     conversion des glycémies vers le mg/dL
  chargement.py   lecture du CSV
  rapport.py      rapport texte (python -m santestats)
tests/            tests pytest, lancés aussi par la CI GitHub Actions
data/             cohorte synthétique
docs/issues/      tâches de l'équipe (créées comme issues GitHub au début de la partie 2)
scripts/          script de création des issues
```

## Contribuer

Les règles d'équipe (branches, messages de commit, pull requests, revue) sont dans
[`CONTRIBUTING.md`](CONTRIBUTING.md).
