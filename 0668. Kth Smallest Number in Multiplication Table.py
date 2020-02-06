# do binary search on the final result
# time O(log(k)*min(m,n)), space O(1)
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # check 1 <= k <= m*n
        
        if m > n:  # greatly reduce time
            m, n = n, m
        
        left, right = 1, m*n
        while left + 1 < right:
            mid = left + (right - left) // 2
            cnt = self.count(m, n, mid)
            if cnt >= k:
                right = mid
            else:
                left = mid
        
        if self.count(m, n, left) >= k:
            return left
        else:
            return right
        
    def count(self, m, n, guess):
        cnt = 0
        for i in range(1, m+1):
            cnt += min(guess//i, n)
        return cnt
    
