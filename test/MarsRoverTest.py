import unittest

from test.MarsRover import MarsRover


class MarsRoverTest(unittest.TestCase):
    def test_rover_turns_right_from_north(self):
        rover = MarsRover("N", 0, 0, "R")
        rover.move()
        self.assertEqual("E", rover.direction)  # add assertion here

    def test_rover_turns_right_from_east(self):
        rover = MarsRover("E", 0, 0, "R")
        rover.move()
        self.assertEqual("S", rover.direction)  # add assertion here

    def test_rover_turns_right_from_south(self):
        rover = MarsRover("S", 0, 0, "R")
        rover.move()
        self.assertEqual("W", rover.direction)  # add assertion here

    def test_rover_turns_right_from_west(self):
        rover = MarsRover("W", 0, 0,"R")
        rover.move()
        self.assertEqual("N", rover.direction)  # add assertion here

    def test_rover_turns_left_from_north(self):
        rover = MarsRover("N", 0, 0,"L")
        rover.move()
        self.assertEqual("W", rover.direction)

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("W", 0, 0,"L")
        rover.move()
        self.assertEqual("S", rover.direction)

    def test_rover_turns_left_from_south(self):
        rover = MarsRover("S", 0, 0,"L")
        rover.move()
        self.assertEqual("E", rover.direction)

    def test_rover_turns_left_from_west(self):
        rover = MarsRover("E", 0, 0,"L")
        rover.turnLeft()
        self.assertEqual("N", rover.direction)

    def test_moves_forward_when_facing_north(self):
        rover = MarsRover("N",0,0,"F")
        rover.moveForward()
        self.assertEqual(1, rover.yposition)

    def test_moves_forward_when_facing_east(self):
        rover = MarsRover("E",0,0,"F")
        rover.moveForward()
        self.assertEqual(1, rover.xposition)

    def test_moves_forward_when_facing_south(self):
        rover = MarsRover("S", 0, 0,"F")
        rover.moveForward()
        self.assertEqual(-1, rover.yposition)

    def test_moves_forward_when_facing_west(self):
        rover = MarsRover("W", 0, 0,"F")
        rover.moveForward()
        self.assertEqual(-1, rover.xposition)

    def test_moves_backward_when_facing_north(self):
        rover = MarsRover("N", 0, 0,"B")
        rover.moveBackward()
        self.assertEqual(-1, rover.yposition)

    def test_moves_backward_when_facing_east(self):
        rover = MarsRover("E", 0, 0,"B")
        rover.moveBackward()
        self.assertEqual(-1, rover.xposition)

    def test_moves_backward_when_facing_south(self):
        rover = MarsRover("S", 0, 0,"B")
        rover.moveBackward()
        self.assertEqual(1, rover.yposition)

    def test_moves_backward_when_facing_south(self):
        rover = MarsRover("W", 0, 0,"B")
        rover.moveBackward()
        self.assertEqual(1, rover.xposition)

if __name__ == '__main__':
    unittest.main()
