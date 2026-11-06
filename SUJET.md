# TD — Gestion collaborative avec Git et GitHub

## En 3 heures

Vous allez d'abord manipuler Git seul sur un projet Python existant, puis développer à quatre le même projet sur GitHub, avec issues, pull requests, revues et vrais conflits. En fin de séance, votre équipe publie une version 0.2.0 dont la qualité est contrôlée automatiquement.

**Le projet.** `santestats` analyse une cohorte de 40 patients synthétiques : IMC, glycémies harmonisées en mg/dL, rapport en ligne de commande. Le code tient en une centaine de lignes ; ce qui compte ici, c'est Git.

**À la fin du TD, vous savez :**

- enregistrer, consulter et annuler des modifications (commit, log, diff, restore, revert) ;
- travailler sur des branches et les fusionner, y compris quand Git signale un conflit ;
- collaborer sur GitHub : cloner, pousser, tirer, ouvrir et relire une pull request ;
- appliquer un workflow d'équipe : une issue, une branche, une PR, une revue, une CI verte.

| Partie | Durée | Mode | Ce que vous faites |
| --- | --- | --- | --- |
| 0. Mise en route | 15 min | seul | configurer Git et GitHub |
| 1. Git en local | 50 min | seul | cloner le dépôt de cours, branches, fusions, premier conflit |
| Pause | 10 min |  |  |
| 2. Collaborer sur GitHub | 65 min | équipe | dépôt d'équipe, 4 issues, 4 pull requests, 3 conflits |
| 3. Workflow d'équipe | 30 min | équipe | CI obligatoire, régression bloquée, version 0.2.0 |
| Bilan | 10 min | classe | ce qui a coincé, règles retenues |

**Prérequis.** Un compte GitHub (à créer en début de séance si besoin). Pour travailler sur votre machine : Git 2.40 ou plus récent, Python 3.10 ou plus récent, un éditeur (VS Code conseillé). Rien d'installé : GitHub Codespaces, dans le navigateur, suffit (partie 0).

**Équipes.** Quatre personnes, nommées A, B, C et D ; chaque lettre correspond à une issue. En trinôme, C prend aussi l'issue de D. A crée le dépôt de l'équipe.

**Évaluation.** Note individuelle sur 20, lue dans le dépôt de votre équipe après la séance. Ce que GitHub a enregistré à votre nom compte ; ce qui n'y apparaît pas ne compte pas. La partie 1 est un entraînement, non notée.

| Bloc | Points | Ce qui est regardé |
| --- | --- | --- |
| Votre pull request | 7 | branche `<numéro>-<description>`, commits `<type>: <description>`, `Closes #<n>`, code + test + CHANGELOG, fusion après approbation avec CI verte, par vous |
| Votre revue | 4 | au moins une revue *Approve* ou *Request changes*, un commentaire sur une ligne, des commentaires utiles (« ok » ne suffit pas) |
| Votre rôle | 6 | A : dépôt créé depuis le modèle, ruleset, CI obligatoire, étiquette `v0.2.0` et Release. B, C, D : conflit résolu par vous, sans marqueur oublié, tests verts, travail des autres conservé |
| Partie 3 | 2 | participation à la PR de l'issue 5 et à celle des règles d'équipe |
| Hygiène | 1 | commits rattachés à votre compte GitHub (même adresse e-mail), aucun fichier parasite (`.venv/`, `__pycache__/`, `.env`, `.DS_Store`…) |

Ne supprimez pas le dépôt de l'équipe et ne le passez pas en privé avant la publication des notes.

**Convention du sujet.** Les commandes sont à taper dans un terminal, à la racine du dépôt. Les lignes qui commencent par `#` sont des commentaires. Remplacez ce qui est entre chevrons, comme `<votre-identifiant>`.

**Dépôt de cours :** `https://github.com/Lille-Health-Data-Science/td-git-sante`

## Partie 0 — Mise en route (15 min)

Objectif : un Git qui sait qui vous êtes et un accès GitHub qui fonctionne.

**Pas encore de compte GitHub ?** Créez-le sur `https://github.com/signup` (5 minutes, adresse e-mail à valider). Notez votre identifiant : votre équipe en aura besoin.

Choisissez ensuite **une** des deux options. Sans Git ni Python déjà installés, prenez directement l'option 2.

### Option 1 : sur votre machine

1. Vérifiez les versions :

```bash
git --version        # 2.40 ou plus récent
python --version     # 3.10 ou plus récent (python3 sur macOS et Linux)
```

2. Dites à Git qui vous êtes (une seule fois par machine). Utilisez l'adresse e-mail de votre compte GitHub :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "vous@exemple.fr"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor "code --wait"   # si vous utilisez VS Code
git config --global --list                      # vérification
```

3. Connectez-vous à GitHub. Le plus simple est GitHub CLI (`gh`) :

```bash
gh auth login
# GitHub.com → HTTPS → Yes (authentifier Git) → Login with a web browser
gh auth status
```

Sans `gh` sous Windows, Git for Windows embarque Git Credential Manager : une fenêtre de connexion s'ouvrira au premier `git push`. GitHub n'accepte plus les mots de passe pour pousser en HTTPS.

### Option 2 : GitHub Codespaces (aucune installation)

1. Ouvrez le dépôt de cours dans le navigateur.
2. Bouton vert **Code** → onglet **Codespaces** → **Create codespace on main**.
3. Un VS Code s'ouvre dans le navigateur, avec Python, pytest, Git et `gh` déjà configurés à votre nom. Le terminal est en bas. Tapez-y une fois `git config --global pull.rebase false`.

Un compte gratuit inclut 120 heures de calcul Codespaces par mois, largement assez pour ce TD. Pensez à arrêter le codespace en fin de séance (menu Codespaces → Stop).

### Point de contrôle

- [ ] `git config user.name` affiche votre nom.
- [ ] `gh auth status` (ou Codespaces) indique que vous êtes connecté à github.com.

## Partie 1 — Git en local, seul (50 min)

Vous travaillez sur une copie du dépôt de cours. Vous n'avez pas le droit d'y pousser : tout se passe sur votre machine, vous ne pouvez rien casser chez les autres. Après chaque commande, lisez ce que Git répond : il dit presque toujours quoi faire ensuite.

### 1.1 Cloner et explorer (8 min)

```bash
git clone https://github.com/Lille-Health-Data-Science/td-git-sante.git
cd td-git-sante
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
pytest                             # 11 passed
python -m santestats               # le rapport de la cohorte
```

Dans Codespaces, le dépôt est déjà cloné et installé : passez directement aux commandes ci-dessous.

```bash
git log --oneline                  # l'historique de main
git log --oneline --graph --all    # toutes les branches
git log --oneline -- santestats/glycemie.py   # commits qui ont touché ce fichier
git show --stat HEAD               # le dernier commit et les fichiers modifiés
git branch                         # vos branches locales
git branch -a                      # + les branches du dépôt distant
```

Répondez :

- [ ] Quel commit a introduit la conversion des glycémies, et à quelle date ?
- [ ] Pourquoi `git branch` n'affiche que `main`, alors que `git branch -a` montre aussi trois branches `exercice/*` ?
- [ ] Le rapport affiche « Attention : 6 glycémie(s) dans une unité non prise en charge ». Quelle unité manque ? (Regardez `data/patients_synthetiques.csv`.)

### 1.2 Premier cycle : branche, commit, fusion (10 min)

Vous ajoutez l'âge moyen au rapport, sur une branche à vous.

```bash
git switch -c age-moyen            # crée la branche et s'y place
```

Dans `santestats/rapport.py`, juste **après** la ligne `lignes.append(f"IMC moyen : ...")`, ajoutez :

```python
    lignes.append(f"Âge moyen : {sum(p.age for p in patients) / len(patients):.1f} ans")
```

```bash
git status                         # fichier modifié, pas encore indexé
git diff                           # ce qui a changé, ligne par ligne
python -m santestats               # « Âge moyen : 56.4 ans »
git add santestats/rapport.py      # on prépare le commit (zone d'index)
git status                         # le fichier est indexé
git commit -m "feat: afficher l'âge moyen dans le rapport"
git log --oneline --graph --all
git switch main                    # l'âge moyen disparaît du fichier : normal
git merge age-moyen                # « Fast-forward »
```

- [ ] Pourquoi Git a-t-il pu faire un *fast-forward*, sans créer de commit de fusion ?

### 1.3 Fusionner une branche existante (7 min)

La branche `exercice/ajout-patients` ajoute cinq patients. Elle a été créée avant votre commit.

```bash
git switch exercice/ajout-patients # Git crée la branche locale à partir de celle du dépôt distant
git log --oneline -2
git switch main
git merge --no-edit exercice/ajout-patients
pytest                             # toujours 11 passed
python -m santestats               # Patients : 45
git log --oneline --graph -6
```

- [ ] Cette fois, Git a créé un commit de fusion. Pourquoi ? Dessinez le graphe sur papier.

### 1.4 Votre premier conflit (12 min)

Deux collègues ont modifié le titre du rapport, chacun sur sa branche, sans se concerter.

```bash
git diff main...origin/exercice/titre-fr   # trois points : ce que la branche a changé depuis qu'elle a quitté main
git diff main...origin/exercice/titre-en
git merge --no-edit origin/exercice/titre-fr     # passe sans difficulté
git merge --no-edit origin/exercice/titre-en     # CONFLICT (content)
git status                                       # « both modified: santestats/rapport.py »
```

Ouvrez `santestats/rapport.py`. Git a écrit les deux versions entre des marqueurs :

```text
<<<<<<< HEAD
TITRE = "Rapport de cohorte (santestats)"
=======
TITRE = "santestats cohort report"
>>>>>>> origin/exercice/titre-en
```

- Au-dessus de `=======` : votre version (`HEAD`, c'est-à-dire `main`).
- En dessous : la version qui arrive.

C'est à vous de décider. Gardez le titre français (ou écrivez-en un troisième), puis **supprimez les trois lignes de marqueurs**. VS Code propose aussi des boutons *Accept Current / Accept Incoming / Accept Both*.

```bash
pytest                             # on vérifie avant de valider
git add santestats/rapport.py      # « le conflit est résolu »
git commit --no-edit               # termine la fusion
git log --oneline --graph -10
```

En cas de panique : `git merge --abort` remet tout comme avant la fusion.

### 1.5 Ce qui ne doit jamais partir (5 min)

```bash
mkdir -p data/prive
echo "nir,nom,prenom" > data/prive/vrais_patients.csv
git status                         # rien : le fichier est ignoré
git check-ignore -v data/prive/vrais_patients.csv
```

- [ ] Ouvrez `.gitignore`. Quelle ligne protège ce fichier ? Citez deux autres choses qu'on ne versionne jamais.
- [ ] Pourquoi supprimer un fichier sensible dans un commit suivant ne suffit-il pas ?

### 1.6 Annuler (8 min)

**Une modification pas encore indexée :**

```bash
echo "brouillon" >> README.md
git restore README.md              # le fichier revient à son état du dernier commit
```

**Un message de commit raté** (sur un commit pas encore poussé) :

```bash
echo "Mes notes de TD" > notes.md
git add notes.md
git commit -m "ajou notes"
git commit --amend -m "docs: ajouter mes notes de TD"
```

**Un commit fautif déjà dans l'historique** :

```bash
# Dans santestats/glycemie.py, remplacez 18.016 par 18, puis :
git commit -am "fix: facteur mmol arrondi"
pytest                             # 1 failed : test_mmol_vers_mg_dl
git revert --no-edit HEAD          # un NOUVEAU commit qui annule le précédent
pytest                             # 11 passed
git log --oneline -3
```

- [ ] `git revert` ajoute un commit au lieu d'effacer le fautif. Pourquoi est-ce la bonne méthode sur une branche partagée ?

### 1.7 Et si on poussait ? (2 min)

```bash
git push
```

GitHub refuse (erreur 403 ou *Permission denied*) : vous pouvez lire ce dépôt, pas y écrire. Votre travail reste intact sur votre machine. Dans Codespaces, si GitHub propose de créer un *fork*, refusez. La partie 2 règle la question : chaque équipe aura son propre dépôt.

## Partie 2 — Collaborer sur GitHub (65 min)

L'équipe crée son propre dépôt, se répartit quatre issues, et chaque modification entre dans `main` par une pull request relue par un autre membre. Les règles du jeu sont dans `CONTRIBUTING.md` : lisez-le pendant que A prépare le dépôt.

### 2.1 Créer le dépôt de l'équipe (10 min)

**A, sur github.com :**

1. Sur la page du dépôt de cours : **Use this template** → **Create a new repository**.
2. Nom : `santestats-equipe-<numéro>`. Visibilité : **Public** (données synthétiques ; la protection de branche est gratuite sur les dépôts publics). Si l'option **Include all branches** apparaît, laissez-la décochée.
3. **Settings** → **Collaborators** → **Add people** : ajoutez B, C et D, ainsi que l'intervenant, `antoine-teston`.
4. **Settings** → **Rules** → **Rulesets** → **New ruleset** → **New branch ruleset** :
    - nom : `protéger main`, *Enforcement status* : **Active** ;
    - *Target branches* → **Add target** → **Include default branch** ;
    - cochez **Require a pull request before merging**, *Required approvals* : **1** ;
    - laissez cochés *Restrict deletions* et *Block force pushes* → **Create**.

5. Vérifiez que `antoine-teston` apparaît dans **Collaborators** (invitation en attente) : c'est par cette invitation que l'intervenant reçoit l'adresse de votre dépôt pour la notation. Sans elle, le dépôt ne peut pas être noté.

**B, C et D :** acceptez l'invitation (e-mail, ou `https://github.com/<A>/<dépôt>/invitations`).

**Tout le monde**, dans un dossier **différent** du dépôt de cours (ou dans un nouveau codespace ouvert sur le dépôt de l'équipe) :

```bash
cd ..
git clone https://github.com/<A>/santestats-equipe-<numéro>.git
cd santestats-equipe-<numéro>
pip install -r requirements.txt    # dans un environnement virtuel, comme en 1.1
pytest                             # 11 passed
```

**A seulement**, une fois : créez les issues de l'équipe.

```bash
python scripts/creer_issues.py     # crée les issues 1 à 7 à partir de docs/issues/
```

Sur GitHub, onglet **Issues** : chacun ouvre son issue (A → 1, B → 2, C → 3, D → 4) et se l'assigne (*Assignees* → *assign yourself*).

### 2.2 Chacun son issue (20 min)

Tout le monde en parallèle. Exemple pour C :

```bash
git switch main
git pull                                   # partir d'un main à jour
git switch -c 3-obesite-morbide
# ... modifier le code comme l'indique l'issue, CHANGELOG compris ...
pytest
git add santestats/imc.py tests/test_imc.py CHANGELOG.md
git commit -m "feat: distinguer l'obésité morbide"
git push -u origin 3-obesite-morbide
```

| Membre | Issue | Branche | Fichiers touchés |
| --- | --- | --- | --- |
| A | 1 | `1-conversion-g-l` | `glycemie.py`, `test_glycemie.py`, `CHANGELOG.md` |
| B | 2 | `2-seuil-hyperglycemie` | `glycemie.py`, `rapport.py`, `test_glycemie.py`, `CHANGELOG.md` |
| C | 3 | `3-obesite-morbide` | `imc.py`, `test_imc.py`, `CHANGELOG.md` |
| D | 4 | `4-classes-obesite-oms` | `imc.py`, `test_imc.py`, `CHANGELOG.md` |

Sur GitHub, cliquez sur **Compare & pull request**. Vérifiez la base (`main`), complétez la description (le modèle s'affiche, gardez `Closes #<numéro de l'issue>`), choisissez un relecteur dans **Reviewers**, puis **Create pull request**. Onglet **Checks** : la CI lance les tests.

Ne fusionnez rien pour l'instant.

### 2.3 Revue croisée (10 min)

A relit la PR de B, B celle de C, C celle de D, D celle de A.

1. Onglet **Files changed** : lisez le diff. Survolez une ligne et cliquez sur **+** pour commenter.
2. Au moins un commentaire utile par revue : une question, une suggestion, un oubli (test, CHANGELOG).
3. Pour tester la PR chez vous : `gh pr checkout <numéro de la PR>`, puis `pytest`, puis `git switch main`.
4. **Review changes** → **Approve**, ou **Request changes** si quelque chose doit être corrigé. L'auteur corrige par un nouveau commit sur sa branche, puis `git push`.

### 2.4 Fusionner, dans l'ordre 1, 2, 3, 4 (25 min)

Une PR à la fois, toute l'équipe regarde le même écran. Après **chaque** fusion, tout le monde met son `main` à jour :

```bash
git switch main
git pull
```

**PR de l'issue 1 (A).** Approuvée → **Merge pull request** → **Confirm merge** → **Delete branch**. L'issue 1 se ferme toute seule.

**PR de l'issue 2 (B).** GitHub annonce *This branch has conflicts that must be resolved*. Résolvez-le en local plutôt qu'avec le bouton web, pour voir ce qui se passe :

```bash
git switch 2-seuil-hyperglycemie
git fetch origin
git merge origin/main              # lisez la sortie : quels fichiers sont fusionnés automatiquement ?
git status
# CHANGELOG.md : gardez les deux lignes, supprimez les marqueurs
pytest
git add CHANGELOG.md
git commit --no-edit
git push
```

- [ ] A et B ont tous les deux modifié `glycemie.py` et `test_glycemie.py`. Pourquoi Git n'y a-t-il vu aucun conflit, alors qu'il en voit un dans `CHANGELOG.md` ?

Fusionnez la PR 2.

**PR de l'issue 3 (C).** Même chose : conflit sur `CHANGELOG.md` uniquement. C le résout, pousse, fusionne.

**PR de l'issue 4 (D).** Trois fichiers en conflit : `CHANGELOG.md`, `santestats/imc.py`, `tests/test_imc.py`. C et D ont traité différemment les IMC de 40 et plus.

Ici, aucune des deux versions n'est « la bonne » par défaut. **C et D se mettent ensemble** et décident, puis D résout :

- `classer_imc` doit rester cohérente : chaque IMC dans une seule classe, aucun trou ;
- on ne jette pas le travail de l'autre : le test écrit par C est conservé, adapté si le libellé change ;
- si le libellé retenu pour 40 et plus change, la ligne de l'issue 3 dans le CHANGELOG doit le dire.

D explique la décision dans un commentaire de la PR, pousse, l'équipe relit, D fusionne.

### Point de contrôle

- [ ] Les issues 1 à 4 sont fermées.
- [ ] Sur `main` à jour, `pytest` passe (17 tests si le test de C a été conservé).
- [ ] `python -m santestats` affiche `Glycémies converties en mg/dL : 40 / 40` et trois classes d'obésité.
- [ ] `git log --oneline --graph` montre une fusion par PR (ou onglet **Insights** → **Network** sur GitHub).

## Partie 3 — Un workflow d'équipe qui tient (30 min)

Une relecture humaine ne suffit pas : l'équipe rend les tests obligatoires, voit la CI bloquer une régression, puis publie une version étiquetée.

### 3.1 Rendre la CI obligatoire (3 min)

**A :** **Settings** → **Rules** → **Rulesets** → `protéger main` :

- cochez **Require status checks to pass** → **Add checks** → choisissez `tests` (le job GitHub Actions qui a tourné sur vos PR) ;
- cochez aussi **Require conversation resolution before merging** → **Save changes**.

### 3.2 La CI attrape une régression (12 min)

Un volontaire traite l'**issue 5** exactement comme elle est écrite, y compris « sans lancer les tests en local » :

```bash
git switch main && git pull
git switch -c 5-facteur-mmol-arrondi
# dans santestats/glycemie.py : 18.016 → 18
git commit -am "refactor: arrondir le facteur mmol/L à 18"
git push -u origin 5-facteur-mmol-arrondi
```

Ouvrez la PR. Après une minute, l'onglet **Checks** est rouge : `test_mmol_vers_mg_dl` échoue (7 mmol/L donnent 126,0 au lieu de 126,1). Le bouton de fusion est bloqué.

En équipe, répondez en commentaire de la PR :

- [ ] 7,0 mmol/L × 18 = 126,0 mg/dL, contre 126,1 avec 18,016. L'écart (0,09 %) change-t-il le classement d'un patient dans le rapport ? Si ce n'est pas le cas, qu'est-ce qui pose quand même problème dans cette PR ?
- [ ] « Il suffit de corriger le test pour qu'il passe » : pourquoi est-ce une mauvaise réponse ici ?
- [ ] Décision : fermez la PR (**Close pull request**) avec un commentaire qui la justifie, puis fermez l'issue 5 en *Close as not planned*.

### 3.3 Publier la version 0.2.0 (10 min)

**A** traite l'**issue 6** :

```bash
git switch main && git pull
git switch -c 6-version-0-2-0
# CHANGELOG.md : « ## [Non publié] » devient « ## [0.2.0] - <date du jour> »,
#                avec au-dessus une nouvelle section « Non publié » vide
# santestats/__init__.py : __version__ = "0.2.0"
git commit -am "docs: publier la version 0.2.0"
git push -u origin 6-version-0-2-0
```

PR, revue, fusion. Puis, sur `main` à jour :

```bash
git switch main && git pull
git tag -a v0.2.0 -m "Version 0.2.0"
git push origin v0.2.0
```

Sur GitHub : **Releases** → **Draft a new release** → étiquette `v0.2.0` → collez les lignes du CHANGELOG → **Publish release**.

Les autres membres récupèrent l'étiquette :

```bash
git pull --tags
git log --oneline --decorate -3     # tag: v0.2.0
```

- [ ] Pourquoi passer de 0.1.0 à 0.2.0, et pas à 0.1.1 ni à 1.0.0 ?

### 3.4 Vos règles (5 min)

Ensemble, complétez la section 7 de `CONTRIBUTING.md` avec **trois règles** que l'équipe garderait sur un vrai projet (qui fusionne, combien de relecteurs, quand découper une PR, comment nommer les branches…). Cette modification passe, elle aussi, par une branche et une PR.

## Bonus, pour qui a terminé

- **Issue 7, en rebase.** Traitez l'issue 7, puis mettez votre branche à jour avec `git fetch origin` et `git rebase origin/main` au lieu d'un merge. Comparez le graphe obtenu avec ceux de la partie 2. Poussez avec `git push --force-with-lease` : jamais de force sur une branche que quelqu'un d'autre utilise.
- **Ranger ses commits avant la PR.** Sur une branche à vous, faites trois petits commits, puis `git rebase -i HEAD~3` et regroupez-les (`squash`).
- **Annuler une PR déjà fusionnée.** Sur une PR fermée, bouton **Revert** : GitHub prépare une PR qui annule la première. Retrouvez la commande équivalente.
- **Mettre de côté un travail en cours.** Modifiez un fichier, puis `git stash`, changez de branche, revenez, `git stash pop`.
- **Qui a écrit cette ligne ?** `git blame santestats/imc.py`, puis le même fichier dans l'onglet **Blame** de GitHub.

## Mémo des commandes

| Je veux… | Commande |
| --- | --- |
| récupérer un dépôt | `git clone <url>` |
| voir où j'en suis | `git status` |
| voir ce que j'ai modifié | `git diff` (indexé : `git diff --staged`) |
| préparer puis enregistrer | `git add <fichier>` puis `git commit -m "type: message"` |
| voir l'historique | `git log --oneline --graph --all` |
| créer une branche et y aller | `git switch -c <branche>` |
| changer de branche | `git switch <branche>` |
| fusionner une branche dans la branche courante | `git merge <branche>` |
| abandonner une fusion en conflit | `git merge --abort` |
| marquer un conflit comme résolu | `git add <fichier>` puis `git commit` |
| envoyer ma branche la première fois | `git push -u origin <branche>` |
| récupérer le travail des autres | `git pull` (ou `git fetch` puis `git merge origin/main`) |
| jeter une modification non indexée | `git restore <fichier>` |
| retirer un fichier de l'index | `git restore --staged <fichier>` |
| corriger le dernier commit non poussé | `git commit --amend` |
| annuler un commit déjà partagé | `git revert <commit>` |
| retrouver un commit « perdu » | `git reflog` |
| étiqueter une version | `git tag -a v0.2.0 -m "…"` puis `git push origin v0.2.0` |
| tester la PR d'un collègue | `gh pr checkout <numéro>` |

Pour aller plus loin : le livre *Pro Git*, gratuit en français sur [git-scm.com/book/fr](https://git-scm.com/book/fr/v2), et l'entraînement visuel aux branches sur [learngitbranching.js.org](https://learngitbranching.js.org/?locale=fr_FR).
