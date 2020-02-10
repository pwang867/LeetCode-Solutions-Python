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
                    dp[i][d] += dp[j][d] + 1  # +1 means the sequence (A[j], A[i]), easy to forget
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
    
"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
 
A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.

 
Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""
