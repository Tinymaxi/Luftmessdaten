import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from time import *

from adafruit_mcp3xxx.analog_in import AnalogIn
#spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
spi = busio.SPI(clock=board.D21, MISO=board.D19, MOSI=board.D20)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
channel1 = AnalogIn(mcp, MCP.P0)
##print('LDR Raw ADC Value: ', channel1.value)
##print('LDR ADC Voltage: ' + str(channel1.voltage) + 'V')

def MCP3008_LDR():    
    MCP3008_LDR = channel1.value
    sleep(1)
    return MCP3008_LDR

#print(MCP3008_LDR())
