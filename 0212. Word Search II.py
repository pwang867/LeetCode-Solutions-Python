# use Trie to solve this problem
# time < O(m*n*len(words)*word_length)
# space < O(len(words)*word_length) for Trie

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, "", trie.root, res)
        
        return res
                    
    
    def dfs(self, board, i, j, path, node, res):
        # board[i][j] is not included in path yet
        # node is the node of the last letter in path
        
        if node.is_word:
            res.append(path)
            node.is_word = False  # important !! delete the found word from dictionary
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
            or board[i][j] not in node.children:
            return
        
        cur = board[i][j]
        board[i][j] = "#"
        for v in [(-1,0), (1,0), (0,-1), (0,1)]:
            p, q = i+v[0], j+v[1]
            self.dfs(board, p, q, path+cur, node.children[cur], res)
        board[i][j] = cur
        
        

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}
        
        
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
        
