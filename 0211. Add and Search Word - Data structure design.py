# method 2, same as method 1, use Trie, but use BFS for search


import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:                               # mistake: for c in node:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot
        character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = [self.root]
        for c in word:
            new_nodes = []
            for node in nodes:
                if c != ".":
                    if c in node.children:
                        new_nodes.append(node.children[c])
                else:
                    new_nodes.extend(node.children.values())
            nodes = new_nodes
        for node in nodes:
            if node.isWord:
                return True
        return False


# method 1, use dfs for search


class WordDictionary1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if not word:
            return node.is_word
        c, word = word[0], word[1:]
        if c != ".":
            if c in node.children:
                return self.dfs(word, node.children[c])
            else:
                return False
        else:
            for c in node.children:
                if self.dfs(word, node.children[c]):
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)