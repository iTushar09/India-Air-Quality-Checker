from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = "bb525f74dd4ca888d6fb690404bdcc60"

@app.route('/', methods=['GET', 'POST'])
def index():
    air_quality_info = None
    error_msg = None

    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if not city:
            error_msg = "Please enter a city name"
        else:
            try:
                # Get city coordinates
                geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},IN&limit=1&appid={api_key}"
                geo_response = requests.get(geo_url).json()

                if not geo_response:
                    error_msg = "City not found or no data available."
                else:
                    lat = geo_response[0]['lat']
                    lon = geo_response[0]['lon']

                    # Get air pollution data
                    air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
                    air_response = requests.get(air_url).json()

                    if 'list' not in air_response or not air_response['list']:
                        error_msg = "No air quality data for this location."
                    else:
                        aqi = air_response['list'][0]['main']['aqi']
                        aqi_mapping = {
                            1: ("Good", "green"),
                            2: ("Fair", "yellow"),
                            3: ("Moderate", "orange"),
                            4: ("Poor", "red"),
                            5: ("Very Poor", "purple")
                        }
                        category, color = aqi_mapping.get(aqi, ("Unknown", "gray"))
                        air_quality_info = {
                            'city': city.title(),
                            'aqi': aqi,
                            'category': category,
                            'color': color
                        }

            except Exception as e:
                error_msg = "Error fetching data."

    return render_template('index.html', air_quality=air_quality_info, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
