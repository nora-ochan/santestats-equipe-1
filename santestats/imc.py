"""Calcul et classification de l'indice de masse corporelle (IMC)."""


def calculer_imc(poids_kg: float, taille_cm: float) -> float:
    """Renvoie l'IMC en kg/m², arrondi à une décimale."""
    if poids_kg <= 0 or taille_cm <= 0:
        raise ValueError("Le poids et la taille doivent être positifs.")
    taille_m = taille_cm / 100
    return round(poids_kg / taille_m**2, 1)


def classer_imc(imc: float) -> str:
    """Classe un IMC d'adulte selon les seuils de l'OMS."""
    if imc < 18.5:
        return "Insuffisance pondérale"
    if imc < 25:
        return "Corpulence normale"
    if imc < 30:
        return "Surpoids"
    return "Obésité"
