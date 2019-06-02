class Bomb:

    X_DISPLACEMENT = 67
    Y_DISPLACEMENT = 14

    def __init__(self):
        self.timer = 30

    def setTimer(self, time):
        self.timer = time

    def tick(self):
        if(self.timer > 0):
            self.timer -= 1

    def defuse(self, code):
        if(self.code == code):
            return True
        else:
            return False
