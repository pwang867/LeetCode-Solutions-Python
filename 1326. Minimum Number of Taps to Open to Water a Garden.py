# time O(n*log(n)), space O(n)
# sort, greedy
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append([i-r, i+r])
        intervals.sort(key = lambda x: [x[0], -x[1]])
        res = []
        
        for interval in intervals:
            start, end = interval
            if not res:
                res.append(interval)
                continue
            if start > res[-1][1]:
                return -1
            if end <= res[-1][1]:
                continue
            if start <= 0:   # easy to miss the left boundary
                res = []
            while len(res) >= 2:
                if res[-2][1] >= start:
                    res.pop()
                else:
                    break
            res.append(interval)
        
        while len(res) >= 2:
            if res[-2][1] >= n:
                res.pop()
            else:
                break
        if res[-1][1] < n:
            return -1
        return len(res)


# ref: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484394/Python-Greedy-with-stack-(O-NlogN)-Super-easy-to-understand
# time O(n*log(n)), space O(n), greedy
# similar to 55. jump game, and # 1024 video stitching
class Solution1(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        intervals = [[i-r, i+r] for i, r in enumerate(ranges)]
        intervals.sort()
        res = 0
        watered = 0
        i = 0
        while i < len(intervals):
            ends = []
            while i < len(intervals) and intervals[i][0] <= watered:
                ends.append(intervals[i][1])
                i += 1
            if not ends:
                return -1
            end = max(ends)
            if end > watered:
                watered = end
                res += 1
            if watered >= n:
                return res
        return res
    

"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
"""
