# https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation
# method 2: sort start and end time separately
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts = [interval[0] for interval in intervals]
        ends   = [interval[1] for interval in intervals]
        starts.sort()   # don't forget to sort
        ends.sort()
        max_room = 0
        cur_room = 0
        i, j = 0, 0
        while i < len(starts) and j < len(ends):
            if ends[j] <= starts[i]:
                cur_room -= 1
                j += 1
            else:
                cur_room += 1
                i += 1
            max_room = max(max_room, cur_room)
        return max_room
    

# method 1: soret start and end time together
class Solution1(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        times = [time for interval in intervals for time in [(interval[1], -1), (interval[0], 1)]]
        times.sort()
        
        cnt = 0
        max_rooms = 0
        for time, change in times:
            cnt += change
            max_rooms = max(max_rooms, cnt)  # don't forget this step
        return max_rooms


"""
Given an array of meeting time intervals consisting of 
start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
"""
