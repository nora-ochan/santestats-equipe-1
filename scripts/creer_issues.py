"""Crée les issues du TD dans le dépôt de l'équipe, à partir de docs/issues/*.md.

À lancer UNE SEULE FOIS, par une seule personne, depuis la racine du dépôt de l'équipe :

    python scripts/creer_issues.py

Prérequis : GitHub CLI installé et connecté (`gh auth login`), déjà présent dans Codespaces.
"""

import shutil
import subprocess
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent.parent / "docs" / "issues"


def main() -> None:
    if shutil.which("gh") is None:
        sys.exit("GitHub CLI (gh) introuvable : installez-le ou créez les issues à la main.")
    for fichier in sorted(DOSSIER.glob("*.md")):
        lignes = fichier.read_text(encoding="utf-8").splitlines()
        titre = lignes[0].removeprefix("# ").strip()
        corps = "\n".join(lignes[1:]).strip()
        subprocess.run(
            ["gh", "issue", "create", "--title", titre, "--body", corps],
            check=True,
        )
        print(f"Créée : {titre}")


if __name__ == "__main__":
    main()
