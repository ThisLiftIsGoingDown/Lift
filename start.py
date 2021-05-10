from Levels import Level
import time
from Cars import Car
def onstartup():
    initCompleted = open("qwe.uma", "r")
    tmp = initCompleted.read(-1)                # is lift initialsied?
    tmp1 = tmp.split("=")
    if tmp1[1] == "0":
        initCompleted.close
        return False
    else:
        initCompleted.close
        return True


def ConfigInit():
    config = open("Levels.uma", "w")
    print("Welcome to the Lift Setup Assistant", "\n" + "Please Enter your number of Levels: ")
    numberOfLevels = input()
    numberOfLevels = int(numberOfLevels)
    levels = list()                                         # initialize levels .uma, and setup floors
    levelHeightTemp = 0
    config.write(f"Number of Levels={numberOfLevels}\n")
    for i in range(0, numberOfLevels):
        print(f"Type the height of Level {i}: \n")
        levelHeightTemp = input()
        levelHeightTemp = int(levelHeightTemp)
        config.write(f"Height of level {i}={levelHeightTemp}\n")
        levels.append(levelHeightTemp)
    config.close()
    fire = open("FireFl.uma", "w")
    print(f"Please Enter your Fire Level (must be in range from 0 to {len(levels) - 1})")
    while True:
        firetemp = input()                      #Configuring Fire level
        firetemp = int(firetemp)
        if firetemp < 0 or firetemp > len(levels):
            print(f"Please enter a valid Fire level (must be in range from 0 to {len(levels) - 1})")
        else:
            break
    fire.write(f"Fire Floor is:{firetemp}")
    print(f"The Fire Floor is now set to {firetemp}")
    fire.close
    print(f"Starting Car Setup assistant ...")
    time.sleep(0.2)
    print(f".")
    time.sleep(0.2)
    print(f"..")
    time.sleep(0.5)
    print(f"...OK!")
    ConfigCars()
    zeh = open("qwe.uma", "w")
    zeh.write("Completed=1")            # completed set to 1 to know setup completed
    zeh.close()
    return levels


def readConfig():
    config = open("Levels.uma", "r")
    levels = list()
    Lines = config.readlines(-1)
    lineinit = Lines[0]
    lineinit = lineinit.split("=")  # read data from level.uma
    lineinit = lineinit[1]
    lineinit = int(lineinit)
    for m in range(1, lineinit + 1):
        temp = Lines[m]
        temp = temp.split("=")
        temp = temp[1]
        temp = int(temp)
        levels.append(temp)
    config.close()
    return levels


def initlevels(lev):
    levelcount = len(lev)         #Level obj erstellen und level height eingeben
    levels = []
    fre = open("FireFl.uma" , "r")
    firefl = fre.readline(-1)
    firefl = firefl.split(":")
    firefl = int(firefl[1])
    fre.close()
    for i in range(0, levelcount):
        levels.append(Level(lev[i], None, False, "---"))
        if i == firefl:
            levels[i].set_Firefl()
    return levels

def ConfigCars(levels):
    print(f"please enter the number of cars")
    carsc = open("CarConfig.uma" , "w")
    NrOCars = input()
    NrOCars = int(NrOCars)
    carsc.write(f"Number of Cars={NrOCars}")
    cars = []
    calls = []
    for i in range(0,NrOCars):
        cars.append(Car(0,"all", calls, 0.0 , i))




