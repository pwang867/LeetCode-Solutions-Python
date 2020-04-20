# time log(A) + log(B) + log(N), space O(1)
# binary search
# least common multiple, and greatest common divisor


class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        BASE = 10 ** 9 + 7
        lcm = A * B / self.gcd(A, B)  # least common multiple
        left, right = min(A, B), min(A, B) * N
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.count(mid, A, B, lcm) >= N:
                right = mid
            else:
                left = mid
        if self.count(left, A, B, lcm) == N:
            return left % BASE
        else:
            return right % BASE

    def count(self, val, A, B, lcm):
        # count number of magical numbers <= val
        return val // A + val // B - val // lcm

    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)


# method 1, brute force, time O(N), TLE


class Solution1(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        i, j = 1, 1
        res = 0
        for _ in range(N):
            if i * A == j * B:
                res = i * A
                i += 1
                j += 1
            elif i * A > j * B:
                res = j * B
                j += 1
            else:
                res = i * A
                i += 1
        return res


"""
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8


Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
"""