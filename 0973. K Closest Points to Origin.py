# method 2, quick selection, time O(n)


class Solution(object):
    def kClosest(self, points, K):
        if not points or K >= len(points):
            return points
        if K <= 0:
            return []
        left, right = 0, len(points) - 1
        while left < right:  # use a while loop instead of recursion
            mid = self.partition(points, left, right)
            if mid == K:
                break
            elif mid > K:
                right = mid - 1
            else:
                left = mid + 1
        return points[:K]

    def partition(self, points, left, right):
        if left > right:
            raise ValueError("required: left <= right")
        i, j = left, right - 1
        pivot = self.dist(points[right])
        while i <= j:
            if self.dist(points[i]) <= pivot:
                i += 1
            elif self.dist(points[j]) > pivot:
                j -= 1
            else:
                points[i], points[j] = points[j], points[i]
                i += 1
                j -= 1
        points[i], points[right] = points[right], points[i]
        return i

    @staticmethod
    def dist(point):
        return point[0] ** 2 + point[1] ** 2


print(Solution.dist([1,1]))


# method 1, k*log(n)


import heapq


class Solution1(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        arr = [(point[0]**2+point[1]**2, i) for i, point in enumerate(points)]
        top = heapq.nsmallest(K, arr)
        return [points[i] for d, i in top]


'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''
