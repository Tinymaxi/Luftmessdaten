import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from time import sleep
from adafruit_mcp3xxx.analog_in import AnalogIn
#spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
spi = busio.SPI(clock=board.D21, MISO=board.D19, MOSI=board.D20)
cs = digitalio.DigitalInOut(board.D25)
mcp = MCP.MCP3008(spi, cs)
channel = AnalogIn(mcp, MCP.P0)
##print('VOC Raw ADC Value: ', channel.value)
##print('VOC ADC Voltage: ' + str(channel.voltage) + 'V')

def MCP3008_VOC():    
    MCP3008_VOC = channel.value
    sleep(1)
    return MCP3008_VOC

#print(MCP3008_VOC())
