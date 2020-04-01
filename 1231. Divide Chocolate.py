"""
More Good Binary Search Problems
Here are some similar binary search problems.
Also find more explanations.
Good luck and have fun.

875. Koko Eating Bananas
774. Minimize Max Distance to Gas Station

1011. Capacity To Ship Packages In N Days
410. Split Array Largest Sum
1231. Divide Chocolate
"""


# this is a max-min problem, min-max and max-min happens at the same time
# time O(log(sum(sweetness)))
class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        if K <= 0:
            return sum(sweetness)
        if  K+1 == len(sweetness):
            return min(sweetness)
        
        left, right = min(sweetness)-1, sum(sweetness)+1
        while left + 1 < right:
            mid = left + (right-left)//2
            groups = self.partition(sweetness, mid)
            if len(groups) < K+1:
                right = mid
            else:
                left = mid
        
        if len(self.partition(sweetness, right)) == K+1:
            return right
        return left
    
    def partition(self, arr, minNum):
        total = 0
        groups = []
        for num in arr:
            total += num
            if total >= minNum:
                groups.append(total)
                total = 0
        groups[-1] += total
        return groups


# dp, time O(K*n*n)
# time limit exceeded
class Solution1(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        n = len(sweetness)
        
        # presum
        sums = [0]*n
        total = 0
        for i, num in enumerate(sweetness):
            total += num
            sums[i] = total
        
        K += 1
        dp = [[0]*n for _ in range(K+1)]
        dp[1] = sums[:]
        for i in range(2, K+1):
            for j in range(i-1, n):
                for k in range(j-1, -1, -1):
                    dp[i][j] = max(dp[i][j], min(sums[j]-sums[k], dp[i-1][k]))
                    if dp[i-1][k] < sums[j]-sums[k]:
                        break
        return dp[K][n-1]
    


"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
"""


if __name__ == "__main__":
    sweetness = [87002,22650,61737,4432,87341,67643,13454,83823,87836,2978,99313,82797,77350,55994,31403,73836,54451,54807,60146,72381,7271,37633,32603,33752,78004,76288,94608,3516,98287,16577,36186,40401,70733,35764,76303,74279,18351,74113,26480,64253,49402,47512,37185,42488,43068,3542,55773,91365,86770,52915]
    K = 3  # 641293
        
    #sweetness = [7,1,6,9]
    #K = 2
        
    #sweetness = [90670,55382,95298,95795,73204,41464,18675,30104,47442,55307]
    #K = 6    # answer 55382
    
    print(Solution().maximizeSweetness(sweetness, K))
    