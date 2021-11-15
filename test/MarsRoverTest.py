import unittest

from test.MarsRover import MarsRover
#from parameterized import parameterized

class MarsRoverTest(unittest.TestCase):

    def test_rover_turns_right_from_north(self):
        rover = MarsRover("N", 0, 0)
        rover.go("R")
        self.assertEqual("E", rover.direction)  # add assertion here

    def test_rover_turns_right_from_east(self):
        rover = MarsRover("E", 0, 0)
        rover.go("R")
        self.assertEqual("S", rover.direction)  # add assertion here

    def test_rover_turns_right_from_south(self):
        rover = MarsRover("S", 0, 0)
        rover.go("R")
        self.assertEqual("W", rover.direction)  # add assertion here

    def test_rover_turns_right_from_west(self):
        rover = MarsRover("W", 0, 0)
        rover.go("R")
        self.assertEqual("N", rover.direction)  # add assertion here

    def test_rover_turns_left_from_north(self):
        rover = MarsRover("N", 0, 0)
        rover.go("L")
        self.assertEqual("W", rover.direction)  # add assertion here

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("W", 0, 0)
        rover.go("L")
        self.assertEqual("S", rover.direction)

    def test_rover_turns_left_from_south(self):
        rover = MarsRover("S", 0, 0)
        rover.go("L")
        self.assertEqual("E", rover.direction)

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("E", 0, 0)
        rover.go("L")
        self.assertEqual("N", rover.direction)

    def test_moves_forward_when_facing_north(self):
        rover = MarsRover("N",0,0)
        rover.go("F")
        self.assertEqual(1, rover.yposition)

    def test_moves_forward_when_facing_east(self):
        rover = MarsRover("E",0,0)
        rover.go("F")
        self.assertEqual(1, rover.xposition)

    def test_moves_forward_when_facing_south(self):
        rover = MarsRover("S", 0, 0)
        rover.go("F")
        self.assertEqual(-1, rover.yposition)

    def test_moves_forward_when_facing_west(self):
        rover = MarsRover("W", 0, 0)
        rover.go("F")
        self.assertEqual(-1, rover.xposition)

    def test_moves_backward_when_facing_north(self):
        rover = MarsRover("N", 0, 0)
        rover. go("B")
        self.assertEqual(-1, rover.yposition)

    def test_moves_backward_when_facing_east(self):
        rover = MarsRover("E", 0, 0)
        rover.go("B")
        self.assertEqual(-1, rover.xposition)

    def test_moves_backward_when_facing_south(self):
        rover = MarsRover("S", 0, 0)
        rover.go("B")
        self.assertEqual(1, rover.yposition)

    def test_moves_backward_when_facing_south(self):
        rover = MarsRover("W", 0, 0)
        rover.go("B")
        self.assertEqual(1, rover.xposition)

if __name__ == '__main__':
    unittest.main()
