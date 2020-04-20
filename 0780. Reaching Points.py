# traveling backwards is easier, because there is only one route allowed backwards
# moving forward has two routes
# forward approach (DFS+memo): time/space O(tx*ty)
# backward approach: time O(log(tx*ty)), space O(1)
# similar to GCD


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx >= ty:
                if ((tx - sx) // ty) == 0:
                    break
                tx -= ((tx - sx) // ty) * ty
            else:
                if ((ty - sy) // tx) == 0:
                    break
                ty -= ((ty - sy) // tx) * tx
        return tx == sx and ty == sy


"""
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].
Accepted
"""
