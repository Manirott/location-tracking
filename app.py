from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)

# File to store locations (safe for Render)
LOCATION_FILE = "locations.txt"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/location', methods=['POST', 'GET'])
def location():
    if request.method == 'POST':
        data = request.get_json()
        lat = data.get("latitude")
        lon = data.get("longitude")
        timestamp = data.get("timestamp")

        if lat is None or lon is None:
            return jsonify({"error": "Missing latitude or longitude"}), 400

        location_info = f"{timestamp} - Latitude: {lat}, Longitude: {lon}\n"

        # Save to file (append mode)
        with open(LOCATION_FILE, "a") as file:
            file.write(location_info)

        return jsonify({"message": "Location saved successfully!"}), 200

    elif request.method == 'GET':
        if os.path.exists(LOCATION_FILE):
            with open(LOCATION_FILE, "r") as file:
                content = file.read()
            return f"<pre>{content}</pre>"
        else:
            return "No location data found."

