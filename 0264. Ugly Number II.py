# method 1: track the number in res that primes[i] needs to multiply 
# to generate a candidate
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5]
        idx = [0]*len(primes)
        
        res = [1]
        while n > 1:
            candidates = [res[idx[i]]*primes[i] for i in range(len(primes))]
            _min = min(candidates)
            res.append(_min)
            for i, candidate in enumerate(candidates):
                if candidate == _min:
                     idx[i] += 1
            n -= 1
        
        return res[-1]
    
