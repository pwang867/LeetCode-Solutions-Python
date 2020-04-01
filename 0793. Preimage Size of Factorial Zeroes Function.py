# edge case: when K=104, output is 0
# binary search, (log(num))^2


class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        x = self.search(K)
        # if self.f(x) != K:  # unnecesary, y will be equal to x in this case
        #     return 0
        y = self.search(K+1)
        return y - x
    
    def search(self, K):
        # search the first num such that f(num) >= K
        num = 1
        while self.f(num) < K:
            num *= 2
        left, right = num//2, num
        while left + 1 < right:
            mid = left + (right-left)//2
            num_zeros = self.f(mid)
            if num_zeros >= K:
                right = mid
            else:
                left = mid
        if self.f(left) >= K:
            return left
        else:
            return right
    
    def f(self, num):
        if num < 5:
            return 0
        cnt = 0
        divisor = 5
        while num >= divisor:
            cnt += num//divisor
            divisor *= 5
        return cnt


"""
Let f(x) be the number of zeroes at the end of x!. 
(Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, 
while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. 
Given K, find how many non-negative integers x have the 
property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].
"""
