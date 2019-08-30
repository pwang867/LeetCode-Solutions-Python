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


# method 1: use a heap
# time O(n*k*log(n)), space > O(n)
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
        pre = 0
        
        while n > 0:
            _min = heapq.heappop(heap)
            if _min == pre:  # easy to miss !! deal with duplicates
                continue
            pre = _min
            n -= 1
            
            for prime in primes:
                heapq.heappush(heap, _min*prime)
            
        
        return pre
    
