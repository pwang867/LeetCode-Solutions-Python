# Time: O(len(strs)*m*n)
# dynamic programming
# dp[i][j] means the max number of traversed strings 
# that could be constructed using i '0' and j '1'
# for every str, update dp backwards so that we don't overwrite values to be used

# similar to: #322 coin change

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # add 1 to m and n to make index simple
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        # add every str one by one to update dp
        for s in strs:
            cnt0 = s.count('0')  # counts of '0' in s
            cnt1 = len(s) - cnt0
            # update every dp element
            # dp in range i < cnt0 and j < cnt1 smaller than current str, ignored
            for i in range(m, cnt0 - 1, -1):  
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        
        return dp[-1][-1]
    

"""
In the computer world, use restricted resource you have to generate 
maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. 
On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can
 form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s 
and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""
