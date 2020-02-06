# method 2, space O(num of operations of .flip()), time O(1)
# main idea is the same as method 1 -- to switch with the end, but saves more space

# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
import random
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_cols = n_cols
        self.N = n_rows*n_cols
        self.d = {}  # {index: val}, if i not in self.d, it means self.d[i]=i
        self.n = self.N  # the total number of usable elements

    def flip(self):
        """
        :rtype: List[int]
        """
        if self.n == 0:
            return []
        i = random.randrange(self.n)
        res = self.d.get(i, i)
        self.d[i] = self.d.get(self.n - 1, self.n - 1)   # switch with the end
        if self.n - 1 in self.d:  # then delete the end to save space
            del self.d[self.n-1]
        self.n -= 1
        return divmod(res, self.n_cols)

    def reset(self):
        """
        :rtype: None
        """
        self.d.clear()
        self.n = self.N


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()


# method 1, space O(m*n), time O(1)
# memory limit exceeded
import random
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.idx = [[i, j] for i in range(n_rows) for j in range(n_cols)]
        self.N = n_rows*n_cols
        self.n = self.N

    def flip(self):
        """
        :rtype: List[int]
        """
        if self.n == 0:
            return []
        i = random.randrange(self.n)
        res = self.idx[i]
        self.idx[i], self.idx[self.n-1] = self.idx[self.n-1], self.idx[i]
        self.n -= 1
        return res

    def reset(self):
        """
        :rtype: None
        """
        self.n = self.N


"""
You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input: 
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input: 
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
