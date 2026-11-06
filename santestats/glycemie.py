"""Harmonisation des glycémies vers une unité unique : le mg/dL."""

# Facteurs de conversion vers le mg/dL.
# 1 mmol/L de glucose = 18,016 mg/dL (masse molaire du glucose : 180,16 g/mol).
FACTEURS_VERS_MG_DL = {
    "mg/dL": 1.0,
    "mmol/L": 18.016,
    "g/L": 100.0,
}


def convertir_en_mg_dl(valeur: float, unite: str) -> float:
    """Convertit une glycémie en mg/dL, arrondie à une décimale.

    Lève ValueError si l'unité n'est pas prise en charge.
    """
    if unite not in FACTEURS_VERS_MG_DL:
        raise ValueError(f"Unité non prise en charge : {unite!r}")
    return round(valeur * FACTEURS_VERS_MG_DL[unite], 1)
