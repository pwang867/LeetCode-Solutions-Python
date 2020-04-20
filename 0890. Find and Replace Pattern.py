# optimal, all letters in words and pattern are only visited once only


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        norm_pattern = self.normalize(pattern)
        res = []
        for word in words:
            norm_word = self.normalize(word)
            if norm_word == norm_pattern:
                res.append(word)
        return res

    def normalize(self, word):  # change 'dkd' to 'aba'
        res = []
        usable = 'a'
        _dict = {}
        for i, c in enumerate(word):
            if c in _dict:
                res.append(_dict[c])
            else:
                res.append(usable)  # don't forget this line
                _dict[c] = usable
                usable = chr(ord(usable) + 1)
        return "".join(res)


"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x 
in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, 
and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""
