''' 
https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation
'''

# time O(nlog(n)), space O(n)
class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        size = 0
        ids = list(range(len(s)))
        while len(ids) > 1:
            largest = max([s[i+size] for i in ids if i + size < len(s)])
            next_ids = []
            for i, j in enumerate(ids):
                if j + size >= len(s):
                    continue
                if i-1 >= 0 and ids[i-1] + size == j:
                    continue
                if s[j+size] == largest:
                    next_ids.append(j)
            ids = next_ids
            size += 1
        return s[ids[0]:]


"""
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""
