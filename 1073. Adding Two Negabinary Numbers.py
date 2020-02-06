# ref: https://leetcode.com/problems/adding-two-negabinary-numbers/discuss/303831/ChineseC%2B%2B-1073.
# when carry==-1, -(-2)**k = (-2)**k + (-2)**(k+1), so carry==-1 become (1, 1)

# carry can be -1, 0, 1
# -(-2)**k = (-2)**k + (-2)**(k+1)

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1)-1, len(arr2)-1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry != 0:   # wrong: carry > 0
            cur = carry
            if i >= 0:
                cur += arr1[i]
                i -= 1  # don't forget !!!
            if j >= 0:
                cur += arr2[j]
                j -= 1
            if cur == -1:
                res.append(1)
                carry = 1
            elif cur >= 2:
                res.append(cur%2)
                carry = -1
            else:
                res.append(cur)
                carry = 0
        while res and res[-1]==0:
            res.pop()
        res.reverse()
        return res or [0]



"""
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
 

Note:

1 <= arr1.length <= 1000
1 <= arr2.length <= 1000
arr1 and arr2 have no leading zeros
arr1[i] is 0 or 1
arr2[i] is 0 or 1
"""
