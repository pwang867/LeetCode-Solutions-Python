class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
    
    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.intervals or self.intervals[-1][-1] + 1 < val:
            self.intervals.append([val, val])
        elif self.intervals[-1][0] <= val:
            self.intervals[-1][-1] = max(self.intervals[-1][-1], val)
        elif val < self.intervals[0][0] - 1:
            self.intervals.insert(0, [val, val])
        elif val <= self.intervals[0][1]:
            self.intervals[0][0] = min(self.intervals[0][0], val)
        else:
            i = self.binarySearch(val)
            if self.intervals[i-1][-1] + 1 == val and self.intervals[i][0] - 1 == val:
                self.intervals = self.intervals[:i-1] + \
                         [[self.intervals[i-1][0], self.intervals[i][-1]]] + self.intervals[i+1:]
                # mistake: don't forget extra brackets: [[self.intervals[i-1][0], self.intervals[i][-1]]]
            elif self.intervals[i][0] - 1 == val:
                self.intervals[i][0] = val
            elif self.intervals[i-1][-1] + 1 == val:
                self.intervals[i-1][-1] = val
            elif self.intervals[i-1][-1] < val < self.intervals[i][0]:
                self.intervals.insert(i, [val, val])
    
    def binarySearch(self, val):
        left, right = 0, len(self.intervals)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if self.intervals[mid][0] > val:
                right = mid
            else:
                left = mid
        return right

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
"""
