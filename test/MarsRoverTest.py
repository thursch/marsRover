import unittest

from test.MarsRover import MarsRover


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


if __name__ == '__main__':
    unittest.main()
