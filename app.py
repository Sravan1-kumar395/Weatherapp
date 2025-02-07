from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "292882322a86680f04b3d94c7f8d3e6d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "Unknown error")}), response.status_code

    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(debug=True)
