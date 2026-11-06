"""Rapport texte sur la cohorte, en ligne de commande."""

import argparse
from collections import Counter

from .chargement import Patient, charger_patients
from .glycemie import convertir_en_mg_dl
from .imc import calculer_imc, classer_imc

TITRE = "Rapport santestats"


def construire_rapport(patients: list[Patient]) -> str:
    """Construit le rapport de la cohorte sous forme de texte."""
    lignes = [TITRE, "=" * len(TITRE), f"Patients : {len(patients)}", ""]

    imcs = [calculer_imc(p.poids_kg, p.taille_cm) for p in patients]
    lignes.append(f"IMC moyen : {sum(imcs) / len(imcs):.1f}")
    lignes.append("Répartition par classe d'IMC :")
    categories = Counter(classer_imc(imc) for imc in imcs)
    for categorie, effectif in sorted(categories.items(), key=lambda c: (-c[1], c[0])):
        lignes.append(f"  - {categorie} : {effectif}")
    lignes.append("")

    glycemies = []
    non_converties = 0
    for patient in patients:
        try:
            glycemies.append(convertir_en_mg_dl(patient.glycemie, patient.unite_glycemie))
        except ValueError:
            non_converties += 1
    lignes.append(f"Glycémies converties en mg/dL : {len(glycemies)} / {len(patients)}")
    if non_converties:
        lignes.append(f"  Attention : {non_converties} glycémie(s) dans une unité non prise en charge")
    n_elevees = sum(1 for g in glycemies if g >= 126)
    lignes.append(f"Glycémies >= 126 mg/dL : {n_elevees}")
    return "\n".join(lignes)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Rapport sur une cohorte synthétique.")
    parser.add_argument(
        "fichier",
        nargs="?",
        default="data/patients_synthetiques.csv",
        help="chemin du CSV (par défaut : data/patients_synthetiques.csv)",
    )
    args = parser.parse_args(argv)
    print(construire_rapport(charger_patients(args.fichier)))
