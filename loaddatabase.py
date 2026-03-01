import pandas as pd
import itertools
import re

data = pd.read_excel("medical_database.xlsx")

medicine_db = {}

for _, row in data.iterrows():

    dose = re.findall(r"\d+", str(row["MaxDose"]))
    max_dose = int(dose[0]) if dose else 0

    medicine_db[row["Drug"].lower()] = {
        "MaxDose": max_dose,
        "InteractsWith": str(row["InteractsWith"]).lower(),
        "Family": str(row["FamilyOfMed"]).lower(),
        "Treats": str(row["TreatsDisease"]).lower(),
    }


def explain_interaction(m1, m2):

    f1 = medicine_db[m1]["Family"]
    f2 = medicine_db[m2]["Family"]

    if f1 == f2:
        return f"Both belong to {f1} family."

    if "nsaid" in f1 or "nsaid" in f2:
        return "NSAIDs increase bleeding risk."

    return "Possible drug interaction."


def analyze_prescription(prescription, disease):

    disease = disease.lower()

    risk = 0
    reasons = []
    advice = []

    for med, dose in prescription.items():

        if med not in medicine_db:
            continue

        # softer disease rule
        if disease and disease not in medicine_db[med]["Treats"]:
            risk += 0.5
            reasons.append(
                f"{med} may not directly treat {disease}"
            )

        max_dose = medicine_db[med]["MaxDose"]

        if max_dose and dose > max_dose:

            risk += 3

            reasons.append(
                f"{med} exceeds safe dose ({max_dose} mg)"
            )

            advice.append(
                f"Reduce dosage of {med}"
            )

    meds = list(prescription.keys())

    for m1, m2 in itertools.combinations(meds, 2):

        if (
            m2 in medicine_db[m1]["InteractsWith"]
            or medicine_db[m1]["Family"]
            == medicine_db[m2]["Family"]
        ):

            risk += 2

            reasons.append(
                f"{m1} + {m2}: {explain_interaction(m1,m2)}"
            )

            advice.append(
                "Consult physician."
            )

    score = max(0, 100 - int(risk * 15))

    if score >= 80:
        level = "SAFE ✅"
    elif score >= 50:
        level = "MODERATE RISK ⚠"
    else:
        level = "HIGH RISK 🚨"

    return level, score, reasons, list(set(advice))


def suggest_medicines(disease):

    disease = disease.lower()

    result = []

    for med, info in medicine_db.items():

        if disease in info["Treats"]:
            result.append(
                (med.title(), info["Family"])
            )

    return result[:6]


def get_all_medicines():
    return list(medicine_db.keys())