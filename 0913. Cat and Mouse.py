# method 1, miniMax, top down dp
# time O(n^3*num_of_neighbors), space O(n^3)


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        return self.dfs(0, 1, 2, graph, {})

    def dfs(self, t, m, c, graph, memo):
        # t = turn, c = cat position, m = mouse position
        if t == 2 * len(graph) - 1:
            return 0  # a tie
        if m == 0:
            return 1  # Mouse wins
        if c == m:
            return 2  # Cat wins
        if (t, m, c) in memo:  # because we have an optimization of t == 2 * len(graph) - 1, we can not use t%2
            return memo[(t, m, c)]
        ret = -1
        if t % 2 == 0:  # mouse's turn
            res = [self.dfs(t + 1, nei, c, graph, memo) for nei in graph[m]]
            if 1 in res:
                ret = 1
            elif 0 in res:
                ret = 0
            else:
                ret = 2
        else:
            res = [self.dfs(t + 1, m, nei, graph, memo) for nei in graph[c] \
                   if nei != 0]
            if 2 in res:
                ret = 2
            elif 0 in res:
                ret = 0
            else:
                ret = 1
        memo[(t, m, c)] = ret
        return ret


# method 2, slightly optimized from method 1, same complexity


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        return self.dfs(0, 1, 2, graph, {})

    def dfs(self, t, m, c, graph, memo):
        # t = turn, c = cat position, m = mouse position
        if t == 2 * len(graph) - 1:
            return 0  # a tie
        if m == 0:
            return 1  # Mouse wins
        if c == m:
            return 2  # Cat wins
        if (t, m, c) in memo:
            return memo[(t, m, c)]
        ret = -1
        if t % 2 == 0:  # mouse's turn
            seen_zero = False
            for nei in graph[m]:
                tmp = self.dfs(t + 1, nei, c, graph, memo)
                if tmp == 1:
                    ret = 1
                    break
                elif tmp == 0:
                    seen_zero = True
            else:
                if seen_zero:
                    ret = 0
                else:
                    ret = 2
        else:
            seen_zero = False
            for nei in graph[c]:
                if nei == 0:  # cat can not go to hole
                    continue
                tmp = self.dfs(t + 1, m, nei, graph, memo)
                if tmp == 2:
                    ret = 2
                    break
                elif tmp == 0:
                    seen_zero = True
            else:
                if seen_zero:
                    ret = 0
                else:
                    ret = 1
        memo[(t, m, c)] = ret
        return ret



"""
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, 
if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated (ie. the players are in the same position as a previous turn, and 
it is the same player's turn to move), the game is a draw.
Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse, 2 if the game 
is won by Cat, and 0 if the game is a draw.

 

Example 1:

Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0
 

Note:

3 <= graph.length <= 50
It is guaranteed that graph[1] is non-empty.
It is guaranteed that graph[2] contains a non-zero element. 
"""
