class MarsRover(object):
    def __init__(self, direction, xposition, yposition):
        self.direction = direction
        self.xposition = xposition
        self.yposition = yposition

    def turnRight(self):
        compass = ["N", "E", "S", "W"]
        self.direction = compass[(compass.index(self.direction) + 1) % 4]


    def turnLeft(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "N"

    def moveForward(self):
        if self.direction == "N":
            self.yposition = +1
