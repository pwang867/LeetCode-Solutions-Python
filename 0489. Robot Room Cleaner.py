# method 2, time/space O(n)
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.dfs(0, 0, robot, 0, set())

    def dfs(self, i, j, robot, k, visited):
        # (i, j) is current position, self.dirs[k] is direction
        # the robot will return to its initial position and direction after dfs finishes
        robot.clean()
        visited.add((i, j))
        for m in range(4):
            dx, dy = self.dirs[(k + m) % 4]
            p, q = i + dx, j + dy
            if (p, q) not in visited and robot.move():  # the order of check visited and .move() matters!
                self.dfs(p, q, robot, (k + m) % 4, visited)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
            else:
                robot.turnRight()



# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution1(object):
    def __init__(self):
        self.cleaned = set()
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.idir = 0  # 0 means up, 1 right, 2 down, 3 left
        self.pos = (1, 3)

    def turn_right(self, robot):
        self.idir = (self.idir + 1) % 4
        robot.turnRight()

    def turn_left(self, robot):
        self.idir = (self.idir + 3) % 4
        robot.turnLeft()

    def move_robot(self, robot):
        # move the robot and update the position
        dx, dy = self.dirs[self.idir]
        next_pos = (self.pos[0] + dx, self.pos[1] + dy)
        if next_pos not in self.cleaned and robot.move():
            self.cleaned.add(next_pos)
            self.pos = next_pos
            return True
        else:
            return False

    def backtrack(self, robot):
        dx, dy = self.dirs[self.idir]
        if robot.move():  # going back, so ignore if it is cleaned
            self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None

        go back to where it comes from after finishing this function
        and the direction will be opposite to when it comes
        """
        robot.clean()
        # go straight
        if self.move_robot(robot):
            self.cleanRoom(robot)
            self.turn_left(robot)
        else:
            self.turn_right(robot)
        # go right
        if self.move_robot(robot):
            self.cleanRoom(robot)
        else:
            self.turn_left(robot)
            self.turn_left(robot)
        # go left
        if self.move_robot(robot):
            self.cleanRoom(robot)
            self.turn_right(robot)
        else:
            self.turn_left(robot)
        # go down
        if self.move_robot(robot):
            self.cleanRoom(robot)
            self.turn_right(robot)
            self.turn_right(robot)
        # go back
        self.backtrack(robot)


"""
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally. 
You must solve this problem "blindfolded". In other words, you must control the robot using only 
the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""

