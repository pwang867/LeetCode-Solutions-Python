# time O(m*n*log(m*n))
# space O(m*n)

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    arr = []
                    self.dfs(grid, i, j, arr)
                    rotated_arrs = self.get_strs(arr, len(grid), len(grid[0]))
                    for rotated_arr in rotated_arrs:
                        if rotated_arr in islands:
                            break
                    else:
                        cnt += 1
                        islands |= rotated_arrs
        return cnt

    def dfs(self, grid, i, j, arr):
        # return a list of pairs of index of the island
        arr.extend([i, j])
        grid[i][j] = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(grid) and 0 <= q < len(grid[0]) and grid[p][q] == 1:
                self.dfs(grid, p, q, arr)

    def get_strs(self, arr, m, n):
        # return a set of strs by considering rotation and reflection
        top, bottom, left, right = float('inf'), -float('inf'), float('inf'), -float('inf')
        for k in range(len(arr) // 2):
            i, j = arr[2 * k], arr[2 * k + 1]
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)
        original = []
        rotate1 = []
        rotate2 = []
        rotate3 = []
        reflect_lr = []
        reflect_ud = []
        for k in range(len(arr) // 2):
            i, j = arr[2 * k], arr[2 * k + 1]
            original.extend([i - top, j - left])
            rotate1.extend([j - left, bottom - i])  # use the top left corner as reference
            rotate2.extend([bottom - i, right - j])
            rotate3.extend([right - j, i - top])
            reflect_lr.extend([i - top, right - j])
            reflect_ud.extend([bottom - i, j - left])
        res = set()
        for temp in [original, rotate1, rotate2, rotate3, reflect_lr, reflect_ud]:
            temp = self.sort(temp)
            temp = map(str, temp)
            res.add(" ".join(temp))  # use " " instead of ""
        return res

    def sort(self, arr):
        temp = [[arr[2 * i], arr[2 * i + 1]] for i in range(len(arr) // 2)]
        temp.sort()
        res = []
        for x, y in temp:
            res.append(x)
            res.append(y)
        return res


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
Note: The length of each dimension in the given grid does not exceed 50.
"""