class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        total = sum([a for a in A if a%2==0])
        
        for query in queries:
            val, i = query
            if A[i]%2 == 0 and val%2 == 0:  # mistake: i%2 == 0
                total += val
            elif A[i]%2 == 0 and val%2 != 0:
                total -= A[i]
            elif A[i]%2 != 0 and val%2 != 0:
                total += A[i] + val
            res.append(total)
            A[i] += val
        
        return res
    
