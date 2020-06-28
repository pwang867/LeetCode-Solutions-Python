# we need one unused character in str2
# we need at least one node, whose in_degree > out_degree
# time O(n), space O(26)

# the only case that we can not do it is when we have a circle of 26 circles
# str1[i] -> str2[i] is an edge, we only have 26 chars, so we only have at most 26 edges


class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:   # edge case
            return True

        # one node can only have 1 out degree
        d = {}  # save edges, at most 26 edges
        for i in range(len(str1)):
            if str1[i] not in d:
                d[str1[i]] = str2[i]
            else:
                if d[str1[i]] != str2[i]:
                    return False

        # check if it is a circle
        return len(set(d.values())) < 26


"""
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 
by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
"""
