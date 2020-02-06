# method 1: dp
# dp[i][j] means the number of sequences of length >=2 (not >=3) 
# ending with A[i] and with an increment of j
# dp[i] is a dictionary, because the range of increment is unknown 
# and the increment might be negative

from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        
        dp = [defaultdict(int) for _ in range(n)]
        
        cnt = 0
        for i in range(2, n):
            for j in range(0, i):
                d = A[i] - A[j]
                if d in dp[j]:
                    cnt += dp[j][d]
                    dp[i][d] += dp[j][d] + 1  # +1 means the sequence (A[j], A[i])
                else:
                    dp[i][d] += 1
        
        return cnt

# method 0 wrong solution, duplicates are hard to deal with
# fails at case: A = [1,1,1,1,2,1]
# brute force, time O(n^3)
# pick first two numbers from A, and then the subsequence is searched
class Solution0(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        
        res = 0
        for i in range(len(A)-2):
            for j in range(i+1, len(A)-1):
                print(i, j)
                res += self.countSubsequence(A, j, A[j]-A[i])
        
        return res
    
    def countSubsequence(self, A, start, delta):
        # find the length of subsequence in A[start+1:] whose increment is delta
        cnt = 0
        factor = 1
        i = start + 1
        while i < len(A):
            temp = A[i] - A[start]
            if temp == delta:
                start = i
                # deal with duplicates, using a factor
                duplicate = 1
                while start+1 < len(A) and A[start+1]==A[start]:
                    duplicate += 1
                    start += 1
                factor *= duplicate
                
                cnt += factor
                i = start + 1
            elif temp < delta:
                i += 1
            elif temp > delta:
                break
        print("cnt: ", cnt)
        return cnt
    
