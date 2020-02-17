"""
reference: https://leetcode.com/problems/count-the-repetitions/discuss/95429/Python-69ms-solution

Find the cycle inside the matching pattern
three regions: prefix region + cycling region + tail region
"""


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # delete extra letters in s1 that are not in s2
        s1 = "".join([c for c in s1 if c in s2])  
        
        s1_round, s2_round = 0, 0  # number of rounds that has been checked
        i, j = 0, 0  # the iteration index of s1 and s2
        d = {}  # {s2 index j: (s1_round, s2_round)}
        
        while s1_round < n1:
            if j == len(s2):
                s2_round += 1
                j = 0
            elif i == len(s1):
                s1_round += 1
                i = 0
                if j not in d:
                    d[j] = (s1_round, s2_round)
                else:
                    # period detected
                    pre_s1_round, pre_s2_round = d[j]
                    s1_period = s1_round - pre_s1_round
                    s2_period = s2_round - pre_s2_round
                    # cycling region
                    repeating_s2_rounds = (n1 - pre_s1_round)//s1_period*s2_period
                    # prefix and tail regions
                    remaining_s1_rounds =  (n1 - pre_s1_round)%s1_period \
                                            + pre_s1_round
                    for key, val in d.items():
                        if val[0] == remaining_s1_rounds:
                            remaining_s2_rounds = val[1]
                            break
                    total_s2_rounds = repeating_s2_rounds + remaining_s2_rounds
                    return total_s2_rounds//n2
            elif s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return s2_round//n2  # no period detected
    
    
"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""
