# x + (x+1) + ... + (x+k-1) = k*x + (k-1)*k//2 = N
# k*x = N - (k-1)*k//2
# 1. we can iterate on k
# 2. from N - (k-1)*k//2 > 0, we get k < sqrt(2*N) + 1
# time O(sqrt(N)), space O(1)

class Solution3(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for k in range(1, int(sqrt(2*N))+1):
            if (N-k*(k-1)//2) % k == 0:
                cnt += 1
        return cnt
    



# method 2, presums, time O(N), TLE
class Solution2(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        presums = {0}
        total = 0
        cnt = 1
        for i in range(1, (N+1)//2+1):
            total += i
            if total - N in presums:
                cnt += 1
            presums.add(total)
        return cnt
    


# method 1, time O(N), not optimal, TLE
# from m + ... + n == N, we can get (n*n+n) - (m*m-m) = N
# then use method similar to two-sum

class Solution1(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        visited = set()
        cnt = 1  # itself
        for i in range(1, (N+1)//2+1):
            cur = i*i + i
            target = cur - 2*N
            if target in visited:
                cnt += 1
            visited.add(i*i-i)
        return cnt


"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""
