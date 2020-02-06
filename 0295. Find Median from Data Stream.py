# save the data stream in two containers, 
# a min heap and a max heap, and max heap saves -num
# time for addNum() is O(log(n)), time for findMedian() is O(1)
# space used is the heaps, which is O(n)
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # len(self.max_heap) - len(self.min_heap) is 0 or 1
        self.max_heap = []  # stores -num, smaller half of data stream
        self.min_heap = []
        

    def addNum(self, num): 
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == len(self.min_heap):
            if not self.min_heap or num <= self.min_heap[0]:  
                # mistake: don't forget not self.min_heap
                heapq.heappush(self.max_heap, -num)
            else:
                temp = heapq.heappushpop(self.min_heap, num)
                heapq.heappush(self.max_heap, -temp)
        else:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                temp = heapq.heappushpop(self.max_heap, -num)
                heapq.heappush(self.min_heap, -temp)
                

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return 1.0*(-self.max_heap[0] + self.min_heap[0])/2
        else:
            return -self.max_heap[0]
    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
