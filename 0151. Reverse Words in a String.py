# method 2: reverse the whole string, then reverse each word, like pancake flip
# method 2, time/space O(n)
# can write a helper function called flip(str_list, left, right)



# method 1, use built-in functions directly
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        s_list.reverse()
        return " ".join(s_list)




"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces 
between two words to a single space in the reversed string.
"""
    