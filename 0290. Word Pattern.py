# iterate through the list and return False when pattern has mismatch
# need to check pattern_to_word and word_to_pattern
# time/space O(n)
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Create a hashtable(dictionary) to store all "pattern-word" pairs
        words = str.split()
        if len(pattern) != len(words):
            return False
        
        p_word = {}  # stores {pattern: str}
        word_p = {} # {word: pattern}, a set is actually enough
        for i in range(len(pattern)):  
            p = pattern[i]
            word = words[i]
            if p in p_word:
                if p_word[p] != word:  # if pattern same, word different
                    return False
            else:
                if word in word_p:     # if pattern different, word same
                    return False
                else:
                    p_word[p] = word
                    word_p[word] = p
        return True

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
