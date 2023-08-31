import requests
import json
import pyttsx3

print("************WELCOME TO THE WHEATER TELLER*************************")
city = input("enter the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=55135cf22be74f6991993545233108&q={city}"

info = requests.get(url)
dic = json.loads(info.text)

engine = pyttsx3.init()
engine.setProperty('rate',110)
engine.setProperty('volume',110)


temp_c = dic["current"]["temp_c"]
s = f"the temperature of {city} in celcius is {temp_c}"
engine.say(s)
engine.runAndWait()
print("temperature in celcius is ",temp_c)

temp_f = dic["current"]["temp_f"]
q = f"the temperature of {city} in fehrenite is {temp_f}"
engine.say(q)
engine.runAndWait()
print("temperature in fehrenite is ",temp_f)

wind_mph = dic["current"]["wind_mph"]
w = f"the speed of wind in {city}  in miles per hour is {wind_mph}"
engine.say(w)
engine.runAndWait()
print("wind speed in mph: ",wind_mph)

wind_kph = dic["current"]["wind_kph"]
s = f"the speed of wind in {city}  in kilometer per hour is {wind_kph}"
engine.say(s)
engine.runAndWait()
print("wind speed in kph: ",wind_kph)

humidity = dic["current"]["humidity"]
g = f"humidity in {city} is {humidity} percent"
engine.say(g)
engine.runAndWait()
print("humidity: ",humidity,"%")

text = dic["current"]["condition"]["text"]
c = f"the condition of {city} is {text}"
engine.say(c)
engine.runAndWait()
print("condition is: ",text)





