"""
Inspired from https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/441547/Upper-bound-proof-(intuition-from-segment-tree)

i. The maximum number of points is 1000*1000 (given in question)
ii. The maximum number of ships is 10 (given in question)

If we do a quartered search, the number of levels in the tree will be maximum of log(1000*1000)/log 4 which is 10 (from i.)
At each node , we will divide the node into 4 child nodes and call the hasShips method for each child node. We only add the child node to the next level if there is a ship in that child node.
The next level can only have 10 or less nodes (from ii.) (So each level can have a maximum of 10 nodes and for each node we need to call the hasShips 4 times i.e 40 times for each level.
The maximum number of levels is 10 . So the maximum number of calls to hasShips is 400
"""

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y


# binary search


class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        i, j = topRight.x, topRight.y
        p, q = bottomLeft.x, bottomLeft.y
        if i < p or j < q:
            return 0
        has_ship = sea.hasShips(topRight, bottomLeft)
        if not has_ship:
            return 0
        if i == p and j == q:
            return 1
        m, n = (i+p)//2, (j+q)//2   # mid point
        return self.countShips(sea, topRight, Point(m+1, n+1))\
                + self.countShips(sea, Point(m, n), bottomLeft)\
                + self.countShips(sea, Point(m, j), Point(p, n+1)) \
                + self.countShips(sea, Point(i, n), Point(m+1, q))
        




"""
(This problem is an interactive problem.)

On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example :



Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 

Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000
"""
