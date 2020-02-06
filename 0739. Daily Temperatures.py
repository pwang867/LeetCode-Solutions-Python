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
    
