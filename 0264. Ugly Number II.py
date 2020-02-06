# method 1: track the number in res that primes[i] needs to multiply 
# to generate a candidate
# time O(n)
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
    


# method 2: use a heap
# time O(n*log(n))



"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""
