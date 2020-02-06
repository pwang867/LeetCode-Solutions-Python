# method 2: trie solution
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/371876/Detailed-Explanation-using-Trie-O(word_length-%2B-100*puzzle_length)
# to implement

# method 1, bit mask
# change all words to bit numbers, time O(2^(len(puzzles[0]))*len(puzzles) + len(words)*len(words[0]))
# we only need to record different characters in word
from collections import defaultdict
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        wordsBit = defaultdict(int)
        for word in words:
            wordset = set(list(word))
            if len(wordset) > 7:
                continue
            else:
                wordsBit[self.word2Num(wordset)] += 1
        puzzlesBit = [self.word2Num(set(list(puzzle))) for puzzle in puzzles]
        
        res = [0]*len(puzzles)
        for i, puzzle in enumerate(puzzles):
            first = 1<<(ord(puzzle[0])-ord("a"))
            puzzleBit = puzzlesBit[i]
            cur = puzzleBit    # cur is the substring of puzzleBit, at most 2**7 substrings because len(puzzle) <= 7
            count = 0
            while cur > 0:
                if (first | cur) == cur:
                    count += wordsBit[cur]
                cur = (cur-1)&puzzleBit   # get next substring of puzzleBit
            res[i] = count
        return res
    
    def word2Num(self, wordset):
        num = 0
        for c in wordset:
            num |= 1<<(ord(c)-ord("a"))
        return num


"""
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 

Example :

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
 

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
Accepted
"""
