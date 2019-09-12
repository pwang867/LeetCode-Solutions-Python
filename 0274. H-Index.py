class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        counts = [0]*(n+1)  # counts[i] is the counts of paper with citation == i
        for citation in citations:
            if citation > n:
                citation = n
            counts[citation] += 1
            
        total = 0  # total is the papers with citations >= i
        for i in range(n, -1, -1):
            total += counts[i]
            if total >= i:
                return i
        
        
