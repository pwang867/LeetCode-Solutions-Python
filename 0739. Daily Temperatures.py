# maintain a decreasing stack, time/space O(n)
# same as: 496. Next Greater Element I
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        wait = [0]*len(T)  # days to wait for a warmer day
        
        stack = []  # list of tuples (temp, index)
        
        for i in range(len(T)):
            if stack and T[i] > stack[-1][0]:
                while stack and T[i] > stack[-1][0]:
                    temp, index = stack.pop()
                    wait[index] = i - index
            stack.append((T[i], i))
        
        return wait

    
"""
Given a list of daily temperatures T, return a list such that, 
for each day in the input, tells you how many days you would have to wait 
until a warmer temperature. If there is no future day for which this is possible,
 put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
 your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].
"""

