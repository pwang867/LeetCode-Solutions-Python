# dp, O(n)


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 3
        self.N = 10 ** 9 + 7
        # (last_record, num_A, num_continous_L)
        dp = {('A', 1, 0): 1, ('L', 0, 1): 1, ('P', 0, 0): 1}
        for step in range(n - 1):
            dp = self.add_one_record(dp)
        return sum(dp.values()) % self.N

    def add_one_record(self, dp):
        res = collections.defaultdict(int)
        for key, cnt in dp.items():
            last_record, num_A, num_L = key
            if num_A == 0:
                res[('A', 1, 0)] = (res[('A', 1, 0)] + cnt) % self.N
            if num_L <= 1:
                res[('L', num_A, num_L + 1)] = (res[('L', num_A, num_L + 1)] + cnt) % self.N
            res[('P', num_A, 0)] = (res[('P', num_A, 0)] + cnt) % self.N
        return res


"""
Given a positive integer n, return the number of all possible attendance records with length n, 
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) 
or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.
"""
