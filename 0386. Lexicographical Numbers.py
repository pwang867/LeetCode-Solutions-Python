

# DFS recursion
class Solution2(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10):
            if i <= n:
                self.dfs(i, n, res)
        return res
    
    def dfs(self, total, n, res):
        res.append(total)
        for digit in range(10):
            next_num = total*10 + digit
            if next_num <= n:
                self.dfs(next_num, n, res)


# DFS iteration
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        stack = [x for x in range(9, 0, -1) if x <= n]
        while stack:
            node = stack.pop()
            res.append(node)
            for digit in range(9, -1, -1):
                new_node = node*10 + digit
                if new_node <= n:
                    stack.append(new_node)
                else:  # effective pruning
                    return
        return res


"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
