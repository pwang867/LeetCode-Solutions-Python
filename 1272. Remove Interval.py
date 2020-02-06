# method 2, binary search, time O(log(n)), space O(result)
class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        if toBeRemoved[0] >= intervals[-1][-1] \
        or toBeRemoved[1] <= intervals[0][0]:
            return intervals
        
        left = self.search(intervals, toBeRemoved[0])
        right = self.search(intervals, toBeRemoved[1])
        result = []
        if left >= 0:
            result = intervals[:left]
            if toBeRemoved[0] >= intervals[left][-1]:
                result.append(intervals[left])
            elif intervals[left][0] != toBeRemoved[0]:
                result.append([intervals[left][0], toBeRemoved[0]])
        if toBeRemoved[1] < intervals[right][-1]:
            result.append([toBeRemoved[1], intervals[right][-1]])
        result += intervals[right+1:]
        return result
    
    def search(self, intervals, target):
        # find the last interval that interval[0] <= target
        left, right = 0, len(intervals)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if intervals[mid][0] >= target:
                right = mid
            else:
                left = mid
        if target >= intervals[right][0]:
            return right
        elif target >= intervals[left][0]:
            return left
        else:
            return -1



# method 1, line sweep, time/space O(result)


"""
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
"""
