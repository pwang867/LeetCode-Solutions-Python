# 2D dfs
# change definition of self.memo[(i, s)]: records the max count for seats[i+1:]
class Solution2(object):
    def maxStudents(self, seats):
        if not seats or not seats[0]:
            return 0
        self.res = 0
        self.memo = {}
        return self.dfs(seats, 0, 0)
    
    def dfs(self, seats, i, j):
        if j == len(seats[0]):
            s = "".join(seats[i])
            if (i, s) not in self.memo:
                self.memo[(i, s)] = self.dfs(seats, i+1, 0)
            return self.memo[(i, s)]
        elif i == len(seats):
            return 0
        else:
            if seats[i][j] == "#":
                return self.dfs(seats, i, j+1)
            else:
                res = 0
                if self.possible(seats, i, j):
                    seats[i][j] = "p"
                    res = max(res, 1 + self.dfs(seats, i, j+1))
                    seats[i][j] = "."
                res = max(res, self.dfs(seats, i, j+1))
                return res
    
    def possible(self, seats, i, j):
        for dx, dy in [(0, -1), (-1, 1), (-1, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(seats) and 0 <= q < len(seats[0]):
                if seats[p][q] == "p":
                    return False
        return True
    


# self.memo[(i, s)] records the max count for seats[:i+1]
class Solution1(object):
    def maxStudents(self, seats):
        if not seats or not seats[0]:
            return 0
        self.res = 0
        self.memo = {}
        self.dfs(seats, 0, 0, 0)
        return self.res
    
    def dfs(self, seats, i, j, cnt):
        if cnt + (len(seats)-1 - i)*len(seats[0]) + len(seats[0]) - j < self.res:  # early cutoff 1
            return
        if j == len(seats[0]):
            s = "".join(seats[i])
            if (i, s) in self.memo and self.memo[(i, s)] >= cnt:   # memorization, dp
                return
            self.memo[(i, s)] = cnt
            self.dfs(seats, i+1, 0, cnt)
        elif i == len(seats):
            self.res = max(self.res, cnt)
        else:
            if seats[i][j] == "#":
                self.dfs(seats, i, j+1, cnt)
            else:
                if self.possible(seats, i, j):
                    seats[i][j] = "p"
                    self.dfs(seats, i, j+1, cnt+1)
                    seats[i][j] = "."
                self.dfs(seats, i, j+1, cnt)
    
    def possible(self, seats, i, j):
        for dx, dy in [(0, -1), (-1, 1), (-1, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(seats) and 0 <= q < len(seats[0]):
                if seats[p][q] == "p":
                    return False
        return True


"""
Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

 

Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
 

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8
"""
