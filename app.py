from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DB_FILE = "database.json"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        db = json.load(f)
else:
    db = {}

@app.route("/")
def home():
    return "TinyWebDB personalizado com armazenamento permanente."

@app.route("/getvalue", methods=["POST"])
def get_value():
    tag = request.form.get("tag")
    value = db.get(tag, "")
    return jsonify(["VALUE", tag, value])

@app.route("/storeavalue", methods=["POST"])
def store_value():
    tag = request.form.get("tag")
    value = request.form.get("value")
    db[tag] = value
    with open(DB_FILE, "w") as f:
        json.dump(db, f)
    return jsonify(["STORED", tag, value])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
