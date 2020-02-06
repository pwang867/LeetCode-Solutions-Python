# easy to understand, but hard to implement and be bug free


# ref: https://leetcode.com/problems/rotated-digits/discuss/116530/O(logN)-Time-O(1)-Space
# ref: http://www.frankmadrid.com/ALudicFallacy/2018/02/28/rotated-digits-leet-code-788/
# time/space O(log(N))
# iterate digit by digit from left to right
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = map(int, list(str(N)))
        same = {0, 1, 8}
        good = [0, 1, 2, 5, 6, 8, 9]
        good_set = set(good)
        res = 0
        path = set()
        for i, digit in enumerate(digits):
            for j in good:
                if j >= digit:
                    break
                res += 7**(len(digits)-1-i)
                if path.issubset(same) and j in same:
                    res -= 3**(len(digits)-1-i)
            if digit not in good_set:  # mistake: if digit is not in good_set
                return res
            path.add(digit)  # mistake: path.append(digit)
        if not path.issubset(same):
            res += 1
        return res
    


"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""

