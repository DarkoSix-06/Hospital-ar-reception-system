from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from db import insert_user, get_all_users
from utils import get_face_encoding, compare_face_to_database
from werkzeug.utils import secure_filename
from db import insert_user, get_all_users, find_user_by_name_or_id
from flask_cors import CORS, cross_origin
from datetime import datetime


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)



@app.route('/')
def home():
    return "✅ Hospital Face Recognition Server is running."

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.form
        image = request.files['image']
        name = data.get('name')
        patientID = data.get('patientID')
        illness = data.get('illness')
        reason = data.get('reason')

        if not all([name, patientID, illness, reason, image]):
            return jsonify({"error": "Missing form data"}), 400

        filename = secure_filename(f"{name}_{patientID}.jpg")
        save_path = os.path.join("faces", filename)
        image.save(save_path)

        face_encoding = get_face_encoding(save_path)
        if face_encoding is None:
            return jsonify({"error": "No face detected"}), 400

        user_data = {
            "name": name,
            "patientID": patientID,
            "illness": illness,
            "reason": reason,
            "face_encoding": face_encoding.tolist()
        }
        insert_user(user_data)
        return jsonify({"message": f"Registered {name} successfully!"})

    except Exception as e:
        print("❌ Register error:", str(e))
        return jsonify({"error": str(e)}), 500

    data = request.form
    image = request.files['image']
    name = data['name']
    patientID = data['patientID']
    illness = data['illness']
    reason = data['reason']

    filename = secure_filename(f"{name}_{patientID}.jpg")
    save_path = os.path.join("faces", filename)
    image.save(save_path)

    face_encoding = get_face_encoding(save_path)
    if face_encoding is None:
        return jsonify({"error": "No face detected"}), 400

    user_data = {
        "name": name,
        "patientID": patientID,
        "illness": illness,
        "reason": reason,
        "face_encoding": face_encoding.tolist()
    }
    insert_user(user_data)
    return jsonify({"message": f"Registered {name} successfully!"})

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        image = request.files['image']
        filename = "temp.jpg"
        image.save(filename)

        face_encoding = get_face_encoding(filename)
        if face_encoding is None:
            return jsonify({"status": "no_face"})

        known_users = get_all_users()
        match = compare_face_to_database(face_encoding, known_users)

        if match:
            last_seen = datetime.now().strftime("%Y-%m-%d %H:%M")
            return jsonify({
                "status": "recognized",
                "name": match["name"],
                "patientID": match["patientID"],
                "illness": match["illness"],
                "reason": match["reason"],
                "lastSeen": last_seen
            })
        else:
            return jsonify({"status": "new_user"})

    except Exception as e:
        print("❌ Server error:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/search')
def search():
    name = request.args.get("name")
    patientID = request.args.get("id")
    user = find_user_by_name_or_id(name, patientID)
    if user:
        return jsonify({
            "status": "found",
            "name": user["name"],
            "patientID": user["patientID"],
            "illness": user["illness"],
            "reason": user["reason"],
            "visits": user.get("visits", [])
        })
    else:
        return jsonify({"status": "not_found"})


@app.route('/all')
def get_all():
    users = get_all_users()
    for user in users:
        user.pop('face_encoding', None)
    return jsonify({"users": users})

@app.route('/update', methods=['POST', 'OPTIONS'])
@cross_origin()
def update_user():
    if request.method == 'OPTIONS':
        # Handle preflight request
        return jsonify({}), 200

    data = request.json
    name = data.get("name")
    patientID = data.get("patientID")

    user = find_user_by_name_or_id(name, patientID)
    if not user:
        return jsonify({"status": "not_found"})

    user.update({
        "illness": data.get("illness", user["illness"]),
        "reason": data.get("reason", user["reason"])
    })

    insert_user(user, update=True)
    return jsonify({"status": "updated", "user": user})


if __name__ == '__main__':
    os.makedirs('faces', exist_ok=True)
    print("🚀 Starting Hospital Face Recognition API server...")
    app.run(debug=True)
