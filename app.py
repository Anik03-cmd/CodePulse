from flask import Flask, request
from loaddatabase import *
from ocr_reader import extract_prescription

app = Flask(__name__)

stored_detected = []


@app.route("/", methods=["GET", "POST"])
def home():

    global stored_detected

    result = ""
    edit_section = ""

    medicines = get_all_medicines()

    # ================= OCR STEP =================

    if request.method == "POST" and "scan" in request.form:

        disease = request.form["disease"]

        image = request.files["image"]

        path = "uploaded.png"
        image.save(path)

        detected = extract_prescription(
            path,
            medicines
        )

        stored_detected = detected

        if detected:

            edit_section = """
            <h3>Detected Medicines (Edit if needed)</h3>
            <form method="POST">
            """

            edit_section += f"""
            <input type="hidden"
            name="disease"
            value="{disease}">
            """

            for med in detected:

                edit_section += f"""
                {med}
                Dose:
                <input name="dose_{med}"
                value="100"><br><br>
                """

            edit_section += """
            <button name="analyze">
            Run Safety Analysis
            </button>
            </form>
            """

        else:
            edit_section = "<h3>No medicines detected</h3>"

    # ================= ANALYSIS =================

    if request.method == "POST" and "analyze" in request.form:

        disease = request.form["disease"]

        prescription = {}

        for med in stored_detected:

            dose = int(
                request.form.get(
                    f"dose_{med}", 100
                )
            )

            prescription[med] = dose

        level, score, reasons, adv = analyze_prescription(
            prescription,
            disease
        )

        reasons_html = "<ul>" + "".join(
            f"<li>{r}</li>" for r in reasons
        ) + "</ul>"

        adv_html = "<ul>" + "".join(
            f"<li>{a}</li>" for a in adv
        ) + "</ul>"

        result = f"""
        <div style="border:3px solid red;
        padding:20px;margin-top:20px">

        <h2>Safety Score : {score}/100</h2>

        <h2>{level}</h2>

        <h3>Reasons</h3>
        {reasons_html}

        <h3>Recommendations</h3>
        {adv_html}

        </div>
        """

    return f"""
<h1>Prescription OCR Analyzer</h1>

<form method="POST"
enctype="multipart/form-data">

Disease:<br>
<input name="disease" required><br><br>

Upload Prescription:<br>
<input type="file" name="image"><br><br>

<button name="scan">
Scan Prescription
</button>

</form>

{edit_section}

{result}
"""


app.run(host="0.0.0.0", port=5000)