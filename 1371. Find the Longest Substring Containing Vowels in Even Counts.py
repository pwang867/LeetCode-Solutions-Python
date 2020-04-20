# we only need to check the count is even or odd for each vowel
# so we can use a bit mask to save the state
# time O(n), space O(n)


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state = 0
        pre = {0: -1}
        max_len = 0
        for i, c in enumerate(s):
            if c in idx:
                j = idx[c]  # index in state
                state = state ^ (1 << j)
            if state in pre:
                max_len = max(max_len, i - pre[state])
            else:
                pre[state] = i
        return max_len


"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
"""