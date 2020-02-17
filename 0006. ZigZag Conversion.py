# space/time O(n), be careful with index
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        period = 2*numRows - 2
        res = []
        n = len(s)
        for i in range(numRows): # for each row
            for j in range(i, n, period):  # j is index in the string s
                res.append(s[j])
                if i != 0 and i != numRows-1 and j + period - 2*i < n:  
                    # ignore the top and bottom row, check index out of range
                    res.append(s[j + period - 2*i])
        
        return ''.join(res)


"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed font 
for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""
