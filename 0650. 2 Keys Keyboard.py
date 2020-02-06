# method 2, math, greedy
# sum of all prime factors, time O(n), space O(1)
# reason p*q > p+q, so if you have (p+q) operations, always try to copy + (p-1) pase + copy + (q-1) paste
class Solution(object):
    def minSteps(self, n):
        if n == 1: return 0
        res = 0
        divisor = 2
        while n > 1:
            while n%divisor == 0:
                n /= divisor
                res += divisor
            divisor += 1
        return res


# method 1, brute force, dfs with memo, time/space O(n^2)
class Solution1(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 2
        self.res = float('inf')
        self.memo = {}
        self.dfs(2, 1, 2, n)
        return self.res
    
    def dfs(self, count, copy, step, n):
        if count == n:
            self.res = min(self.res, step)
            return
        if count > n:
            return
        if step + 1 >= self.res:   # early termination
            return
        if (count, copy) in self.memo and self.memo[(count, copy)] <= step:
            return
        self.memo[(count, copy)] = step
        # copy + paste
        self.dfs(count*2, count, step+2, n)
        # paste
        self.dfs(count+copy, copy, step+1, n)


"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
 

Note:

The n will be in the range [1, 1000].
"""
