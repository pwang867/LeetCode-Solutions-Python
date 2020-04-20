# ref: https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions
# dp[i][j][k] means the max points to remove boxes[i:j+1] when there are k boxes
# attached to the left of boxes[i] with the same color
# time O(n^4), space O(n^3)


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        if not boxes:
            return 0
        self.memo = {}
        return self.dp(boxes, 0, len(boxes) - 1, 0)

    def dp(self, boxes, i, j, k):
        if i > j:
            return 0
        if i == j:
            return (k + 1) ** 2
        while i < j and boxes[i + 1] == boxes[i]:  # optimization: merge same colors
            i += 1
            k += 1
        if (i, j, k) in self.memo:
            return self.memo[(i, j, k)]
        points = (k + 1) ** 2 + self.dp(boxes, i + 1, j, 0)  # boxes[i] is removed now
        # boxes[i] is removed later with boxes[m] where boxes[m] == boxes[i]
        for m in range(i + 1, j + 1):
            if boxes[m] == boxes[i]:
                points = max(points, self.dp(boxes, i + 1, m - 1, 0) \
                             + self.dp(boxes, m, j, k + 1))
        self.memo[(i, j, k)] = points
        return points


"""
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.
"""