"""
for a directed graph, those three conditions must be met:
1. there is one and only one node who has no parent,
    and the only node without parent is the root
2. every node has no more than 2 children  (automatically satisfied in this problem)
3. only one connected component（method to use: union find，or dfs starting from root）
"""


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        out_deg = [0] * n
        in_deg = [0] * n
        for i in range(n):
            for j in [leftChild[i], rightChild[i]]:
                if j != -1:
                    out_deg[i] += 1
                    if out_deg[i] > 2:  # more than two children  (unnecessary work)
                        return False
                    in_deg[j] += 1
                    if in_deg[j] > 1:  # more than two parents
                        return False

        # find root
        root = -1
        for i in range(n):
            if in_deg[i] == 0:
                if root != -1:  # two roots
                    return False
                root = i
        if root == -1:  # no root
            return False

        # check no circle, and one component
        visited = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue
                if child in visited:  # has circle
                    return False
                else:
                    visited.add(child)
                    stack.append(child)
        return len(visited) == n


"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.



Example 1:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:



Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:



Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false


Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""