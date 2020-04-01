# group strings by length, and then process from short to long
# time O(n*m), m = len(words[i]), n = len(words)
import collections
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        groups = collections.defaultdict(list)   # group words by length
        for word in words:
            _len = len(word)
            groups[_len].append(word)
        chain_len = {}   # chain: max_len words
        for _len in range(max(groups.keys())+1):
            if _len in groups:
                cur_words = groups[_len]
                for word in cur_words:
                    chain_len[word] = 1
                    for i in range(len(word)):
                        pre = word[:i] + word[i+1:]
                        if pre in chain_len:
                            chain_len[word] = max(chain_len[word], chain_len[pre] + 1)
        return max(chain_len.values())


"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
"""
