from BME280 import *
from MCP3008_LDR import *
from MCP3008_VOC import *
from time import sleep

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print('VOC Raw ADC Value: ', channel.value)
    print('VOC ADC Voltage: ' + str(channel.voltage) + 'V')
    print('LDR Raw ADC Value: ', channel1.value)
    print('LDR ADC Voltage: ' + str(channel1.voltage) + 'V')
    sleep(1)
