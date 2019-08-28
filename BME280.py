import board
import busio
import digitalio
import adafruit_bme280
from time import sleep
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
spi = busio.SPI(clock=board.D21, MISO=board.D19, MOSI=board.D20)
cs = digitalio.DigitalInOut(board.D13)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)
##print("\nTemperature: %0.1f C" % bme280.temperature)
##print("Humidity: %0.1f %%" % bme280.humidity)
##print("Pressure: %0.1f hPa" % bme280.pressure)
bla = bme280.temperature

def BME280_TEMPERATURE():    
    BME280_TEMPERATURE = bme280.temperature
    sleep(1)
    return BME280_TEMPERATURE

def BME280_HUMIDITY():    
    BME280_HUMIDITY = bme280.humidity
    sleep(1)
    return BME280_HUMIDITY

def BME280_PRESSURE():    
    BME280_PRESSURE = bme280.pressure
    sleep(1)
    return BME280_PRESSURE

#print(BME280_PRESSURE())
