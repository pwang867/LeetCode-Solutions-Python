# method 2, instead of saving path, we can save usable cols to save time
# time < O(n!)
class Solution2(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs(set(range(n)), set(), set(), n)
        return self.res
    
    def dfs(self, cols, diag, adiag, n):
        # cols, diag, anti-diag: set
        if len(cols) == 0:
            self.res += 1
            return
        i = n - len(cols)
        for j in cols:
            if i - j not in diag and i + j not in adiag:
                cols.remove(j)
                diag.add(i-j)
                adiag.add(i+j)
                self.dfs(cols, diag, adiag, n)
                cols.add(j)
                diag.remove(i-j)
                adiag.remove(i+j)


class Solution1(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        self.helper([], n, 0)
        return self.ans
    
    def helper(self, path, n, i):
        # path stores (i, j) positions of already placed queens
        # i: the i-th row
        # base case
        if i == n:
            self.ans += 1
        # try every position in i-th row
        for j in range(n):
            if self.isSafe(path, n, i, j):
                path.append((i, j))
                self.helper(path, n, i + 1)
                path.pop()
    
    def isSafe(self, path, n, i, j):
        # check if (i, j) will be attacked by previous queens in path
        for ii, jj in path:
            if ii == i or jj == j or ii - jj == i - j or ii + jj == i + j:
                return False
        return True



"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

from time import time
for n in range(14, 16):
    t1 = time()
    print(Solution2().totalNQueens(n))
    print(n, time() - t1)
