# method 3: based on method 2, 
# use O(n) time to do a pre-check self.maxSum() for sums 
# before using O(n*log(n)) to run maxSumUnderk()
import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        
        res = -float('inf')
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix = [[matrix[j][i] for j in range(m)] for i in range(n)]
            m, n = n, m
        for i in range(m):
            sums = [0]*n
            for j in range(i, m):
                sums = [sums[p] + matrix[j][p] for p in range(n)]
                temp = self.maxSum(sums)  # this step greatly saves time
                if temp > k:
                    temp = self.maxSumUnderk(sums, k)
                res = max(res, temp)
        
        return res
    
    def maxSum(self, nums):
        # max sum of continous array
        max_sum = -float('inf')
        cur_sum = 0
        
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
    
    def maxSumUnderk(self, nums, k):
        # return the max sum which <= k, return None if not found
        pre_sums = []
        cur_sum = 0
        
        res = -float('inf')
        for num in nums:
            bisect.insort(pre_sums, cur_sum)  # search O(log(n)), insert O(n)
            cur_sum += num
            i = bisect.bisect_left(pre_sums, cur_sum - k)
            if i != len(pre_sums):
                res = max(res, cur_sum - pre_sums[i])
        
        return res


# method 2: close to O(max(m,n)*log(max(m,n))*min(m,n)^min(m,n))
# we can use sortedcontainers.SortedList() instead of bisect.insort() 
# to save insertion time cost of nearly O(n)
# when m >> n, len(pre_sums) == m so that time complexity is m*log(m)*n*n
import bisect
class Solution2(object):
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]:
            return None
        
        res = -float('inf')
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix = [[matrix[j][i] for j in range(m)] for i in range(n)]
            m, n = n, m
        for i in range(m):
            sums = [0]*n
            for j in range(i, m):
                sums = [sums[p] + matrix[j][p] for p in range(n)]
                temp = self.maxSumSubarray(sums, k)
                if temp is not None:
                    res = max(res, temp)
        
        return res
    
    def maxSumSubarray(self, nums, k):
        # return the max sum which <= k, return None if not found
        pre_sums = []
        cur_sum = 0
        
        res = None
        for num in nums:
            bisect.insort(pre_sums, cur_sum)  # search O(log(n)), insert O(n)
            cur_sum += num
            i = bisect.bisect_left(pre_sums, cur_sum - k)
            if i != len(pre_sums):
                if res is None:
                    res = cur_sum - pre_sums[i]
                else:
                    res = max(res, cur_sum - pre_sums[i])
        
        return res

# method 1: brute force, try every possible submatrix
# time O(m^2*n^2), space O(m*n), Time Limit Exceeded
class Solution1(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        
        m, n = len(matrix), len(matrix[0])
        sums = [[0]*(n+1) for _ in range(m+1)]
        
        # prepare sums matrix
        for i in range(1, m+1):
            for j in range(1, n+1):
                sums[i][j] = matrix[i-1][j-1] + sums[i-1][j] + sums[i][j-1] \
                            - sums[i-1][j-1]
        
        # find the max sum of all submatrix
        ans = None
        for i in range(1, m+1):
            for j in range(1, n+1):
                for p in range(i, m+1):
                    for q in range(j, n+1):
                        area = sums[p][q] + sums[i-1][j-1] \
                                - sums[i-1][q] - sums[p][j-1]
                        if area <= k:
                            ans = area if ans is None else max(ans, area)
        
        return ans
        
