class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []  # (char, cnts)
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        res = [c*cnt for c, cnt in stack]
        return "".join(res)
        
s = "pbbcggttciiippooaais"
k = 2
print(Solution().removeDuplicates(s, k))
