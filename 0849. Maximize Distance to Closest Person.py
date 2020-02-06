# time O(n), space O(1)
# tip: use index -1 and n to represent the boundaries to make things easier
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        pre = -1  # the id of the previous seat that has person
        max_dist = 0
        for i, num in enumerate(seats):
            if num == 1:
                if pre == -1:
                    dist = i
                else:
                    dist = (i-pre)//2
                max_dist = max(max_dist, dist)
                pre = i
                
                if len(seats)-1-i <= max_dist:  # early termination, much faster
                    return max_dist
        
        return max(max_dist, len(seats)-1-pre)  # don't miss the rightmost seat
    
    