class Level:
    def __init__(self, levelheight, locked, fireFl ,name):
        self.levelheight = levelheight
        self.locked = locked
        self.fireFl = fireFl
        self.name = name

    def get_level(self):
        return self.level

    def set_Firefl(self):
        self.fireFl = True
        return self

    def get_auth(self):
        return self.locked

    def get_firefl(self):
        return self.fireFl