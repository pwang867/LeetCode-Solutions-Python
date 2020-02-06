# binary search on result, 
# because citations are sorted
# time O(log(n))

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # don't forget, otherwise index our of bound
        if not citations: 
            return 0
        
        n = len(citations)
        left, right = 0, n-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if citations[mid] == n-mid:
                return n-mid
            elif citations[mid] > n-mid:
                right = mid
            else:
                left = mid
        
        if citations[left] >= n-left:
            return n-left
        elif citations[right] >= n-right:
            return n-right
        else:
            return 0
        
"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""
