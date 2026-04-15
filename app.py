from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

API_KEY = "24bbcd2ccf13fbc05886c2a7cdad7f72"

@app.route("/")
def home():
    return send_from_directory("", "index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return jsonify({"error": "City not found"})

    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "icon": data["weather"][0]["icon"]
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)