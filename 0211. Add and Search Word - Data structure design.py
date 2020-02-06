# use Trie

class TrieNode:
    def __init__(self):
        self.children = {}
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
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
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
        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)