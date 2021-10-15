class Mover:
    directionDelta = {"right": [0, 1], "left":[0, -1], 
                            "up":[-1, 0], "down":[1, 0]}

    def move(self, curr_x, curr_y, direction):
        delta = Mover.directionDelta[direction]
        curr_x+=delta[0]
        curr_y+=delta[1]

        if curr_x < 0 or curr_x > 9 or curr_y < 0 or curr_y > 9:
            raise ValueError("Grid dimensions are 10 X 10. Can not move in this direction")
        return curr_x, curr_y

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveRobot(self, directions):
        mover = Mover()
        for direction in directions:
            self.x, self.y = mover.move(self.x, self.y, direction)
        print("Robot's current position in grid is: " + str(self.x) + ", " + str(self.y))

if __name__ == "__main__":
    s = Robot(0, 0)
    s.moveRobot(["right", "left", "right", "down", "down"])