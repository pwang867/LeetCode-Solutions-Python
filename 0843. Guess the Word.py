# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# method 2: always choose the word with the most evenly distributed neighbors
# the probability of two words with 0 common words is 80%, so we need to minimize
# the uneven distribution. There are six conditions: 0-5 common words.
# if we want to make things simple, we can simply choose the word 
# with fewest neighbors which has 0 common letters with the word
class Solution(object):
    def findSecretWord(self, wordlist, master):
        N = 6
        candidates = wordlist[:]
        while candidates:
            dists = self.getDist(candidates)
            i = self.getCandidate(dists, candidates)  # get the index
            candidate = candidates[i]
            num = master.guess(candidate)
            if num == N:
                return
            candidates = [candidates[j] for j, _dist in enumerate(dists[i]) 
                          if j != i and _dist == num]
    
    def getDist(self, candidates):
        # return a 2D matrix mat, with dist[i][j] meaning 
        # the num of common words between candidates[i] and candidates[j]
        n = len(candidates)
        dists = [[6]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                cnt = 0
                wordi, wordj = candidates[i], candidates[j]
                for k in range(len(wordi)):
                    if wordi[k] == wordj[k]:
                        cnt += 1
                dists[i][j] = cnt
                dists[j][i] = cnt
        return dists
    
    def getCandidate(self, dists, candidates):
        # find the candidate with the most evenly distributed dist
        score = float('inf')
        res = 0
        for i, row in enumerate(dists):
            cnts = [0]*6
            for j, cnt in enumerate(row):
                if j != i:
                    cnts[cnt] += 1
            avg = sum(cnts)/6.0
            temp = sum([abs(x-avg) for x in cnts])
            if temp < score:
                score = temp
                res = i
        return res
        

# method 1: brute force, take one word from the end and then filter candidates
class Solution1(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        # wordlist can not be modifed due to share with master
        N = 6
        candidates = wordlist + []
        while candidates:
            word = candidates.pop()  # choose word in a smarter way?
            num = master.guess(word)
            if num == N:
                return
            candidates = [next_word for next_word in candidates
                        if self.possible(word, next_word, num)]
            print(word, candidates, num)
        
    def possible(self, word, next_word, num):
        # check if the count of common letters 
        # between word and next_word is num
        cnt = 0
        for i in range(len(word)):
            if word[i] == next_word[i]:
                cnt += 1
                if cnt > num:
                    return False
                
        return cnt == num


        
"""
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, 
and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  
The guessed word should have type string and must be from the original 
list with 6 lowercase letters.

This function returns an integer type, representing the number of 
exact matches (value and position) of your guess to the secret word.  
Also, if your guess is not in the given wordlist, 
it will return -1 instead.

For each test case, you have 10 guesses to guess the word. 
At the end of any number of calls, if you have made 10 or less calls 
to master.guess and at least one of these guesses was the secret, 
you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, 
each with 100 words in the word list.  The letters of each word in those 
testcases were chosen independently at random from 'a' to 'z', 
such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, 
so we pass the test case.
"""
