# union find, O(N^2), N=len(grid)

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        N = len(grid)
        # cut each cell into four triangles, top=0, left=1, bottom=2, right=3
        parent = {(i, j, k): (i, j, k) for i in range(N) 
                  for j in range(N) for k in range(4)}
        size = {(i, j, k): 1 for i in range(N) 
                for j in range(N) for k in range(4)}
        
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            return False
        
        for i in range(N):
            for j in range(N):
                # connect triangles in neighboring cells
                # only connect to top and left neighbors to avoid duplicate work
                if i - 1 >= 0:   
                    union((i-1, j, 2), (i, j, 0))
                if j - 1 >= 0:
                    union((i, j-1, 3), (i, j, 1))
                # connect triangles within the cell
                if grid[i][j] != "\\":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                    
        map(find, parent)
        return len(set(parent.values()))


"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

 

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
