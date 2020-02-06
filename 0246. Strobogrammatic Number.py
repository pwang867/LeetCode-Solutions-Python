class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}  
        # 2:2 not strobogrammatic, do not forget 0:0
        if len(num) == 0:
            return True
        
        left, right= 0, len(num) - 1
        while left <= right:   # don't forget equal, edge case: "121"
            if num[left] not in d or num[right] not in d \
            or num[left] != d[num[right]]:
                return False
            left += 1
            right -= 1
        
        return True


"""
A strobogrammatic number is a number that looks the same when 
rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""
