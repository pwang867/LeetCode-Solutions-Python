# worst case is always O(M*N*N*K), but it is a sparse matrix

import collections


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0] or not B or not B[0]:
            return []
        M, N, K = len(A), len(A[0]), len(B[0])
        dA = self.simplify(A)
        dB = self.simplify(B)
        res = [[0] * K for _ in range(M)]
        for i in dA:
            for j in dA[i]:
                if j in dB:
                    for k in dB[j]:
                        res[i][k] += dA[i][j] * dB[j][k]
        return res

    def simplify(self, mat):
        d = collections.defaultdict(collections.defaultdict)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:  # turn matrix into sparse dictionary
                    d[i][j] = mat[i][j]
        return d


"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
