# time/space O(m*n), k = len(common)


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1:
            return str2
        if not str2:
            return str1
        common = self.longest_common_subsequence(str1, str2)
        i, j, k = 0, 0, 0
        res = []
        while k < len(common):
            if str1[i] != common[k]:
                res.append(str1[i])
                i += 1
            elif str2[j] != common[k]:
                res.append(str2[j])
                j += 1
            else:
                res.append(common[k])
                i += 1
                j += 1
                k += 1
        res.append(str1[i:])
        res.append(str2[j:])
        return ''.join(res)

    def longest_common_subsequence(self, str1, str2):   # time/space O(m*n)
        # dp[i][j] saves the route, saving space
        m, n = len(str1), len(str2)
        dp = [[-1 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 0
                else:
                    if len(dp[i][j - 1]) >= len(dp[i - 1][j]):
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
        i, j = m, n
        res = []
        while i > 0 and j > 0:
            if dp[i][j] == 0:
                res.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i][j] == 1:
                i -= 1
            elif dp[i][j] == 2:
                j -= 1
        return "".join(res)

    def longest_common_subsequence2(self, str1, str2):   # time/space O(m*n*k), k = len(common)
        # dp[i][j] saves the subsequence, wasting space
        m, n = len(str1), len(str2)
        dp = [["" for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i][j - 1]) >= len(dp[i - 1][j]):
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)



Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.


Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""