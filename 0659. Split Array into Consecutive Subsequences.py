# dp, space/time O(n)
# dp = {nums[i]: [list of lengths of subsequences ending with nums[i]]}
# in dp[nums[i]], lengths that are larger than 3 
# are all put before lengths smaller than 3

# dp[num] only depends on dp[num-1]
from collections import defaultdict, deque
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = defaultdict(deque)  # dp will have at most two keys
        
        for num in nums:
            if num-2 in dp:   # early termination and save space
                if dp[num-2][-1] < 3:
                    return False
                else:
                    del dp[num-2]
            if num - 1 not in dp:
                dp[num].append(1)
            else:
                length = dp[num - 1].pop()
                if len(dp[num - 1]) == 0:
                    del dp[num - 1]
                if length + 1 >= 3:  
                    # to make sure all small numbers (<3) are on the right of d[num]
                    dp[num].appendleft(length + 1)
                else:
                    dp[num].append(length + 1)

        # check lengths of all subsequences
        for num in dp:
            for length in dp[num]:
                if length < 3:
                    return False
        return True



"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
 

Constraints:

1 <= nums.length <= 10000
"""
    