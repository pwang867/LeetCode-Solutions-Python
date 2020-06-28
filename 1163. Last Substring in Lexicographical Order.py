''' 
https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation
'''


# we are searching the max suffix
# time O(n), space O(n), space can be optimized to O(1) with some tricky pointers
# same as method 1, but modulized


class Solution2(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        ids = list(range(len(s)))
        step = 0
        ids = self.filter_max(s, ids, step)
        while len(ids) > 1:
            step += 1
            ids = self.filter_max(s, ids, step)
            ids = self.swallow(ids, step)
        return s[ids[0]:]

    def filter_max(self, s, ids, step):
        # only keep i in ids that s[i+step] is max
        max_char = max([s[i + step] for i in ids if i + step < len(s)])
        ids = [i for i in ids if i + step < len(s) and s[i + step] == max_char]
        return ids

    def swallow(self, ids, step):
        if not ids:
            return []
        res = [ids[0]]
        for i in range(1, len(ids)):
            if ids[i - 1] + step < ids[i]:
                res.append(ids[i])
        return res


# method 1


class Solution1(object):
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
                if i-1 >= 0 and ids[i-1] + size == j:   # optimization
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
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""
