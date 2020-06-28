# method 1: presums, time/space O(n)


class Solution1(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        pre_sums = {0: 1}
        cur_sum = 0
        cnt = 0
        for a in A:
            cur_sum += a
            cnt += pre_sums.get(cur_sum - S, 0)
            pre_sums[cur_sum] = pre_sums.get(cur_sum, 0) + 1
        return cnt


# method 1: sliding window, atmost(S) - atmost(S-1), time O(n), space O(1)


"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
