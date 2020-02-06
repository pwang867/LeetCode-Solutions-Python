# count sort, time O(n), space O(n)
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
        
        
"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
