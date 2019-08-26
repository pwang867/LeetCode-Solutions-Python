# method2, by equation, gray code: G(n) = n^(n>>1)
# ref: https://en.wikipedia.org/wiki/Gray_code
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(2**n):
            res.append(i^(i>>1))
        
        return res

# method 1: by mirror reflection
class Solution1(object):
    def grayCode(self, n):
        res = [0]
        
        for i in range(n):
            _len = len(res)
            for j in range(_len-1, -1, -1):
                # "+" has precedence over "<<"
                res.append(res[j] + (1<<i))  # mistake: res[j] + 1<<i
        
        return res
    
