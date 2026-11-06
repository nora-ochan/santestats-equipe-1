from santestats.chargement import charger_patients

FICHIER = "data/patients_synthetiques.csv"


def test_nombre_de_patients():
    assert len(charger_patients(FICHIER)) == 40


def test_premier_patient():
    patient = charger_patients(FICHIER)[0]
    assert patient.id_patient == "P001"
    assert patient.unite_glycemie == "mmol/L"
