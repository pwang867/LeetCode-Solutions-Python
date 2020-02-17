# method 2: use Math
"""
Note the four buttons as (a, b, c, d)
we can easily see a*b = c, a*c = b, b*c = a
so we can only have 8 operations: (None, a, b, c, d, a*d, b*d, c*d)
where None means no operation, or means the original state
when n < 3, (a, b, c, d) might become each other, 
so we need to consider separately

(none) -> (a, b, c, d) -> (none, a, b, c, ad, bd, cd)  -> (none, a, b, c, d, ad, bd, cd) -> repeating
"""

class Solution(object):
    def flipLights(self, n, m):
        if n == 0 or m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if n > 2:
            if m == 1:
                return 4
            elif m == 2:
                return 7  # easy to miss !!   # no d for m==2
            else:
                return 8


# method 1: brute force, use bit operations to simulate the buttons
# there is definitely no more than 2^n states, so there must be a period/cycle
# we can use a set to save the previous states to help find the cycle
class Solution1(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        pass
        

"""
There is a room with n lights which are turned on initially and 4 
buttons on the wall. After performing exactly m unknown operations 
towards buttons, you need to return how many different kinds of 
status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], 
function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
 

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]
 

Example 2:

Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]
 

Example 3:

Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], 
[off, off, off], [off, on, on].
"""

