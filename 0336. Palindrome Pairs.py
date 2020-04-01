# based on method 2, but make it simpler
# time O(n*k^2)


class Solution3(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wordDict = {word: i for i, word in enumerate(words)}
        pairs = []
        for i, word in enumerate(words):
            rword = word[::-1]
            if rword in wordDict and rword != word:   # easy to miss: and rword != word
                pairs.append([i, wordDict[rword]])
            for _len in range(1, len(word)+1):
                left_part = rword[:len(word)-_len]   # search target string to add to the left of current word
                if self.isPal(word, 0, _len-1) and left_part in wordDict:
                    pairs.append([wordDict[left_part], i])
                right_part = rword[_len:]
                if self.isPal(word, len(word)-_len, len(word)-1) and right_part in wordDict:
                    pairs.append([i, wordDict[right_part]])
        return pairs
    
    def isPal(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
 # method 2, use dictionary
# for every word, produce all the possible candidates from word, 
# do not have to go through all the words, and only
# check all the candidates that are no longer than word
# note: the pair can either be on the left or on the right
# time O(n*k*k), where k is the length of the word, and n is number of words
   

# method 2 and method 3 are the same, while method 3 made things simple
class Solution2(object):
    def palindromePairs(self, words):
        # input requirement: words are all unique
        
        word_dict = {words[i]:i for i in range(len(words))}
        # lengths can help reduce the number of candidates, but not necessary
        lengths = list(set(len(word) for word in words))  
        lengths.sort()
        
        res = []
        for i, word in enumerate(words):
            # each word only looks for a pair whose length is no more than word
            rword = word[::-1]  # mistake: word.reverse(), python str has no .reverse()
            if rword in word_dict and rword != word: 
                # when candidate length is equal to word
                # word is on the left, because rword can also find word
                res.append([i, word_dict[rword]])
            for length in lengths:  # candidate length is less than word
                if length == len(word):
                    break
                # word is on the left
                if self.isPalindrome(rword[:len(word)-length]) \
                        and rword[len(word)-length:] in word_dict:
                    res.append([i, word_dict[rword[len(word)-length:]]])
                # word is on the right
                if self.isPalindrome(rword[length:]) \
                        and rword[:length] in word_dict:
                    res.append([word_dict[rword[:length]], i])
        
        return res
    
    def isPalindrome(self, word):
        # or simply use return word == word[::-1]
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                return False
        return True


# method 1: brute force, combine every pair, and then if it is a palindrome
# time O(n^2*k), space O(1)

class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                s = words[i]+words[j]
                if self.isPalindrome(s):
                    res.append([i,j])
        
        return res
    
    def isPalindrome(self, s):
        if not s:
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
    

"""
Given a list of unique words, find all pairs of distinct indices (i, j) 
in the given list, so that the concatenation of the two words, i.e. 
words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""
