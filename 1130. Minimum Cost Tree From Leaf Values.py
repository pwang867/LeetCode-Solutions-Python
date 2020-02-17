
# method 3, optimized from method 2, stack
# maintain a decreasing stack, greedy, time/space O(n)
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        cost = 0
        stack = [float('inf')]
        for num in arr:
            while stack[-1] <= num:
                x = stack.pop()
                cost += x*min(num, stack[-1])
            stack.append(num)
        while len(stack) > 2:
            x = stack.pop()
            cost += x*stack[-1]
        return cost



# method 2: greedy, O(n^2)
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space
# greedy, time O(n^2)
class Solution2(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr or len(arr) == 1:
            return 0
        cost = 0
        while len(arr) > 1:
            x = min(arr)
            i = arr.index(x)
            y = arr[i-1] if i-1 >= 0 else float('inf')
            z = arr[i+1] if i+1 < len(arr) else float('inf')
            cost += x*min([y, z])
            arr.pop(i)
        return cost


# method 1, dp, time O(n^3), space O(n^2)
class Solution1(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        n = len(arr)
        self.maxNum = [[-float('inf')]*n for _ in range(n)]
        self.smallest = [[float('inf')]*n for _ in range(n)]
        return self.dfs(arr, 0, n-1)
    
    def dfs(self, arr, left, right):
        if self.smallest[left][right] != float('inf'):
            return self.smallest[left][right]
        if left == right:
            self.maxNum[left][right] = arr[left]
            self.smallest[left][right] = 0
            return 0
        else:
            for i in range(left, right):
                cur = self.dfs(arr, left, i) + self.dfs(arr, i+1, right)
                cur += self.maxNum[left][i]*self.maxNum[i+1][right]
                self.maxNum[left][right] = max(self.maxNum[left][i], self.maxNum[i+1][right])
                self.smallest[left][right] = min(self.smallest[left][right], cur)
            return self.smallest[left][right]


"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""
