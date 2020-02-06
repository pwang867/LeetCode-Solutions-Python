# sliding window, remove duplicate codes in method 1, time/space O(n)
# ref: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/234482/JavaC%2B%2BPython-Sliding-Window
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or len(A) < K:
            return 0
        longest = self.helper(A, K)
        shortest = self.helper(A, K-1)
        cnt = 0
        for i in range(len(A)):
            cnt += shortest[i] - longest[i]
        return cnt
    
    def helper(self, A, K):
        # find the longest subarrays ending in index i
        # A[longest[i]:i+1] is the longest subarray ending in i 
        # that has K kinds of integers
        longest = [-1]*len(A)
        d = {}
        left = 0
        for right, c in enumerate(A):
            d[c] = d.get(c, 0) + 1
            while len(d) > K:
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    del d[A[left]]
                left += 1
            longest[right] = left
        return longest
    

# sliding window, time/space O(n)
# find the longest and shortest subarrays ending in index i, and add the differences
class Solution1(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or len(A) < K:
            return 0
        
        # find the longest subarrays ending in index i
        # A[longest[i]:i+1] is the longest subarray ending in i 
        # that has K kinds of integers
        longest = [-1]*len(A)
        d = {}
        left = 0
        for right, c in enumerate(A):
            d[c] = d.get(c, 0) + 1
            while len(d) > K:
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    del d[A[left]]
                left += 1
            if len(d) == K:
                longest[right] = left
        # find the shortest subarrays ending in index i
        shortest = [-1]*len(A)
        d = {}
        left = 0
        for right, c in enumerate(A):
            d[c] = d.get(c, 0) + 1
            while len(d) > K or (len(d) == K and d[A[left]] > 1):
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    del d[A[left]]
                left += 1
            if len(d) == K:
                shortest[right] = left
        # get results
        cnt = 0
        for i in range(len(A)):
            if shortest[i] != -1:
                cnt += shortest[i] - longest[i] + 1
        return cnt


"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
Accepted
"""
