# BFS
class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:  # return [] instead of [""] when digits==""
            return []
        
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
             "6":"mno", "7":"qprs", "8":"tuv", "9":"wxyz"}
        
        words = [""]  # mistake: words = []
        for digit in digits:
            words = [word + letter for word in words for letter in d[digit]]
        
        return words


# divide and conquer: cut digits into two slices: digits[0], digits[1:]
# time/space: O(3^len(digits))

class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # create a dict
        _dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", \
                 '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        return self.letterCombinationsHelper(digits, _dict)
        
    def letterCombinationsHelper(self, digits, _dict):
        if not digits:
            return []
        if len(digits) == 1:
            return list(_dict[digits])
        
        # use recursion for len(digits) >= 2
        first_list = list(_dict[digits[0]])
        others_list = self.letterCombinations(digits[1:])
        
        return [s1 + s2 for s1 in first_list for s2 in others_list]



"""

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, 
your answer could be in any order you want.

"""

