class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        right_remove = 0
        left_remove = 0
        left_total = 0
        right_total = 0
        for c in s:
            if c == "(":
                left_total += 1
                left_remove += 1
            elif c == ")":
                right_total += 1
                if left_remove == 0:
                    right_remove += 1
                else:
                    left_remove -= 1
        res = set()
        path = []
        self.dfs(s, 0, res, path, left_total - left_remove, 
                 right_total - right_remove, left_remove, right_remove)
        return list(res)
    
    
    def dfs(self, s, i, res, path, leftcnt, rightcnt, left_remove, right_remove):
        """
        leftcnt: number of left parentheses to add
        left_remove: number of left parentheses to remove
        """
        if i == len(s):
            res.add("".join(path))  # need to remove duplicates
            return
        
        if s[i] == "(":
            if leftcnt > 0:  # do not delete
                path.append(s[i])  
                self.dfs(s, i+1, res, path, leftcnt-1, rightcnt, 
                         left_remove, right_remove)
                path.pop()
            if left_remove > 0:  # delete
                self.dfs(s, i+1, res, path, leftcnt, rightcnt, 
                         left_remove-1, right_remove)
        elif s[i] == ")":
            if rightcnt > leftcnt:  # not rightcnt > 0
                path.append(s[i])
                self.dfs(s, i+1, res, path, leftcnt, rightcnt-1,
                        left_remove, right_remove)
                path.pop()
            if right_remove > 0:
                self.dfs(s, i+1, res, path, leftcnt, rightcnt,
                        left_remove, right_remove-1)
        else:
            path.append(s[i])
            self.dfs(s, i+1, res, path, leftcnt, rightcnt,
                    left_remove, right_remove)
            path.pop()  # do not forget
        
                
"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
    
