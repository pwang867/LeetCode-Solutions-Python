# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.done = False   # this extra variable is needed because None might be an element in self.iterator
        self.next_num = None
        self._get_next_num()
    
    def _get_next_num(self):
        if self.iterator.hasNext():
            self.next_num = self.iterator.next()
        else:
            self.done = True
    
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.done:
            return None
        else:
            return self.next_num

    def next(self):
        """
        :rtype: int
        """
        if not self.done:
            res = self.next_num
            self._get_next_num()
            return res
        else:
            return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.done
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

