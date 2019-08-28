from time import sleep
from gpiozero import CPUTemperature

def cpu_temperature():    
    cpu = CPUTemperature()
    cpu_temperature = cpu.temperature
    sleep(1)
    
    return cpu_temperature





