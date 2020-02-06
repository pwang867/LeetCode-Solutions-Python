# brute force, time O(2^n)
class Solution(object):
    def __init__(self):
        self.res = float('inf')
        self.memo = {}
    
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.minMoveHelper(tuple(arr), 0)
        return self.res
    
    def minMoveHelper(self, arr, move):
        if not arr:
            self.res = min(self.res, move)
            return 0
        if move > self.res:
            return float('inf')
        if arr in self.memo:
            return self.memo[arr]
        res = float('inf')
        for i in range(len(arr)):
            for j in range(len(arr)-1, i-1, -1):
                if self.isPalindrome(arr, i, j):
                    res = min(res, 1+self.minMoveHelper(tuple(arr[:i]+arr[j+1:]), move+1))
                    break
        self.memo[arr] = res
        return res
    
    def isPalindrome(self, arr, i, j):
        if not arr:
            return True
        while i <= j:
            if arr[i] != arr[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    

arr = [4,1,14,16,15,18,19,17,10,8,10,4,19,17,14,17,2,1,14,11]
print(Solution().minimumMoves(arr))

