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
    carsc.write(f"Number of Cars={NrOCars}\n")          #configure cars
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
            carsc.write(f"Car={i}=all\n")
            continue
        carsc.write(f"car{i}={cars[i].floors}\n")
    carsc.close()
    return cars

def initCars(levels):
    cars =[]
    calls = []

    cr = open("CarConfig.uma", "r")
    numberOCars =cr.readline(-1)
    numberOCars.split("=")
    numberOCars = int(numberOCars[1])
    for i in range(0,numberOCars):
        currentCar = cr.readline(-1)
        currentCar = currentCar.split("=")
        if currentCar[2] == "all":
            for i in range (0, len(levels)):# working on this





        cars.append(Car(0, level, calls, 0.0, i))
