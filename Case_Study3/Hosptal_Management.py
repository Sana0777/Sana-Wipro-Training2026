from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

patients = []


def get_patient_by_id(pid):
    for patient in patients:
        if patient["id"] == pid:
            return patient
    return None


def add_patient(data):
    data["id"] = len(patients) + 1
    patients.append(data)
    return data


@app.route("/")
def home():
    return redirect(url_for("register_patients"))


@app.route("/register", methods=["GET", "POST"])
def register_patients():

    if request.method == "GET":
        return render_template("register.html")

    data = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "contact": request.form["contact"],
        "disease": request.form["disease"],
        "doctor": request.form["doctor"]
    }

    add_patient(data)

    return redirect(url_for("patient_list"))


@app.route("/patients")
def patient_list():
    return render_template("patients.html", patients=patients)


@app.route("/api/patients", methods=["GET", "POST"])
def manage_patients_api():

    if request.method == "GET":
        return jsonify(patients), 200

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if not data:
        return jsonify({"error": "Invalid"}), 400

    added_patient = add_patient(data)

    return jsonify(added_patient), 201


@app.route("/api/patients/<int:pid>", methods=["GET", "PUT"])
def manage_patient_by_id(pid):

    patient = get_patient_by_id(pid)

    if not patient:
        return jsonify({"error": "Not Found"}), 404

    if request.method == "GET":
        return jsonify(patient), 200

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid data"}), 400

    data.pop("id", None)

    patient.update(data)

    return jsonify(patient), 200


@app.route("/api/patients/<int:pid>", methods=["DELETE"])
def delete_patient_by_id(pid):

    patient = get_patient_by_id(pid)

    if not patient:
        return jsonify({"error": "Not Found"}), 404

    patients.remove(patient)

    return jsonify({"message": "Patient deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
