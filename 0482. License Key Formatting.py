# method 3, solution with most clear logic, O(n)
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "")
        if not S:
            return ""
        S = S.upper()
        m = len(S) % K
        if m != 0:
            res = [S[:m], "-"]
        else:
            res = []
        for i in range(m, len(S), K):
            res.append(S[i:i+K])
            res.append("-")
        res.pop()
        return "".join(res)
    

# method 2: use a single while loop
# loop from behind because the first block might be be length K
# remove extra "-" in the front if any
from collections import deque
class Solution2(object):
    def licenseKeyFormatting(self, S, K):
        res = deque([])
        
        i = len(S) - 1
        cnt = 0
        while i >= 0:
            if cnt == K:
                res.appendleft("-")
                cnt = 0
            if S[i] != "-":
                res.appendleft(S[i].upper())
                cnt += 1
            i -= 1
        
        # easy to make mistake, fail on S = "5F3Z-2e-9-w", K = 4
        if res and res[0] == "-":  
            res.popleft()
        
        return "".join(res)
            

# method 1: two slow due to too many function calls of self.getLastNChar
class Solution1(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        end = len(S) - 1
        while end >= 0:
            block, end = self.getLastNChar(S, end, K)
            res.extend(block)
            if block:
                res.append("-")
        res.reverse()
        return "".join(res[1:])
    
    def getLastNChar(self, s, end, k):
        if k == 0:
            return [], len(s) - 1
        
        res = []
        for i in range(end, -1, -1):
            c = s[i]
            if c != "-":
                res.append(c.upper())
                k -= 1
            if k == 0:
                end = i - 1
                return res, end
        return res, -1
    
"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
"""
