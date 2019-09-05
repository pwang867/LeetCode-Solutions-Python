# time complexity: n*log(log(n)), space O(n)
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity
# don't duplicate the work by calculting i*j and j*i

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
        for i in range(2, int(n**0.5)+1):  # we only need to check to sqrt(n)
            if isPrime[i]:
                cnt += 1
                for j in range(i*i, n, i):  # much better than range(i*2, n, i)
                    isPrime[j] = False
        
        return cnt + sum(isPrime[int(n**0.5)+1:])
    
    
