# Solution 2, greedy, meet most greedy children first, 
# though not all children are met, O(n*log(n) + n)
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        child = len(g)-1
        for i in range(len(s)-1,-1,-1):
            cookie = s[i]
            while child >= 0 and g[child] > cookie:
                child -= 1
            if child < 0:
                return len(s)-1-i
            child -= 1 # large cookie is given to most greedy children
        
        return len(s)

# Solution 1, greedy, meet least greedy children first, 
# all visited children must be meet, O(n*log(n) + n)
class Solution1(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()  # child
        s.sort()  # cookie
        
        child = 0
        
        for i, cookie in enumerate(s):
            if cookie >= g[child]:
                child += 1
            if child >= len(g):  # all children meeted
                return child
        
        return child
    
