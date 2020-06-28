# method 2: simulate the process, time/space O(n)


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack


# method 1: break the popped into blocks (only works when pushed is ascending)
# 1. break the popped [4,5,3,2,1] into [[4], [5, 3, 2, 1]],
# 2. reverse each block, arr = [[4], [1, 2, 3, 5]]
# 3. process backwards, arr[-1] should be able to be placed to the right of arr[-2] or to the left,
#    or arr[-1] could be broken into two parts to put on both sides of arr[-2]

# we can use popped to simulate a stack, process data backwards


"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been 
the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""