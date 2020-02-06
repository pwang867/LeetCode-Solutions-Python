class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # check input
        if not strs or not strs[0]:
            return ""
        
        for i, c in enumerate(strs[0]):
            for j in range(1, len(strs)):
                word = strs[j]
                if i > len(word) - 1 or c != word[i]:
                    return strs[0][:i]   
        
        return strs[0] # don't have to use an extra variable to save res
        

"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

