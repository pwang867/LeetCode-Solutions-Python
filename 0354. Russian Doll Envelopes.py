# binary search, time O(n*log(n)), space O(n)
# sort by ascending width and then descending height
# this makes dealing with envelopes with equal width much easier!
# then use a stack to maintain an increasing height, 
# same idea as longest increasing sequence
from bisect import bisect_left
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:[x[0], -x[1]])
        heights = [x[1] for x in envelopes]  # only need to consider heights
        
        stack = []  # to save an increasing sequence of height
        for height in heights:
            i = bisect_left(stack, height)
            if i == len(stack):
                stack.append(height)
            else:
                stack[i] = height
        
        return len(stack)
    
