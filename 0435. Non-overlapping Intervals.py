# method 1: time O(n*log(n) + n), space O(1)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        pre = intervals[0]
        num_erase = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= pre[-1]:
                pre = intervals[i]
            else:
                # when there is an overlap between pre and intervals[i]
                # one of the two intervals must be erased
                num_erase += 1
                if intervals[i][-1] < pre[-1]:  # greedy!!! only need to compare the tail
                    pre = intervals[i]
        return num_erase
    
