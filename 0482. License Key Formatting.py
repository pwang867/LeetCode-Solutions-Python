# method 2: use a single while loop
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        res = []
        
        i = len(S) - 1
        cnt = 0
        while i >= 0:
            if cnt == K:
                res.append("-")
                cnt = 0
            if S[i] != "-":
                res.append(S[i].upper())
                cnt += 1
            i -= 1
        
        # easy to make mistake, fail on S = "5F3Z-2e-9-w", K = 4
        if res and res[-1] == "-":  
            res.pop()
        
        res.reverse()
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
    
