from time import sleep
import datetime
from __init__ import *

def SDS011_PMtwofive():
    sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
    sensor.sleep(sleep=False)
##    sleep(15)
    sensor.query()
    data = sensor.query()
    a,b = data
##    sensor.sleep()
##    sleep(30)
##    sensor.sleep(sleep=False)
    return a

def SDS011_PMten():
    sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
    sensor.sleep(sleep=False)
##    sleep(15)
    sensor.query()
    data = sensor.query()
    a,b = data
##    sensor.sleep()
##    sleep(30)
##    sensor.sleep(sleep=False)
    return b



