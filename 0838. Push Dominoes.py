# find the closest "R" to the left, and closest "L" to the right

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if not dominoes:
            return ""
        
        n = len(dominoes)
        # left[i] is the distance from dominoes[i] to the closest "R" to its left
        left = [-1]*n  
        right = [-1]*n
        
        # find the closest "R"
        last_R = - float('inf')
        for i, c in enumerate(dominoes):
            if c == "R":
                last_R = i
            elif c == ".":
                left[i] = i - last_R
            else:  # easy to miss
                last_R = -float('inf')  
        
        # find the closest "L"
        last_L = float('inf')
        for i in range(n-1, -1, -1):
            c = dominoes[i]
            if c == "L":
                last_L = i
            elif c == ".":
                right[i] = last_L - i
            else:
                last_L = float('inf')
        
        # find final results
        res = []
        for i, c in enumerate(dominoes):
            if c != ".":
                res.append(c)
            else:
                if left[i] == right[i]:
                    res.append('.')
                elif left[i] > right[i]:
                    res.append('L')
                else:
                    res.append('R')
        
        return ''.join(res)
    
