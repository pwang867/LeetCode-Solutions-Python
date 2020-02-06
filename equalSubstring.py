class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        costs = [self.getCost(s[i], t[i]) for i in range(len(s))]
        sums = [0]*(len(costs)+1)
        
        total = 0
        for i in range(1, len(sums)):
            total += costs[i-1]
            sums[i] = total
#        print(sums)
        
        res = 0
        for i in range(1, len(sums)):
            j = self.binarySearch(sums, i, sums[i-1]+maxCost)
            if j != -1:
                res = max(res, j-i+1)
        return res
        
    
    def getCost(self, a, b):
        return abs(ord(a) - ord(b))
    
    def binarySearch(self, sums, start, target):
        # find the index of the last number <= target
        left, right = start, len(sums)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if sums[mid] <= target:
                left = mid
            else:
                right = mid
        if sums[right] <= target:
            return right
        elif sums[left] <= target:
            return left
        else:
            return -1

s = ""
t = ""
maxCost = 0
print(Solution().equalSubstring(s, t, maxCost))
        