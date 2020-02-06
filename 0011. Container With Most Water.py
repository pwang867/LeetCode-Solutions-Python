# Note: the lines for the container are thickless
# time O(n), space O(1)

# we can actually prove it: assume the largest rectangular is formed by [ii, jj]
# when one of the two pointers left (or right) 
# arrive at the edge of the largest rectangular at index ii,
# it will stay there and wait for another pointer right (or left) because the height at 
# right's current position j must be smaller then ii, 
# otherwise the largest rectangular will be formed by [ii, j]
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            max_area = max(max_area, (right - left)*min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# brute force: try every combination, time O(n^2)


"""
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i 
is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

