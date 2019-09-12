# binary search on result, 
# because citations are sorted
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
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
        
