# method 2: use a res array to store all results
# multiply digit by digit and store it into corresponding location in res 
# time O(m*n)

class Solution(object):
    def multiply(self, num1, num2):
        
        m, n = len(num1), len(num2)
        res = [0]*(m+n+1)
        for i in range(-1, -m-1, -1):
            for j in range(-1, -n-1, -1):
                k = i + j + 1
                res[k] += int(num1[i])*int(num2[j])
                # res[k-1] += res[k]//10
                # res[k] %= 10
        
        for k in range(m+n, 0, -1):  # deal with carry
            res[k-1] += res[k]/10
            res[k] %= 10
        
        # remove leading zeros
        k = 0
        while k < len(res)-1 and res[k] == 0:  # mistake: k < len(res), edge case: [0]
            k += 1
        
        return "".join([str(x) for i, x in enumerate(res) if i >= k])
                

# method 1: divide the problems into number string times a single digit
# and then add all those strings together
# time O((m+n)*min(m,n)), m = len(num1), n = len(num2)
import collections
class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return ""
        ans = ""
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for digit in num1:
            temp = self.single_mul(digit, num2)
            ans = self.add(ans + "0", temp)     
        return ans
        
    
    def single_mul(self, digit, num):
        """
        digit: a single digit string
        num: a str of number of any length
        """
        if digit == "0":
            return "0"
        if digit == "1":
            return num
        
        digit = ord(digit) - ord("0")
        carry = 0
        ans = collections.deque()
        for i in range(-1, -len(num) - 1, -1):
            curr = (ord(num[i]) - ord("0"))*digit + carry
            ans.appendleft(str(curr%10))
            carry = curr/10
        if carry > 0:
            ans.appendleft(str(carry))
        
        return "".join(ans)
    
    
    def add(self, num1, num2):
        """
        num1: any length string
        num2: any length string
        return: str, sum of num1 + num2
        """
        i, j = len(num1)-1, len(num2)-1
        res = collections.deque()
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            cur = carry
            if i >= 0:
                cur += int(num1[i])
            if j >= 0:
                cur += int(num2[j])
            res.appendleft(str(cur%10))
            
            i, j, carry = i-1, j-1, cur//10
            
        return "".join(res)
            

  
"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library 
or convert the inputs to integer directly.
"""

