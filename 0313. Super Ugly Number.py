# n-th ugly number


# method 2: keep tracking the last time prime numbers are used
# time O(n*k), space O(n+k)
# method 2 and method 1 are basicly the same idea, 
# but method 2 uses res and idx instead of a heap to save time and space

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        if n < 1 or not primes:
            return -1
        
        res = [1]
        idx = [0]*len(primes)
        # res[idx[i]] is the latest factor to be considered by primes[i] to
        # produce a candidate primes[i]*idx[i]
        
        while n > 1:
            candidates = []
            for i in range(len(primes)):
                candidates.append(primes[i]*res[idx[i]])
            _min = min(candidates)
            res.append(_min)
            for i in range(len(candidates)):
                if candidates[i] == _min:
                    idx[i] += 1
            n -= 1
            
        return res[-1]


# Solution 1: use a heap
# time O(n*k*log(n))
import heapq

class Solution1(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n < 1:
            return 0
        
        heap = [1]
        visited = set([1])
        while n > 0:
            _min = heapq.heappop(heap)
            n -= 1
            for prime in primes:
                if  _min*prime not in visited:
                    heapq.heappush(heap, _min*prime)
                    visited.add(_min*prime)   # easy to miss !! deal with duplicates
        return _min
    


"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
