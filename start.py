from Levels import Level
import time
from Cars import Car
"""Collection of all initialisation functions to setup and read data from config files """
def onstartup():
    initCompleted = open("qwe.uma", "r")
    tmp = initCompleted.read(-1)                # Check if setup has beeen completed, if yes returns  True
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
    levels = list()                                         #Setup the config files by the means of console
    levelHeightTemp = 0                                     #Writes data to config according to config syntax
    config.write(f"Number of Levels={numberOfLevels}\n")    #also saves config stuff to objects
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
    time.sleep(0.2)         #Silly wait animation just becaus of randomness
    print(f"..")
    time.sleep(0.5)
    print(f"...OK!")
    zeh = open("qwe.uma", "w")
    zeh.write("Completed=1")            # completed set to 1 to know setup completed
    zeh.close()
    return levels


def readConfig():
    config = open("Levels.uma", "r")
    levels = list()
    Lines = config.readlines(-1)
    lineinit = Lines[0]
    lineinit = lineinit.split("=")  # read data from level.uma and put it into level objects
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
    levelcount = len(lev)         #Create level obj initialise and give height
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
    carsc.write(f"{NrOCars}")          #Configures car properties into object and config file
    level = ["all"]
    cars = []
    calls = []
    for i in range(0,NrOCars):
        cars.append(Car(0,level, calls, 0.0 , i))
        print(f"does the car nr. {i} stop at all the floors?(y/n)")
        temp = input()
        temp.lower()
        if temp != "y":
            cars[i].erase_floors()
            for m in range(0, len(levels)):
                print(f"does the car nr. {i} stop at floor {m}")
                temp1 = input()
                temp1.lower()
                if temp1 == "y":
                    cars[i].append_floor("exclusive",True)
                else: cars[i].append_floor("exclusive", False)
        else:
            carsc.write(f"\nall")
            continue
        carsc.write(f"\n{cars[i].floors}")
    carsc.close()
    return cars

def initCars(levels):
    cars =[]
    cr = open("CarConfig.uma", "r")
    numberOCars =int(cr.readline(-1))               #Reads data from config
    for i in range(0,numberOCars):
        calls = []
        currentCar = cr.readline(-1)
        if currentCar == "all":
            cars.append(Car(0, ["all"], calls, 0.0, i))
        else:
            currentCar = currentCar.strip("[")
            currentCar = currentCar[:len(currentCar)-2]
            currentCar = currentCar.strip("\n")
            currentCar = currentCar.split(",")
            levels = []
            for level in currentCar:
                levels.append(eval(level))
            cars.append(Car(0, levels, calls, 0.0, i))
    return cars