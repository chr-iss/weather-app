from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key (get free from https://openweathermap.org/api)
API_KEY = "24bbcd2ccf13fbc05886c2a7cdad7f72"  # Demo key - replace with yours!

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    
    if not city:
        return jsonify({'error': 'City required'}), 400
    
    # Call OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            return jsonify({'error': data.get('message', 'City not found')}), 404
        
        # Send only needed data to frontend
        return jsonify({
            'city': data['name'],
            'country': data['sys']['country'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)