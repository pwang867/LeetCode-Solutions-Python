# self.meo[(i,j,m)] means the total cost to merge stones[i:j+1] into m groups
# time O(n*(n/K)*K*n/k)=O(n^3/K), space O(n*n*k)


class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        if K <= 1 or (len(stones) - 1) % (K - 1) != 0:
            return -1
        self.presums = [0] * (len(stones) + 1)
        total = 0
        for i, stone in enumerate(stones):
            total += stone
            self.presums[i + 1] = total
        self.memo = {}
        return self.dfs(0, len(stones) - 1, 1, K)

    def dfs(self, i, j, m, K):
        if i == j:
            return 0 if m == 1 else float('inf')
        if j - i + 1 == m:
            return 0
        if (i, j, m) in self.memo:
            return self.memo[(i, j, m)]
        if m == 1:
            return self.dfs(i, j, K, K) + self.presums[j + 1] - self.presums[i]
        else:
            res = float('inf')
            for k in range(i, j, K - 1):
                res = min(res, self.dfs(i, k, 1, K) + self.dfs(k + 1, j, m - 1, K))
            self.memo[(i, j, m)] = res
            return res


"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""