# optimal, using math, time O(log(N))


class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.pairs = {'0': '0', '1': '1', "6": '9', '8': '8', '9': '6'}
        self.smaller = {'0': 0, "1": 1, '2': 2, '3': 2, '4': 2,
                        '5': 2, '6': 2, '7': 3, '8': 3, '9': 4}
        self.smaller_sym = {'0': 0, "1": 1, '2': 2, '3': 2, '4': 2,
                            '5': 2, '6': 2, '7': 2, '8': 2, '9': 3}
        self.sym = {'0', '1', '8'}
        return self.count_valid(N + 1) - self.count_non_confusing(N + 1)

    def count_valid(self, N):
        # count all valid numbers that are still numbers after flip
        s = str(N)
        cnt = 0
        for i, digit in enumerate(s):
            cnt += self.smaller[digit] * 5 ** (len(s) - 1 - i)
            if digit not in self.pairs:
                break
        # print("all", N, cnt)
        return cnt

    def count_non_confusing(self, N):
        # return total counts of numbers < N
        if N < 10:
            return self.sym[str(N)]
        s = str(N)
        cnt = 0
        for length in range(len(s)):  # count symmetric number with shorter length
            cnt += self.count_all_non_confusing_with_length(length)
        if len(s) % 2 == 1:  # for center
            factor = 3
        else:
            factor = 1
        for i in range(len(s) // 2):  # count same length
            digit = s[i]
            if i == 0:
                cnt += max(self.smaller[digit] - 1, 0) * 5 ** ((len(s) - 2 - 2 * i) // 2) * factor
            else:
                cnt += self.smaller[digit] * 5 ** ((len(s) - 2 - 2 * i) // 2) * factor
            if digit not in self.pairs:
                break
        else:
            half = s[:len(s) // 2]
            other_half = "".join([self.pairs[x] for x in half[::-1]])
            if len(s) % 2 == 0:
                if int(half + other_half) < N:
                    cnt += 1
            else:
                cnt += self.smaller_sym[s[len(s) // 2]]
                if s[len(s) // 2] in self.sym and \
                        int(half + s[len(s) // 2] + other_half) < N:
                    cnt += 1
        # print("partial", N, cnt)
        return cnt

    def count_all_non_confusing_with_length(self, length):
        if length == 0:
            return 0
        elif length == 1:
            return 3
        if length % 2 == 0:
            return 4 * 5 ** (length // 2 - 1)
        else:
            return 4 * (5 ** (length // 2 - 1)) * 3



# method 1, dfs, time O(res) = O(5^m), m = length of N


class Solution1(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.cnt = 0
        self.pairs = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.valid_nums = {0, 1, 6, 8, 9}
        for x in [1, 6, 8, 9]:
            self.dfs(x, self.pairs[x], 10, N)
        return self.cnt

    def dfs(self, val, rev, level, N):
        if val <= N and val != rev:
            self.cnt += 1
        for x in self.valid_nums:
            if val * 10 + x <= N:
                y = self.pairs[x]
                self.dfs(val * 10 + x, y * level + rev, level * 10, N)


"""
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.



Example 1:

Input: 20
Output: 6
Explanation:
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation:
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].


Note:

1 <= N <= 10^9
Accepted
"""

