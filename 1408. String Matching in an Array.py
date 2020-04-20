# method 2, suffix array using trie
# sort words from long to short, for each word, search in the trie, and insert all of its suffix into the trie
# time/space O(n*m^2)
import collections


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return True


class Solution2(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        words.sort(key=len, reverse=True)
        res = []
        for word in words:
            if trie.search(word):
                res.append(word)
            for i in range(len(word)):
                trie.insert(word[i:])
        return res


# method 1, brute force, O(n^2*m), n = len(words), m = len(words[0])


class Solution1(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        res = []
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].



Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""