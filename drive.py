from main import *
def position(t1, t2, currentposition, currentspeed):   # Position ausrechnen
    timer1 = t2 - t1
    currentposition = currentposition + (timer1 * currentspeed)
    return currentposition
def sigmoid (x):
    return (x / (1 + abs(x)))


def leveling(currentpositionl, callheight):
    distanceToFloor = callheight - currentpositionl
    levelSpd = sigmoid(distanceToFloor/400)    #Calculating optimal speed for leveling
    return levelSpd * spd