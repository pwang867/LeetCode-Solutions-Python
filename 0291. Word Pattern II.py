class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_word = {}  # {pattern: word}
        word_p = {}
        return self.dfs(pattern, str, 0, 0, p_word, word_p)
    
    def dfs(self, pattern, s, i, j, p_word, word_p):
        if i == len(pattern):
            return j == len(s)
        if j == len(s):
            return False
        p = pattern[i]
        if p in p_word:
            pre_word = p_word[p]
            if s[j:j+len(pre_word)] == pre_word:
                if self.dfs(pattern, s, i+1, j+len(pre_word), p_word, word_p):
                    return True
        else:
            for endj in range(j, len(s)):
                word = s[j:endj+1]
                if word in word_p:
                    continue
                p_word[p] = word
                word_p[word] = p
                if self.dfs(pattern, s, i+1, endj+1, p_word, word_p):
                    return True
                del p_word[p]    # don't forget this backtracking step
                del word_p[word]
        return False


"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.
"""
