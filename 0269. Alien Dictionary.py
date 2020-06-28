# topological sort, but need to find the edges by ourselves
# time O(E+V)

# edge case:
# 1. words only has one word, words=["abc"],
# 2. don't forget the letters not compared, words=["abc", "abed"] (don't forget the 'd'):
# edge case: ["abc", "ab"]


import collections


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return []
        if len(words) == 1:
            return words[0]

        # find edges and build graph
        graph = collections.defaultdict(list)  # graph might not have all nodes
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                word1, word2 = words[i], words[j]
                n = min(len(word1), len(word2))
                for k in range(n):
                    if word1[k] != word2[k]:
                        graph[word1[k]].append(word2[k])
                        break
                else:
                    if len(word1) > len(word2):  # edge case: ["abc", "ab"]
                        return ''

        # topological sort
        indegrees = collections.defaultdict(int)  # have all nodes in edges
        for u, neis in graph.items():
            if u not in indegrees:
                indegrees[u] = 0
            for nei in neis:
                indegrees[nei] += 1

        queue = collections.deque([u for u, deg in indegrees.items() if deg == 0])
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        if len(res) != len(indegrees):  # cycle found
            return ""

        # some chars are not contributing to edges, such as ['xy', 'ab']
        chars = set()
        for word in words:
            chars |= set(word)
        for c in chars:
            if c not in indegrees:
                res.append(c)
        return "".join(res)


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
