import pos
import threading
import time
from Levels import Level
import start

currentPosition = 0
currentSpeed = 1
spd = 1
callHeight = 0




onstup = start.onstartup()
if onstup == False:
    Levit = start.ConfigInit()
    cars = start.ConfigCars(Levit)
    print (cars[0].floors)
else:
    Levit = start.readConfig()
    cars =start.initCars(Levit)
    print(cars[0].floors)
levels = start.initlevels(Levit)
while True:
    t1 = time.time()
    distanceRemaining = callHeight - currentPosition
    t2 = time.time()
