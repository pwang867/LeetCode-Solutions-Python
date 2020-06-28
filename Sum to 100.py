class Solution:
    def sum_to_hundred(self, s, target=100):
        if not s:
            return []
        res = []
        self.dfs(s, 0, 0, 100, [], res)
        return res

    def dfs(self, s, i, total, target, path, res):
        if i == len(s):
            if total == target:
                res.append("".join(path))
            return
        num = 0
        for j in range(i, len(s)):
            num = num*10 + int(s[j])
            if path:
                self.dfs(s, j+1, total+num, target, path+["+", str(num)], res)
            else:
                self.dfs(s, j+1, total + num, target, [str(num)], res)
            self.dfs(s, j+1, total-num, target, path+["-", str(num)], res)


if __name__ == "__main__":
    res = Solution().sum_to_hundred("123456789", 100)
    print(res)
    print(len(res))


"""
Add the mathematical operators + or - before any of the digits in the decimal numeric string 123456789
such that the resulting mathematical expression adds up to 100. Return all possible solutions.

There are 12 solutions:

1+2+3-4+5+6+78+9
1+2+34-5+67-8+9
1+23-4+5+6+78-9
1+23-4+56+7+8+9
12+3+4+5-6-7+89
12+3-4+5+67+8+9
12-3-4+5-6+7+89
123+4-5+67-89
123+45-67+8-9
123-4-5-6-7+8-9
123-45-67+89
-1+2-3+4+5+6+78+9

"""