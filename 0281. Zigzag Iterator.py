
# use queue to help iterate, better than using list
from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arrs = deque(deque(x) for x in [v1, v2])
        self.k = len(self.arrs)
    
    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        v = self.arrs.popleft()
        res = v.popleft()
        if v:
            self.arrs.append(v)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.arrs and not self.arrs[0]:   # remove empty list, edge case: v1=[], v2=[]
            self.arrs.popleft()
        return len(self.arrs) > 0



# use list, not time efficient
class ZigzagIterator1(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arrs = [v1, v2]
        self.index = [0]*len(self.arrs)
        self.k = 2
        self.arr_id = 0
    
    def update_arr_id(self):
        self.arr_id = (self.arr_id + 1)%self.k

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            res = self.arrs[self.arr_id][self.index[self.arr_id]]
            self.index[self.arr_id] += 1
            self.update_arr_id()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        for _ in range(self.k):
            if self.index[self.arr_id] == len(self.arrs[self.arr_id]):
                self.update_arr_id()
            else:
                return True
        return False



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""
