import requests

key = "API_KEY"
url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Give a city name: \n")

params = {
    "q": city,      
    "appid": key,       
    "units": "metric"  
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code, response.text)
