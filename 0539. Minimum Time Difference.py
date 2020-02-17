# method 1, change to a circular array of integer minutes
# time/space O(n)
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = [self.time2num(timePoint) for timePoint in timePoints]
        minutes.sort()     # treat minutes as a circular array
        minutes.append(minutes[0] + 24*60)
        min_diff = float('inf')
        for i in range(len(minutes)-1):
            diff = minutes[i+1]-minutes[i]
            min_diff = min(min_diff, diff)
        return min_diff
    
    def time2num(self, time):
        if not time:
            return 0
        hour, minute = time.split(":")
        return int(hour)*60 + int(minute)



"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
