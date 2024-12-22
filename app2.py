from flask import Flask, jsonify, request

app = Flask(__name__)


patients = {}

@app.route("/patients", methods=["POST"])
def create_patient():
    data = request.get_json()
    patient_id = len(patients) + 1
    patient = {
        "id": patient_id,
        "name": data["name"],
        "email": data["email"]
    }
    patients[patient_id] = patient
    return jsonify(patient), 201

@app.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = patients.get(patient_id)
    if patient:
        return jsonify(patient), 200
    else:
        return jsonify({"message": "Patient not found"}), 404

@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    if patient_id in patients:
        del patients[patient_id]
        return "", 204
    else:
        return jsonify({"message": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=54069)

