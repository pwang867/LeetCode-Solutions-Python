# build a dictionary {dist^2: set of points}, O(n^2)

from collections import defaultdict
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        points = map(tuple, points)
        for p in points:
            # build a dictionary {dist^2: set of points}, 
            # or (dist^2: num of points)
            d = defaultdict(int)
            for q in points:
                dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
                d[dist] += 1
            for dist, cnt in d.items():
                if cnt >= 2:
                    res += cnt*(cnt-1)   # mistake: cnt*(cnt-1)//2
        return res


"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
