# presum
# time O(n*log(n)), space O(n)
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        costs = [self.getCost(s[i], t[i]) for i in range(len(s))]
        sums = [0]*(len(costs)+1)
        
        total = 0
        for i in range(1, len(sums)):
            total += costs[i-1]
            sums[i] = total
        
        res = 0
        for i in range(1, len(sums)):
            j = self.binarySearch(sums, i, sums[i-1]+maxCost)
            if j != -1:
                res = max(res, j-i+1)
        return res
    
    def getCost(self, a, b):
        return abs(ord(a) - ord(b))
    
    def binarySearch(self, sums, start, target):
        # find the index of the last number <= target
        left, right = start, len(sums)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if sums[mid] <= target:
                left = mid
            else:
                right = mid
        if sums[right] <= target:
            return right
        elif sums[left] <= target:
            return left
        else:
            return -1


if __name__ == "__main__":
    s = ""
    t = ""
    maxCost = 0
    print(Solution().equalSubstring(s, t, maxCost))


"""
You are given two strings s and t of the same length. 
You want to change s to t. Changing the i-th character of s 
to i-th character of t costs |s[i] - t[i]| that is, 
the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the 
same as the corresponding substring of twith a cost less than or equal to 
maxCost.

If there is no substring from s that can be changed to its corresponding 
substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the 
maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, 
so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.
 

Constraints:

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s and t only contain lower case English letters.
"""
