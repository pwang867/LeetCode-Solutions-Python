# time O(n^3), space O(n) (can be optimized to O(1))


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) < 3:
            return False
        n = len(num)
        for i in range(n // 2):
            for j in range(i + 1, (n * 2) // 3):
                if self.is_valid(num, i, j):
                    return True
        return False

    def is_valid(self, num, i, j):
        # i, j are end index of first and second numbers respectively
        if i + 1 > 1 and num[0] == "0":  # "01" is an invalid number, can be moved into isAdditiveNumnber() to save time
            return False
        if j - i > 1 and num[i + 1] == "0":
            return False
        pre = int(num[:i + 1])
        cur = int(num[i + 1:j + 1])
        k = j + 1
        while k < len(num):
            tmp = str(pre + cur)
            if num[k:k + len(tmp)] == tmp:
                k += len(tmp)
            else:
                return False
            pre, cur = cur, pre + cur
        return True


"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""