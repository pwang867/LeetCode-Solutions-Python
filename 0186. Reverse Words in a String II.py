# time O(n), in place O(1)
class Solution(object):
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)  # reverse the whole list first
        
        # then reverse each reversed word
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(s, start, i - 1)
                start = i + 1
        
        # do not forget the last word !!
        self.reverse(s, start, len(s) - 1)
    
    def reverse(self, s, start, end):
        # reverse list s
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    

"""
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""
