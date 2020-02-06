# edge case: "00000010100101000001111010011100", 
# the leading zeros still need to be taken into account!

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):   # wrong: while n > 0:
            digit = n&1
            res = (res<<1) + digit
            n = n>>1
        return res


"""
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 
represents the unsigned integer 43261596, so return 964176192 which its 
binary representation is 00111001011110000010100101000000.


Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 
represents the unsigned integer 4294967293, so return 3221225471 which 
its binary representation is 10101111110010110010011101101001.
"""
