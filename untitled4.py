import itertools
class Solution(object):
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


