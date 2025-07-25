import requests

def get_city_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        city = response.json().get("city")
        return city
    except:
        return "Unknown"
