# method 1 has best space O(result)
# all solutions has time O(n*log(n))


# https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation
# method 3: sort start and end time separately


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
    

# method 2: soret start and end time together
# space O(n), time O(n*log(n))


class Solution2(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        times = [ele for start, end in intervals for ele in [(start, 1), (end, -1)]]
        times.sort()
        max_room = 0
        cur_room = 0
        for time, change in times:
            cur_room += change
            max_room = max(max_room, cur_room)
        return max_room
    

# method 1, use heap to store end times, 
# whenever we need a room, we first go to heap to 
# check if there is any meeting room finished
# time O(n*log(n)), space O(result)
import heapq
class Solution1(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:  # reuse a meeting room
                heapq.heappushpop(heap, end)
            else:      # open a new meeting room
                heapq.heappush(heap, end)   
        return len(heap)
    

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
