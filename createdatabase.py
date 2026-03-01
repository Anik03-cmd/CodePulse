import pandas as pd

# Complete Medicine Database
data = {
    "Drug": [
        "Metformin","Glipizide","Insulin",
        "Atorvastatin","Simvastatin","Rosuvastatin",
        "Amoxicillin","Ampicillin","Azithromycin","Clarithromycin",
        "Lisinopril","Enalapril","Losartan","Valsartan",
        "Ibuprofen","Naproxen","Warfarin","Aspirin",
        "Omeprazole","Pantoprazole",
        "Sertraline","Fluoxetine",
        "Atenolol","Metoprolol","Amlodipine"
    ],

    "MaxDose": [
        "2000mg","40mg","Variable",
        "80mg","40mg","40mg",
        "3000mg","12000mg","500mg","1000mg",
        "80mg","40mg","100mg","320mg",
        "3200mg","1500mg","10mg","4000mg",
        "40mg","80mg",
        "200mg","80mg",
        "100mg","400mg","10mg"
    ],

    "InteractsWith": [
        "Alcohol,Iodine contrast",
        "Alcohol,Fluconazole",
        "Alcohol,Beta-blockers",
        "Macrolides,Azole Antifungals",
        "Macrolides,Azole Antifungals,Amiodarone",
        "Macrolides,Warfarin",
        "Warfarin,Methotrexate",
        "Warfarin,Oral Contraceptives",
        "Warfarin,Statins,QT-prolonging drugs",
        "Statins,Warfarin,Colchicine",
        "NSAIDs,Potassium supplements,ARBs",
        "NSAIDs,Potassium supplements",
        "ACE Inhibitors,NSAIDs,Potassium",
        "ACE Inhibitors,NSAIDs",
        "Warfarin,ACE inhibitors,ARBs,Aspirin",
        "Warfarin,ACE inhibitors,Lithium",
        "NSAIDs,Aspirin,Macrolides,Statins,Penicillins",
        "Warfarin,NSAIDs,Methotrexate",
        "Clopidogrel,Methotrexate",
        "Methotrexate,Atazanavir",
        "MAOIs,Tramadol,Triptans",
        "MAOIs,Tramadol,Lithium",
        "Verapamil,Diltiazem,Insulin",
        "Verapamil,Clonidine,Insulin",
        "Simvastatin,Cyclosporine"
    ],

    "FamilyOfMed": [
        "Biguanides","Sulfonylureas","Insulins",
        "Statins","Statins","Statins",
        "Penicillins","Penicillins","Macrolides","Macrolides",
        "ACE inhibitors","ACE inhibitors","ARBs","ARBs",
        "NSAIDs","NSAIDs","Anticoagulants","Salicylates",
        "Proton Pump Inhibitors","Proton Pump Inhibitors",
        "SSRIs","SSRIs",
        "Beta-blockers","Beta-blockers",
        "Calcium Channel Blockers"
    ],

    "TreatsDisease": [
        "Diabetes Type 2",
        "Diabetes Type 2",
        "Diabetes Type 1,Diabetes Type 2",
        "Hyperlipidemia,Cardiovascular Disease",
        "Hyperlipidemia",
        "Hyperlipidemia,Cardiovascular Disease",
        "Bacterial Infection,Pneumonia",
        "Bacterial Infection,Meningitis",
        "Bacterial Infection,Pneumonia",
        "Bacterial Infection,H. Pylori",
        "Hypertension,Heart Failure",
        "Hypertension,Heart Failure",
        "Hypertension,Diabetic Nephropathy",
        "Hypertension,Heart Failure",
        "Pain,Inflammation,Fever",
        "Pain,Inflammation,Arthritis",
        "Atrial Fibrillation,DVT,Pulmonary Embolism",
        "Pain,Cardiovascular Disease,Fever",
        "GERD,Peptic Ulcer",
        "GERD,Erosive Esophagitis",
        "Depression,Anxiety,OCD",
        "Depression,Anxiety,Bulimia",
        "Hypertension,Angina,Arrhythmia",
        "Hypertension,Heart Failure,Arrhythmia",
        "Hypertension,Angina"
    ]
}

df = pd.DataFrame(data)

# Save Excel
df.to_excel("medical_database.xlsx", index=False)

print("✅ Complete Medical Database Created!")