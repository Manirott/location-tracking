from flask import Flask, request, jsonify, render_template  # 👈 this is the fix
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')  # ✅ This line serves index.html
@app.route('/location', methods=['POST'])
def receive_location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")

    if lat is None or lon is None:
        return jsonify({"error": "Invalid location data"}), 400

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    location_info = f"[{timestamp}] Latitude: {lat}, Longitude: {lon}\n"

    # Save to file
    with open("location.txt", "a") as file:
        file.write(location_info)

    print("✅ Location saved to location.txt")
    return jsonify({"status": "Location saved successfully."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
