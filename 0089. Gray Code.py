# method2, by equation, gray code: G(n) = n^(n>>1)
# ref: https://en.wikipedia.org/wiki/Gray_code
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(2**n):
            res.append(i^(i>>1))
        
        return res

# method 1: by mirror reflection
class Solution1(object):
    def grayCode(self, n):
        res = [0]
        
        for i in range(n):
            _len = len(res)
            for j in range(_len-1, -1, -1):
                # "+" has precedence over "<<"
                res.append(res[j] + (1<<i))  # mistake: res[j] + 1<<i
        
        return res
    

"""

The gray code is a binary numeral system where two successive values 
differ in only one bit.

Given a non-negative integer n representing the total number of bits 
in the code, print the sequence of gray code. 
A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: 
We define the gray code sequence to begin with 0.
A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
Therefore, for n = 0 the gray code sequence is [0].

"""

