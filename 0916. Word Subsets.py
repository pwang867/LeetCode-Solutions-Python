# use dictionary to save a letter and its highest frequency

from collections import Counter
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        # merge all words in B into a big superset
        allB = {}  # it saves all the letters in B and their highest frequency
        for word in B:
            t = Counter(word)  # {letter: frequency}
            self.merge(allB, t)
        
        res = []
        for word in A:
            t = Counter(word)
            if self.compare(t, allB):
                res.append(word)
        
        return res
        
    
    def merge(self, all_d, d):
        # if the key in d doesn't exist in all_d, add it into all_d
        # otherwise, update the value of the key to the larger one
        for key, val in d.items():
            if key not in all_d:
                all_d[key] = val
            else:
                all_d[key] = max(all_d[key], d[key])
    
    def compare(self, d1, d2):
        for key, val in d2.items():
            if key not in d1 or d1[key] < d2[key]:
                return False
        return True

    
"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
