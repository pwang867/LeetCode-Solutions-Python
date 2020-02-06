class Solution(object):
    def isSolvable(self, words, result):
        if max(map(len, words)) not in [len(result), len(result)-1]:
            return False
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
                        d[words[i][j]] = digit
                        digits.remove(digit)
                        if self.dfs(words, i+1, j, carry+digit, 
                                    result, digits, d):
                            return True
                        digits.add(digit)
                        del d[words[i][j]]
                return False
        
        
words = ["SEND","MORE"]
result = "MONEY"
print(Solution().isSolvable(words, result))

