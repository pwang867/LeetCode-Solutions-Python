# method 2, use bit mask
# time O(n^2*k), n=len(words), k=len(words[i])
class Solution2(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word2Mask(word):
            s = set(word)
            mask = 0
            for c in s:
                mask |= (1<<(ord(c)-ord('a')))
            return mask
        
        sets = [word2Mask(word) for word in words]
        res = 0
        for i in range(len(sets)-1):
            for j in range(i+1, len(sets)):
                if not sets[i]&sets[j]:
                    res = max(res, len(words[i])*len(words[j]))
        return res
    

# use set
# time O(n^2*k), n=len(words), k=len(words[i])
class Solution1(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = [set(word) for word in words]
        res = 0
        for i in range(len(sets)-1):
            for j in range(i+1, len(sets)):
                if not sets[i]&sets[j]:
                    res = max(res, len(words[i])*len(words[j]))
        return res




"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""
