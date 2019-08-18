# Solution 2: use stack to maintain an increasing sequence
# time O(n), space O(n)
class Solution2(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        res_len = len(num)-k
        for i, digit in enumerate(num):
            while stack and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            if digit=="0" and not stack:  # don't put "0" in the beginning
                res_len -= 1
                continue
            stack.append(digit)
        
        res = stack[:res_len]
        
        if not res:
            return "0"
        else:
            return "".join(res)

# Solution 1: recursion, time O(k*n), recursion depth max O(n-k)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = self.removeKdigitsHelper(num, k)
        res = res.lstrip("0")  # deal with leading zeros, such as "0200"
        return res if res else "0"
    
    def removeKdigitsHelper(self, num, k):
        if k == 0:
            return num
        if k >= len(num):
            return ""  # not return "0"
        
        pos = self.getSmallestDigit(num[:k+1])
        # next row: num[pos+1:] not nums[pos], (k-pos) not (k-pos+1)
        return num[pos] + self.removeKdigitsHelper(num[pos+1:], k-pos)  
    
    def getSmallestDigit(self, num):
        # num is a number string
        res = 0  # index
        for i in range(1, len(num)):
            if num[i] < num[res]:
                res = i
        return res
    
    
