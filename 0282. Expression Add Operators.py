# coding=utf-8


# method 2, same as method 1, but do not use backtrack to simplify the code


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        path = []
        self.dfs(num, 0, 0, 0, target, path, res)
        return res

    def dfs(self, num, i, total, pre, target, path, res):
        if i == len(num):
            if total + pre == target:
                res.append("".join(path))
            return
        cur = 0
        for j in range(i, len(num)):
            cur = cur * 10 + int(num[j])
            if not path:
                self.dfs(num, j+1, total + pre, cur, target, [str(cur)], res)
            else:
                self.dfs(num, j+1, total+pre, cur, target, path+["+", str(cur)], res)
                self.dfs(num, j+1, total+pre, -cur, target, path+["-", str(cur)], res)
                self.dfs(num, j+1, total, pre*cur, target, path+["*", str(cur)], res)
            if cur == 0:
                break


# method 1, simply use brute force DFS, backtrack


class Solution1(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        path = []
        ans = []
        self.addOperatorsHelper(num, target, 0, 0, 0, 0, path, ans)
        return ans
    
    def addOperatorsHelper(self, s, target, i, pre, cur, cum, path, ans):
        # cum is the cumulative value in path (including pre, but not cur)
        # i is the current index to be processed
        # pre is the previous number
        # cur is the current number (might not finished yet)
        # path is like ["+", "2", "*", "34"]
        
        if i == len(s):
            if cum == target:
                ans.append("".join(path[1:]))  # path always start with "+"
            return
        cur = cur*10 + int(s[i])
        
        # when number formation is not done, don't process it yet, and avoid creating invalid number "05"
        if cur > 0 and i+1 < len(s):
            self.addOperatorsHelper(s, target, i+1, pre, cur, cum, path, ans)
        
        # add
        path.append("+")
        path.append(str(cur))
        self.addOperatorsHelper(s, target, i+1, cur, 0, cum+cur, path, ans)
        path.pop()
        path.pop()
        
        if not path:  # subtract and multiply requires a previous operand
            return
        
        # subtract
        path.append("-")
        path.append(str(cur))
        self.addOperatorsHelper(s, target, i+1, -cur, 0, cum-cur, path, ans)
        path.pop()
        path.pop()
        
        # multiply, 悔棋一步
        path.append("*")
        path.append(str(cur))
        self.addOperatorsHelper(s, target, i+1, pre*cur, 0, cum-pre+pre*cur, path, ans)
        path.pop()
        path.pop()
        

"""
Given a string that contains only digits 0-9 and a target value, 
return all possibilities to add binary operators (not unary) +, -, 
or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""
