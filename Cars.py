from Levels import Level

class Car():
    def __init__(self, pos, floors, calls , speed , carnr, dir):
        self.floors = floors
        self.calls = calls
        self.pos = pos
        self.speed = speed
        self.carnr = carnr
        self.dir = dir
    def erase_floors(self):
        g =[]
        self.floors = g

    def append_floor(self,mode,floormd):
        d = ["all"]
        if mode == "all":
            self.erase_floors()
            self.floors = d
        else:
            self.floors.append(floormd)