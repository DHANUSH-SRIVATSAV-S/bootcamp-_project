import request 
import os
from datetime import datetime

user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")
#printed from website: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}



complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()
# print (api_data)

if api_data['cod'] == '404':
   print ("Invalid City: {}, Please check your City name",format(location))
else:
    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime(%d %b %y | %I:%M:%S %P)

    print("-----------------------------------------------------------------")
    print("Weather Stats for - {} || {}",format(location.upper(), date_time))
    print("------------------------------------------------------------------")

    print("Current temprature is: {:.2f} deg c".format(temp_city))
    print("Current weather desc :",weather_desc)
    print("Current Humidity     :,hmdt, '%')
    print("Current wind speed   :",wind_spd ,'kmph')


