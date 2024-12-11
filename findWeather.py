import requests, json

api = '326787c2fc168765ccb63bf68eb90d18'

base_url = 'https://api.openweathermap.org/data/2.5/weather?'

city = input("enter the city name: ")

url = base_url + "q=" + city + "&units=metric" + "&appid=" + api

response = requests.get(url)
#print(response.text)

x = json.loads(response.text)

if x["cod"] != 404:
    y = x["main"]


    current_temp = y["temp"]
    current_pre = y["pressure"]
    current_hu = y["humidity"]

    z = x["weather"]

    weather_desc = z[0]["description"]

    print(f"temperature = {current_temp} the presure = {current_pre} the humidity = {current_hu}        description = {weather_desc}")


else:
    print("city not found")