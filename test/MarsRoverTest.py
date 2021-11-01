import unittest


class MarsRover(object):
    def __init__(self, direction, xposition, yposition):
        self.direction = direction
        self.xposition = xposition
        self.yposition = yposition

    def turnRight(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

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


class MarsRoverTest(unittest.TestCase):
    def test_rover_turns_right_from_north(self):
        rover = MarsRover("N", 0, 0)
        rover.turnRight()
        self.assertEqual("E", rover.direction)  # add assertion here

    def test_rover_turns_right_from_east(self):
        rover = MarsRover("E", 0, 0)
        rover.turnRight()
        self.assertEqual("S", rover.direction)  # add assertion here

    def test_rover_turns_right_from_south(self):
        rover = MarsRover("S", 0, 0)
        rover.turnRight()
        self.assertEqual("W", rover.direction)  # add assertion here

    def test_rover_turns_right_from_west(self):
        rover = MarsRover("W", 0, 0)
        rover.turnRight()
        self.assertEqual("N", rover.direction)  # add assertion here

    def test_rover_turns_left_from_north(self):
        rover = MarsRover("N", 0, 0)
        rover.turnLeft()
        self.assertEqual("W", rover.direction)

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("W", 0, 0)
        rover.turnLeft()
        self.assertEqual("S", rover.direction)

    def test_rover_turns_left_from_south(self):
        rover = MarsRover("S", 0, 0)
        rover.turnLeft()
        self.assertEqual("E", rover.direction)

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("E", 0, 0)
        rover.turnLeft()
        self.assertEqual("N", rover.direction)

    def test_moves_forward_north_from_00(self):
        rover = MarsRover("N", 0, 0)
        rover.moveForward()
        self.assertEqual(0, 1, rover.yposition)


if __name__ == '__main__':
    unittest.main()
