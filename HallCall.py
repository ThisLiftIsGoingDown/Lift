class HallCall:
    def __init__(self, active, level, dirUP, dirDN, car):
        self.active = active
        self.level = level
        self.dirUP = dirUP
        self.dirDN = dirDN
        self.car = car
    def get_hall_call(self):
        if self.active:
            dir = 0
            l = self.level
            if self.dirDN:
                dir -= 1
            if self.dirUP:
                dir += 1
            return l, dir
        return None