# topological sort, but need to find the edges by ourselves
# time O(E+V)

# edge case: 1. words only has one word, words=["abc"], 
# 2. don't forget the letters not compared, words=["abc", "abed"] (don't forget the 'd')
from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words: return ""
        if len(words) == 1: return words[0]    # edge case
        edges = self.getEdges(words)
        in_degrees = self.getInDegrees(edges)
        # standard topological sort
        queue = deque(u for u, v in in_degrees.items() if v==0)
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in edges[u]:
                if v == u:
                    continue
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)
        if len(res) != len(in_degrees):
            return ""
        else:
            return "".join(res)
    
    def getEdges(self, words):
        edges = defaultdict(set)
        for i in range(len(words)-1):
            word1 = words[i]  # edge case: word1 = "abc", word2 = "abcde
            word2 = words[i+1]
            for j in range(len(word1)):
                edges[word1[j]].add(word2[j])
                if word1[j] != word2[j]:  # mistake: if word1[j] < word2[j]:
                    break   # easy to forget
            for c in word1[j+1:]:    # don't forget to include the letters not compared yet
                if c not in edges:
                    edges[c].add(c)
            for c in word2[j+1:]:
                if c not in edges:
                    edges[c].add(c)
        return edges
    
    def getInDegrees(self, edges):
        in_degrees = defaultdict(int)
        for u in edges:
            in_degrees[u] += 0   # to make sure in_degrees has all the nodes as the key
            for v in edges[u]:
                if v == u:
                    continue
                in_degrees[v] += 1
        return in_degrees


"""
There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
