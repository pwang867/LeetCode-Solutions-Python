# don't duplicate the work by counting i*j and j*i twice
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        
        isPrime = [True]*(n)
        isPrime[0] = 0
        isPrime[1] = 0
        
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
                for j in range(i*i, n, i):  # much better than range(i*2, n, i)
                # when i == 5, j == 2, the 5*2 is already taken care of when i == 2, j == 5 (2*5)
                    isPrime[j] = False
        
        return cnt
    
