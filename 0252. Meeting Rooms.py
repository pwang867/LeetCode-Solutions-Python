# method 2, sort by starting time, and check interval intersection
# O(n*log(n))
class Solution2(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

# method 1, brute force O(n*n), TLE
class Solution(object):
    def canAttendMeetings(self, intervals):
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] > intervals[j][0] and intervals[j][1] > intervals[i][0]:
                    return False
        return True


"""
Given an array of meeting time intervals consisting of start and end times
 [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend 
 all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""
