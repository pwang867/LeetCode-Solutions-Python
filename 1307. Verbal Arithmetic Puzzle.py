# method 2, O(2^(n-m)), n = number of characters, m = len(result)
# no leading zeros for an integer
class Solution(object):
    def isSolvable(self, words, result):
        if max(map(len, words)) not in [len(result), len(result)-1]:
            return False
        self.non_zeros = {word[0] for word in words if len(word) > 1}  # no leading zeros allowed
        words = [word[::-1] for word in words]
        result = result[::-1]
        return self.dfs(words, 0, 0, 0, result, set(range(10)), {})
    
    def dfs(self, words, i, j, carry, result, digits, d):
        if j == len(result):
            return carry == 0

        if i == len(words):
            if result[j] in d:
                if d[result[j]] != carry%10:
                    return False
                else:
                    return self.dfs(words, 0, j+1, carry//10, result, 
                             digits, d)
            else:
                if carry%10 not in digits:
                    return False
                d[result[j]] = carry%10
                digits.remove(carry%10)
                if self.dfs(words, 0, j+1, carry//10, result, 
                            digits, d):
                    return True
                del d[result[j]]
                digits.add(carry%10)
                return False
        if len(words[i]) <= j:
            return self.dfs(words, i+1, j, carry, result, digits, d)
        else:
            if words[i][j] in d:
                return self.dfs(words, i+1, j, carry+d[words[i][j]], 
                                result, digits, d)
            else:
                for digit in range(10):
                    if digit in digits:
                        if digit == 0 and words[i][j] in self.non_zeros:
                            # no leading '0' for a number
                            continue
                        d[words[i][j]] = digit
                        digits.remove(digit)
                        if self.dfs(words, i+1, j, carry+digit, 
                                    result, digits, d):
                            return True
                        digits.add(digit)
                        del d[words[i][j]]
                return False


# method 1, brute force, 2^n
import itertools
class Solution1(object):
    def isSolvable(self, words, result):
        if len(result) < max(map(len, words)):
            return False
        letters = set()
        for word in words + [result]:
            for c in word:
                letters.add(c)
        letters = list(letters)
        n = len(letters)
        relation = {letters[i]: i for i in range(len(letters))}
        for digits in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n):
            for i in range(len(letters)):
                relation[letters[i]] = digits[i]
            if self.check(words, result, relation):
                return True
        return False
    
    def check(self, words, result, relation):
        nums = []
        for word in words:
            if relation[word[0]] == 0 and len(word) > 0:
                return False
            nums.append(self.word2num(word, relation))
        if relation[result[0]] == 0 and len(result) > 0:
                return False
        return sum(nums) == self.word2num(result, relation)
    
    def word2num(self, word, relation):
        num = 0
        for c in word:
            num = num*10 + relation[c]
        return num


from time import time
t1 = time()
words = ["S","SEVEN","TWENT"]
result = "SEVES"
print(Solution().isSolvable(words, result))
print(time() - t1)


"""
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result). 
Return True if the equation is solvable otherwise return False.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true
Example 4:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10.
"""
