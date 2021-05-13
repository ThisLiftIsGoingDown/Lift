from main import *
from Cars import Car
"""Car Dispatch algorythm, this algorithm takes call inputs and calculates a call assignememt buonity ,
then assigns the call to the car with the highest value
!WORK IN PROGRESS"""
def dispatch(type, cldir, level, cars, call = level , carnr = -1):
    callt = open("CarConfig.uma" , "r")
    numberofcars = int(callt.readline(-1))
    callt.close()
    if type == "cc"
        if carnr == -1:
            return False
        cars[carnr].calls.append(level)
    for car in cars:
        if cldir != car.dir and car.dir != "st":

        for carcalls in car.calls:


#test