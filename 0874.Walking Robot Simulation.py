class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        cur = (0, 1)  # current direction
        pos = (0, 0)
        obstacles = set(map(tuple, obstacles))
        max_dist = 0
        for num in commands:
            command = num
            if command < 0:
                cur = self.getNextDirection(cur, command)
            else:
                while command > 0:
                    if (pos[0]+cur[0], pos[1]+cur[1]) in obstacles:
                        break
                    else:
                        pos = (pos[0]+cur[0], pos[1]+cur[1])
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
        
