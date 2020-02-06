# method 2, Huffman's method, greedy, use heap
# time O(n*log(n)), space O(n)
# ref: https://leetcode.com/problems/minimum-time-to-build-blocks
# /discuss/387035/Python%3A-O(n-log-n)-using-Huffman's-Algorithm-(priority-queue)
# -with-explanation.
import heapq
class Solution(object):
    def minBuildTime(self, blocks, split):
        heapq.heapify(blocks)
        while len(blocks) > 1:
            num1 = heapq.heappop(blocks)
            num2 = heapq.heappop(blocks)
            heapq.heappush(blocks, num2 + split)
        return blocks[0]
    

# method 1, dp[n][n], space O(n^2), time O(n^3), time limit exceeded
# dp[i][j] means the min time needed for one worker to finish blocks[i:j+1]
class Solution1(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        if not blocks:
            return 0
        if len(blocks) == 1:
            return blocks[0]
        blocks.sort()
        
        n = len(blocks)
        dp = [[float('inf')]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = blocks[i]
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                for k in range(j-1, i-1, -1):
                    dp[i][j] = min(dp[i][j], split + max(dp[i][k], dp[k+1][j]))
                    if dp[i][k] <= dp[k+1][j]:
                        break
        
        return dp[0][-1]
    
