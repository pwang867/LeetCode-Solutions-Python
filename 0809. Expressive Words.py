# time O(k*n*m), k=len(S), n=len(words), m=len(words[i])
# edge case: S = "lll", word = "llll"


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S:
            return 0
        d = self.count(S)
        cnt = 0
        for word in words:
            d1 = self.count(word)
            if self.isStretchy(d, d1):
                cnt += 1
        return cnt
    
    def count(self, word):
        if not word:
            return []
        d = [[word[0], 0]]   # mistake: d = [(word[0], 0)], tuple can not be modified!
        for c in word:
            if c == d[-1][0]:
                d[-1][1] += 1
            else:
                d.append([c, 1])
        return d
    
    def isStretchy(self, d, d1):
        if len(d) != len(d1):
            return False
        for i in range(len(d)):
            if d[i][0] != d1[i][0]:
                return False
            if not (d[i][1] == d1[i][1] or (d[i][1] > d1[i][1] and d[i][1] >= 3)):  
                # easy to be forget: d[i][1] > d1[i][1]
                return False
        return True


"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of 
applications of the following extension operation: choose a group consisting of characters c, and add 
some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get 
"helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" 
to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension 
operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""
