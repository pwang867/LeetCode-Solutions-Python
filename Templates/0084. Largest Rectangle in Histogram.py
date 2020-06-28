# coding=utf-8

# method 3: maintain an ascending stack, O(n)


class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [] # maintains a strictly increasing height, saves index
        max_area = 0
        heights.append(0)  # add padding to help process the last height
        for i, height in enumerate(heights):
            # start to count areas before i (excluding i)
            while stack and height <= heights[stack[-1]]:   # mistake: height >= heights[stack[-1]]
                cur = stack.pop()
                # wrong: left = cur
                # wrong: left = cur if stack else 0
                left = stack[-1] + 1 if stack else 0  # tricky here !!!
                width = i-left  
                max_area = max(max_area, heights[cur]*width)
            
            stack.append(i)  # stack save index instead of height
        
        return max_area


# method 2: recursion, divide and conquer, O(n*log(n))
# worst case time O(n^2), space recursion depth O(n)
# Time limit exceeded on worst case: an increasing sequence


class Solution2(object):
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        # find the minimum heights
        min_index = 0
        for i in range(len(heights)):
            if heights[i] < heights[min_index]:
                min_index = i
        return max(len(heights)*heights[min_index], 
                  self.largestRectangleArea(heights[:min_index]),
                  self.largestRectangleArea(heights[min_index+1:]))


# method 1: brute force, iterate all possible rectangle
# O(n^2), Time limit exceeded

class Solution1(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):
            min_h = heights[i]
            for j in range(i, len(heights)):
                min_h = min(min_h, heights[j])  # 木桶原理 cask theory
                max_area = max(max_area, min_h*(j-i+1))
        
        return max_area


"""
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle 
in the histogram.

Above is a histogram where width of each bar is 1, 
given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, 
which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
