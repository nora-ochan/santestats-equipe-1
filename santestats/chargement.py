"""Lecture du fichier CSV de la cohorte."""

import csv
from dataclasses import dataclass


@dataclass
class Patient:
    id_patient: str
    sexe: str
    age: int
    poids_kg: float
    taille_cm: float
    glycemie: float
    unite_glycemie: str
    service: str


def charger_patients(chemin: str) -> list[Patient]:
    """Lit le CSV de la cohorte et renvoie une liste de patients."""
    with open(chemin, newline="", encoding="utf-8") as fichier:
        return [
            Patient(
                id_patient=ligne["id_patient"],
                sexe=ligne["sexe"],
                age=int(ligne["age"]),
                poids_kg=float(ligne["poids_kg"]),
                taille_cm=float(ligne["taille_cm"]),
                glycemie=float(ligne["glycemie"]),
                unite_glycemie=ligne["unite_glycemie"],
                service=ligne["service"],
            )
            for ligne in csv.DictReader(fichier)
        ]
