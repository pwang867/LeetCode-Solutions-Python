# dp, space/time O(n)
# dp = {nums[i]: [list of lengths of subsequences ending in nums[i]]}
# in dp[nums[i]], lengths that are larger than 3 
# are all before lengths smaller than 3

# dp[num] only depends on dp[num-1]
from collections import defaultdict, deque
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = defaultdict(deque)
        
        for num in nums:
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
    