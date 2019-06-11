class Bomb:

    X_DISPLACEMENT = 67
    Y_DISPLACEMENT = 14

    def __init__(self):
        self.timer = 30
        self.defuseLevel = 1

    def setTimer(self, time):
        self.timer = time

    def tick(self):
        if(self.timer > 0):
            self.timer -= 1

    def defuse(self):
        self.defuseLevel -= 1

    def isDefused(self):
        if(self.defuseLevel <= 0):
            return True
        else:
            return False
