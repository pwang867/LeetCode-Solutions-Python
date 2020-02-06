# we will shring [0, N) to [0, N - len(blacklist))
# the blacklist numbers within [0, N - len(blacklist)) 
# will be mapped to valid numbers to [N - len(blacklist), N)

import random
class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        m = len(blacklist)
        blackset = set(blacklist)
        # length of keys and nums will be the same
        nums = []   # nums to map for blacklist numbers within 0 - (self.N - m)
        for i in range(N-1, N-1-m, -1):
            if i not in blackset:
                nums.append(i)
        keys = [key for key in blacklist if key <= N-1-m]
        self.d = {keys[i]: nums[i] for i in range(len(nums))}
        self.N = N - m

    def pick(self):
        """
        :rtype: int
        """
        i = random.randrange(self.N)
        return self.d.get(i, i)



# method 2: binary search, divide [0, N) to m intervals, m = len(blacklist)
# ref: https://leetcode.com/problems/random-pick-with-blacklist/discuss/144441/Java-Binary-Search-Solution-O(BlogB)-for-constructor-and-O(logB)-for-pick()



# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
        
        
"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
