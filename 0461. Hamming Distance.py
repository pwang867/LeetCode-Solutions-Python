# Method 2: bit or
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """          
        return bin(x^y).count('1')  # or use x=x&(x-1) to remove the last "1" in x


# method 1: check bit one by one
class Solution1(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x !=0 or y != 0:
            ans += ((x%2)!=(y%2))
            x = x>>1
            y = y>>1
        return ans
        
    
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
