# time O(n) due to insertion, otherwise binary search should be considered

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        end = 0  # intervals[:end] is before newInterval and has no overlap
        start = len(intervals)  # intervals[start:] is after newInterval and has no overlap
        
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[-1] < newInterval[0]:
                end = i + 1
            elif curr[0] > newInterval[-1]:
                start = i
                break
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[-1] = max(newInterval[-1], curr[-1])
        
        return intervals[:end] + [newInterval] + intervals[start:]



"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""