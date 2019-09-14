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
    
