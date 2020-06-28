"""
4/24/2020


partition function int -> int
f(n) = ...

3 = 1+1+1
  = 2+1
  = 3
f(3) = 3

4 = 1+1+1+1
  = 2+1+1 ( 1 1 2
  = 2+2
  = 3+1
  = 4
f(4) = 5

dfs(pre, remain): ascending order
3 = 1+1+1
  = 2+1
  = 3
pre, remain
None, 10
      1  9

      2  8
         2  6
         3  5

         4  4


      3  7

 n

 ~n!

3

  = 3
  = 1+2
  = 1+1+1

(n//2)*((n-1)//2) ****

"""


class Solution1:
    def partition(self, n):
        if n <= 0:
            return -1
        if n == 1:
            return 1
        self.memo = {}
        return self.dfs(None, n)

    def dfs(self, pre, remain):  # n -> n-1
        # pre < remain when entering DFS
        # return the counts of valid partitions
        if (pre, remain) in self.memo:
            return self.memo[(pre, remain)]
        res = 1
        # generate the next number
        if pre is None:
            pre = 1
        for num in range(pre, remain):  # remain-pre//2
            new_remain = remain - num
            if num > new_remain:
                break
            res += self.dfs(num, new_remain)
        self.memo[(pre, remain)] = res
        return res


"""
binary tree
balanced binary tree, defined as abs(height_left - height_right) <= 1

given n nodes for a balanced tree, how high can it possibly be?

  dp[h] = 1 + dp[h-1] + dp[h-2]

height:    0  1   2    3  h-1         h
min_nodes: 0  1   2    4  cnt1   n  cnt2

"""


# time/space O(log(n)), because dp is for h (height) = Log(n)


class Solution2:
    def max_height(self, n):
        dp = [0, 1]  # dp[h] is the minimum number of nodes for a tree with height h
        while dp[-1] <= n:
            dp.append(dp[-2] + dp[-1] + 1)
        return len(dp) - 2


"""
    root
  k  <=  n-1-k

[left_min, left_max]
[right_min, right_max]

if left_max+1 < right_min:
    return []
else:
    [min(right_min - 1, left_min)

dfs(n):
  return [min, max]

we are using the fact that when the root is highest, there must exist a configuration that all of 
its subtrees are highest-tree
"""


class Solution3:
    def __init__(self):
        self.memo = {}

    def dfs(self, n):   # return the height of highest possible tree
        if n in self.memo:
            return self.memo[n]
        if n <= 2:
            return n
        res = 0
        for k in range((n-1)//2+1):   # optimal solution will be one of those
            left = self.dfs(k)
            right = self.dfs(n-k-1)
            if abs(right-left) > 1:   # kind of greedy
                continue
            res = max(res, max(right, left)+1)
        self.memo[n] = res
        return res


if __name__ == "__main__":
    for n in range(20):
        print("\n")
        print(n)
        print(Solution2().max_height(n))
        print(Solution3().dfs(n))
