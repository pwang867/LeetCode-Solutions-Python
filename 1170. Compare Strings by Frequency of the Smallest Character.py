# O((m+n)*log(m)), m=len(words), n = len(queries)
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        queries = self.words2freq(queries)
        words = self.words2freq(words)
        words.sort()
        res = []
        for query in queries:
            res.append(self.search(words, query))
        return res
    
    def search(self, words, target):
        """ find the count of words[i] > target """
        left, right = 0, len(words)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if words[mid] > target:
                right = mid
            else:
                left = mid
        if words[left] > target:
            return len(words) - left
        elif words[right] > target:
            return len(words) - right
        else:
            return 0
    
    def words2freq(self, words):
        if not words:
            return []
        res = []
        for word in words:
            res.append(self.f(word))
        return res
    
    def f(self, word):
        """ this function find the frequency of the smallest character """
        if not word:
            return 0
        d = {}
        for c in word:
            d[c] = d.get(c, 0) + 1
        N = ord("a")
        for i in range(26):
            c = chr(i + N)
            if c in d:
                return d[c]


"""
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
"""
