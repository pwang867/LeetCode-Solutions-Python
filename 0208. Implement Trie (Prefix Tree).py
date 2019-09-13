# method 2: simply use a dictionary of dictionaries
# to construct the Trie
# simpler and faster than method 1

class Trie1(object):

    def __init__(self):
        self.root = {}
        

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = "#"
        

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "#" in cur
        

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True



# method 1: use an extra class TrieNode 
# to help implement the Trie
class TrieNode(object):
    
    def __init__(self):
        self.is_word = False
        self.children = {}  # {letter: TrieNode}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
        

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    
