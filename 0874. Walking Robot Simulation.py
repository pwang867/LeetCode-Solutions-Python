# cartesian coordinate

# time O(n), space O(1)
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dir = (0, 1)  # current moving direction
        pos = (0, 0)
        obstacles = set(map(tuple, obstacles))
        max_dist = 0
        for command in commands:
            if command < 0:
                dir = self.getNextDirection(dir, command)
            else:
                while command > 0:
                    new_pos = (pos[0]+dir[0], pos[1]+dir[1])
                    if new_pos in obstacles:
                        break
                    else:
                        pos = new_pos
                        max_dist = max(max_dist, pos[0]**2 + pos[1]**2)
                        command -= 1
        return max_dist  # return maximum distance, not final position distance
    
    def getNextDirection(self, cur, command):
        # use z1 = z*e^(i*theta) to get rotation matrix
        # or we can use two dictionaries to get next direction 
        # d={(1,0):(0,1), ...}
        if command == -2:  # rotate CCW
            return (-cur[1], cur[0])
        if command == -1:  # CW
            return (cur[1], -cur[0])
        
"""
A robot on an infinite grid starts at point (0, 0) and faces north.  
The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous 
grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will 
be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""
