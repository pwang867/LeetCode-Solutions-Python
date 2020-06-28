# method 2, time O(n^4), space is O(n^2)
# complexity is the same as method 1, but much faster for sparse matrix


from collections import defaultdict


class Solution2(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return 0
        n = len(A)
        ones_A = []
        ones_B = []
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    ones_A.append(i * 100 + j)
                if B[i][j] == 1:
                    ones_B.append(i * 100 + j)
        counts = defaultdict(int)
        for a in ones_A:
            for b in ones_B:
                counts[a - b] = counts.get(a - b, 0) + 1
        return max(counts.values()) if counts else 0


# method 1, time complexity is O(n^4), space is O(n^2)


class Solution1(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return 0
        n = len(A)
        max_overlap = 0
        for i in range(-(n - 1), n):
            for j in range(-(n - 1), n):
                # (i, j) is the position of the topleft corner of A in B, offset
                overlap = 0
                for p in range(max(-i, 0), min(n, n - i)):
                    for q in range(max(-j, 0), min(n, n - j)):
                        x, y = i + p, j + q  # (p, q) for A, (x, y) for B
                        if A[p][q] == B[x][y] == 1:
                            overlap += 1
                max_overlap = max(max_overlap, overlap)
        return max_overlap


"""
Two images A and B are given, represented as binary, square matrices of the same size.  
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), 
and place it on top of the other image.  After, the overlap of this translation is the number of positions 
that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""
