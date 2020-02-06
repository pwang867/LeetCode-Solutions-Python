# sliding window, time O(n), space O(1)

from collections import Counter
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counts = Counter(s)
        d = {}
        for c in "QWER":
            if c in s_counts and s_counts[c] > len(s)//4:
                d[c] = s_counts[c] - len(s)//4
        
        # find the minimum length of the sliding window containing d
        if not d:
            return 0
        cnt = len(d.values())
        res = float('inf')
        left, right = 0, 0
        for right, c in enumerate(s):
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    cnt -= 1
            while cnt == 0:
                if s[left] not in d:
                    left += 1
                else:
                    if d[s[left]] < 0:
                        d[s[left]] += 1
                        left += 1
                    else:
                        break
            if cnt == 0:
                res = min(res, right-left+1)
        return res

s = "WQRWWERW"
print(Solution().balancedString(s))
