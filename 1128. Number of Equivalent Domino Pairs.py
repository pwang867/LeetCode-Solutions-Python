# method 2: use the fact that 1 <= donimoes[i][j] <= 9
# space O(9*9) = O(1), time O(N + 9*9)

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        M = 9
        dp = [[0]*(M+1) for _ in range(M+1)]
        
        for i, j in dominoes:
            dp[i][j] += 1
        
        res = 0
        for i in range(1, M+1):
            for j in range(1, i+1):
                # be careful about i==j
                cnt = dp[i][j] + dp[j][i] if i != j else dp[i][j]
                res += cnt*(cnt-1)/2
        
        return res


# method 1: flip the dominoes and sort them
# time O(N*log(N)), space O(N) due to overwriting dominoes
class Solution1(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dominoes = map(lambda x: [min(x), max(x)], dominoes)
        dominoes.sort()
        
        res = 0
        cnt = 1
        for i in range(len(dominoes)-1):
            if dominoes[i+1] == dominoes[i]:
                cnt += 1
            else:
                res += cnt*(cnt-1)/2
                cnt = 1
        res += cnt*(cnt-1)/2
        
        return res
    
