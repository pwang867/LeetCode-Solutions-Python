class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        # method 1:
        # ans = 0
        # while x !=0 or y != 0:
        #     ans += ((x%2)!=(y%2))
        #     x = x>>1
        #     y = y>>1
        # return ans
        
        # Method 2:
        return bin(x^y).count('1')
    
