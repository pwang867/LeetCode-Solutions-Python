# method 1: simply use a dictionary of dictionaries
# to construct the Trie

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
