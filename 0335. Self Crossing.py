# coding=utf-8
"""
# greedy, time O(n)

Categorize the self-crossing scenarios, there are 3 of them:
1. line i crosses line i-3
2. line i crosses line i-4
3. line i crosses line i-5
"""


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) <= 3:
            return False
        for i in range(3, len(x)):
            # 4th crosses 1st
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                return True
            # 5th coincides with 1st
            if i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                return True
            # 6th crosses 1st
            if i >= 5 and 0 <= x[i - 2] - x[i - 4] <= x[i] and 0 <= x[i - 3] - x[i - 1] <= x[i - 5]:
                return True
        return False



"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then 
x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. 
In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.



Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true
"""