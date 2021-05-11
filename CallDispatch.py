from main import *
from Cars import Car
"""Car Dispatch algorythm, this algorithm takes call inputs and calculates a call assignememt buonity ,
then assigns the call to the car with the highest value
!WORK IN PROGRESS"""
def dispatch(type, dir, level, cars, calls):
    callt = open("CarConfig.uma" , "r")
    numberofcars = int(callt.readline(-1))
    callt.close()
    for car in cars:
        for carcalls in cars.calls
