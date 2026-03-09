import os
from flask import Flask, jsonify

app = Flask(__name__)

# Lineage Metadata
LINEAGE_DATA = {
    "gotra": "Haritha",
    "lineage": "Rigveda",
    "sutra": "Ashvalayana",
    "pravara": ["Angiras", "Ambarisha", "Yuvanasva"],
    "description": "Digital preservation of Ashvalayana Shrauta/Grihya Sutras."
}

@app.route('/')
def home():
    return jsonify({
        "status": "Online",
        "service": "Anamika Core",
        "message": "Welcome to the ETERNAL Project"
    })

@app.route('/lineage')
def get_lineage():
    return jsonify(LINEAGE_DATA)

@app.route('/rituals')
def get_rituals():
    # Simplified structure of Ashvalayana rituals
    rituals = [
        {"id": 1, "name": "Upanayana", "type": "Samskara"},
        {"id": 2, "name": "Vivaha", "type": "Samskara"},
        {"id": 3, "name": "Sayam-Pratar Homa", "type": "Nitya Karma"}
    ]
    return jsonify(rituals)

if __name__ == '__main__':
    # Listen on all interfaces for Docker
    app.run(host='0.0.0.0', port=8000)

@app.route('/veda/mandala1')
def get_mandala1():
    import json
    import os
    file_path = os.path.join(os.path.dirname(__file__), 'Mandala_1.json')
    try:
        with open(file_path, 'r') as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify({"error": "Mandala_1.json not found in app folder"}), 404
