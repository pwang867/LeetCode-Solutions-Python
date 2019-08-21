# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 08:50:18 2019

@author: WEIMIN ZHOU
"""
# method2: tricky method, there are totally 2**n new abbreviations
# use the binary representation
class Solution(object):
    def generateAbbreviation(self, word):
        all_abbr = []
        n = len(word)
        for m in range(2**n):
            i = m
            abbr = []
            cnt = 0  # counts of "1" bits
            for j in range(n):
                bit = i%2
                i = i // 2
                if bit == 0:
                    if cnt > 0:
                        abbr.append(str(cnt))
                        cnt = 0  # reset cnt, do not forget
                    abbr.append(word[j])
                else:
                    cnt += 1
            if cnt > 0:  # do not forget
                abbr.append(str(cnt))
                cnt = 0
            all_abbr.append("".join(abbr))
        return all_abbr
        


# method 1: recursion
class Solution1(object):
    def generateAbbreviation(self, word):
        res = []  # list of string
        path = []  # list of char
        self.dfs(word, 0, res, path)
        return res
    
    def dfs(self, word, i, res, path):
        if i == len(word):
            res.append("".join(path))
            return  # do not forget
        
        # no abbreviation
        path.append(word[i])
        self.dfs(word, i+1, res, path)
        path.pop()
        
        # use abbreviation
        if path and path[-1].isdigit():
            path[-1] = str(int(path[-1]) + 1)
            self.dfs(word, i+1, res, path)
        else:
            path.append("1")
            self.dfs(word, i+1, res, path)
            path.pop()

if __name__ == "__main__":
    print(Solution().generateAbbreviation("Happy"))
    
