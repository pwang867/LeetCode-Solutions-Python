
# time log(n), space O(1)
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1  # k is the number of digits
        while n > 9*10**(k-1)*k:
            n -= 9*10**(k-1)*k
            k += 1
        
        target = 10**(k-1) + n/k - 1   # the n-th digit is either in target or in target+1
        if n%k == 0:
            return target%10
        else:
            target += 1
            times = k - n%k + 1  # the digit counting backwards, wrong: times = k - n%k
            target = target/10**(times-1)
            return target%10
        


"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
