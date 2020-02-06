# use math: only the outer four points appear only once, 
# all other points appear in even times
# edge case: [[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]]

# time O(N), space O(N)
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # find the position of the possible final rectangle
        A, B, C, D = float('inf'), float('inf'), -float('inf'), -float('inf')
        areas = 0
        s = set()
        for a, b, c, d in rectangles:
            A = min(A, a)
            B = min(B, b)
            C = max(C, c)
            D = max(D, d)
            areas += (c-a)*(d-b)
            for point in [(a,b),(c,d),(c,b),(a,d)]:
                if point in s:
                    s.remove(point)
                else:
                    s.add(point)
            
        # requirement 1: the area of the final rectangle 
        # must be the sum of all small rectangles
        if areas != (C-A)*(D-B):
            return False
        # requirement 2: no overlapping between any two rectangles
        return s == {(A, B), (A, D), (C, B), (C, D)}  # wrong: return len(s) == 4



"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
"""
