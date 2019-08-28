import time
import requests
from pprint import pprint
from time import sleep

city = 'Huttwil,ch' #input('Enter your City: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&mode=json&APPID=0368e81d5eeae2f5dc7f690f3efc6dbd'.format(city)

res = requests.get(url)

data = res.json()

Sunrise_in_houers = int(time.strftime("%H", time.localtime(data['sys']['sunrise']))) * 60
Sunrise_in_minutes = int(time.strftime("%M", time.localtime(data['sys']['sunrise'])))
Sunrise_in_a_rounded_minute = round((float(time.strftime("%S", time.localtime(data['sys']['sunrise'])))) / 60)
Sunrise_in_minutes_of_the_day = int(Sunrise_in_houers + Sunrise_in_minutes + Sunrise_in_a_rounded_minute)

Sunset_in_houers = int(time.strftime("%I", time.localtime(data['sys']['sunset']))) * 60 #%I or %H for 12 or 24 houer format
Sunset_in_minutes = int(time.strftime("%M", time.localtime(data['sys']['sunset'])))
Sunset_in_a_rounded_minute = round((float(time.strftime("%S", time.localtime(data['sys']['sunset'])))) / 60)
Sunset_in_minutes_of_the_day = int(Sunset_in_houers + Sunset_in_minutes + Sunset_in_a_rounded_minute)

sunset = time.strftime(" %H:%M:%S", time.localtime(data['sys']['sunset']))
clouds = data['clouds']['all']
temp = data['main']['temp']
rain = data['sys']
humidity = data['main']['humidity']
##print(Sunrise_in_minutes_of_the_day)
##print(Sunset_in_minutes_of_the_day)
##print(clouds)
##print('Temperatur: {}'.format(temp))
##pprint(data)

def API_HUMIDITY():    
    API_HUMIDITY = humidity
    sleep(1)
    return API_HUMIDITY

def API_TEMPERATURE():    
    API_TEMPERATURE = temp
    sleep(1)
    return API_TEMPERATURE

#print(API_HUMIDITY())
