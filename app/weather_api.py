import requests

def get_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()
    
    current = data['current_condition'][0]
    return {
        'temperature': float(current['temp_C']),
        'humidity': float(current['humidity']),
        'rainfall': float(current['precipMM'])
    }