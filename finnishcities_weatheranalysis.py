#Imports
import requests, json, random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


#API key and URL
key = "API_KEY"
url = "https://api.openweathermap.org/data/2.5/weather"

#JSON file with city info
database="city.list.json"

#Lists
finnish_cities = []
data_list=[]

#Open JSON file and turn it to dictionary
with open(database, mode="r", encoding="utf-8") as read_data:
    cities = json.load(read_data)

#Loop through dictionary and put the finnish cities to a list
for i in cities:
    if i["country"] == "FI":
        finnish_cities.append(i)

#Take 100 random finnish cities
random_finnish_cities = random.sample(finnish_cities, 100)

#Loop through the list
for city in random_finnish_cities:
    #Params for API call
    params = {
        "id": city["id"],      
        "appid": key,       
        "units": "metric"  
    }

    response = requests.get(url, params=params)
    #Add the response to data_list
    if response.status_code == 200:
        data = response.json()
        data_list.append({"city": data["name"],
                          "temp": data["main"]["temp"],
                          "lat": data["coord"]["lat"],
                          "lon": data["coord"]["lon"]
                          })
    else:
        print("Error:", response.status_code, response.text)

#Make the 100 random finnish cities weather to a dataframe
df = pd.DataFrame(data_list)
#Assign temperature,latitude to x,y
x = df["temp"].values
y = df["lat"].values

# Calculate correlation
slope, intercept, r_value, p_value, std_err = linregress(x, y)
correlation = r_value  


#Visualize correlation text
plt.text(min(x), max(y), f"Correlation: {correlation:.2f}", fontsize=12,
         bbox=dict(facecolor='white', alpha=0.5))
#Visualize line
plt.plot(x, intercept + slope*x, color='black', label='Trend line')

#Visualize by making a scatter
colors = x
plt.scatter(x, y, c=colors, cmap='coolwarm', s=50)
plt.xlabel("Temperature (°C)")
plt.ylabel("Latitude")
plt.title("Latitude vs Temperature in Finnish Cities")
plt.show()
