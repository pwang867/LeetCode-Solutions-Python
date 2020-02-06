# method 2, greedy, O(n^2)
# let R = height // sideLength, C = width // sideLength
# let r = height % sideLength, c = width % sideLength
# divide each "tile"(square) into four areas: B[:r, :c],(B[:r, c:], B[r:, :c]), B[r:,c:]
# B[:r, :c] is the most feasible, while B[r:,c:] is the least. when C > R, choose B[:r, c:] over B[r:, :c]
class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        scores = []
        for i in range(sideLength):
            for j in range(sideLength):
                m = (height-i)//sideLength + ((height-i)%sideLength!=0)
                n = (width-j)//sideLength + ((width-j)%sideLength!=0)
                scores.append(m*n)
        scores.sort(reverse=True)
        return sum(scores[:maxOnes])
    

# brute force, DFS, time O(2^n*sideLength^2), n=width*height
# time limit exceeded
class Solution1(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        mat = [[0]*width for _ in range(height)]
        self.res = 0
        self.dfs(mat, 0, 0, 0, sideLength, maxOnes)
        return self.res
    
    def dfs(self, mat, i, j, cnt, sideLength, maxOnes):
        if cnt + (len(mat)-1-i)*len(mat[0]) + len(mat[0])-j <= self.res:
            # early cutoff
            return
        if j == len(mat[0]):
            self.dfs(mat, i+1, 0, cnt, sideLength, maxOnes)
        elif i == len(mat):
            self.res = max(self.res, cnt)
        else:
            # fill mat[i][j] with 1
            one_in_square = 0
            for p in range(max(i-sideLength+1,0), i+1):
                for q in range(max(j-sideLength+1, 0), j+1):
                    one_in_square += mat[p][q]
            if one_in_square < maxOnes:
                mat[i][j] = 1
                self.dfs(mat, i, j+1, cnt+1, sideLength, maxOnes)
                mat[i][j] = 0
            if one_in_square <= maxOnes:
                # fill mat[i][j] with 0
                self.dfs(mat, i, j+1, cnt, sideLength, maxOnes)


"""
Consider a matrix M with dimensions width * height, such that every cell has value 0 or 1, and any square sub-matrix of M of size sideLength * sideLength has at most maxOnes ones.

Return the maximum possible number of ones that the matrix M can have.

 

Example 1:

Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
Output: 4
Explanation:
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
Example 2:

Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
Output: 6
Explanation:
[1,0,1]
[1,0,1]
[1,0,1]
 

Constraints:

1 <= width, height <= 100
1 <= sideLength <= width, height
0 <= maxOnes <= sideLength * sideLength
"""
