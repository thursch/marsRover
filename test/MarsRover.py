class MarsRover(object):
    def __init__(self, direction, xposition, yposition):
        self.direction = direction
        self.xposition = xposition
        self.yposition = yposition

    def turnRight(self):
        compassClockwise = ["N", "E", "S", "W"]
        self.direction = compassClockwise[(compassClockwise.index(self.direction) + 1) % 4]

    def turnLeft(self):
        compassAnticlockwise = ["N", "W", "S", "E"]
        self.direction = compassAnticlockwise[(compassAnticlockwise.index(self.direction) + 1) % 4]

    def moveForward(self):
        if self.direction == "N":
            self.yposition += 1
        elif self.direction == "E":
            self.xposition += 1
        elif self.direction == "S":
            self.yposition -= 1
        else:
            self.xposition -= 1

