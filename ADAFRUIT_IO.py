#!/usr/bin/python3
#import Adafruit IO REST client.

from Adafruit_IO import Client
from cpu_temperature import *
from SDS011_PM import *
from MCP3008_VOC import *
from MCP3008_LDR import *
from BME280 import *
from weather import *
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'your Key'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'your Username'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
pi_CPU_temperature = aio.feeds('cputemperature')
pi_SDS011_PMtwofive = aio.feeds('smalparticelmatter')
pi_SDS011_PMten = aio.feeds('bigparticelmatter')
pi_MCP3008_LDR = aio.feeds('ldrsensor')
pi_MCP3008_VOC = aio.feeds('vocsensor')
pi_BME280_TEMPERATURE = aio.feeds('bme280temperature')
pi_BME280_HUMIDITY = aio.feeds('bme280humidity')
pi_BME280_PRESSURE = aio.feeds('bme280pressure')
pi_API_HUMIDITY = aio.feeds('apihumidity')
pi_API_TEMPERATURE = aio.feeds('apitemperature')

while True:
    aio.send(pi_CPU_temperature.key,cpu_temperature())
    aio.send(pi_SDS011_PMtwofive.key,SDS011_PMtwofive())
    aio.send(pi_SDS011_PMten.key,SDS011_PMten())
    aio.send(pi_MCP3008_LDR.key,MCP3008_LDR())
    aio.send(pi_MCP3008_VOC.key,MCP3008_VOC())
    aio.send(pi_BME280_TEMPERATURE.key,BME280_TEMPERATURE())
    aio.send(pi_BME280_HUMIDITY.key,BME280_HUMIDITY())
    aio.send(pi_BME280_PRESSURE.key,BME280_PRESSURE())
    aio.send(pi_API_HUMIDITY.key,API_HUMIDITY())
    aio.send(pi_API_TEMPERATURE.key,API_TEMPERATURE())   
    sleep(40)
