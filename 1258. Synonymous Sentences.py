# method 2, use union find to find groups to find neighbors

from collections import defaultdict

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        
        # group words using union find
        parent = {}
        size = {}
        def find(u):
            if u not in parent:
                parent[u] = u
                size[u] = 1
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size [q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            return False
        for u, v in synonyms:
            union(u, v)
        map(find, parent)
        groups = defaultdict(list)
        for u, v in parent.items():
            groups[v].append(u)
        for u, arr in groups.items():
            arr.sort()
        
        # dfs 
        words = text.split()
        res = []
        def dfs(words, i, path):
            if i == len(words):
                res.append(" ".join(path))
                return
            neighbors = groups[parent[words[i]]] if words[i] in parent else [words[i]]
            for nei in neighbors:
                path.append(nei)
                dfs(words, i+1, path)
                path.pop()
        dfs(words, 0, [])
        return res



# method 1, BFS
from collections import deque, defaultdict
class Solution1(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        graph = defaultdict(set)
        for u, v in synonyms:
            graph[u].add(v)
            graph[v].add(u)
            
        queue = deque([text])
        visited = {text}
        res = []
        while queue:
            sentence = queue.popleft()
            res.append(sentence)
            words = sentence.split()
            for i, word in enumerate(words):
                if word in graph:
                    for nei in graph[word]:
                        new_words = words[:i] + [nei] + words[i+1:]
                        new_sentence = " ".join(new_words)
                        if new_sentence not in visited:
                            visited.add(new_sentence)
                            queue.append(new_sentence)
        return sorted(res)


"""
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 

Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
​​​​​​​"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[0] != synonyms[1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.
"""
