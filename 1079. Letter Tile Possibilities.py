# use array, dfs, time O(n!)

class Solution2(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = sorted(list(tiles))
        return self.dfs(tiles)

    def dfs(self, tiles):
        if not tiles:
            return 0
        res = 0
        for i, tile in enumerate(tiles):
            if i > 0 and tiles[i] == tiles[i - 1]:
                continue
            res += 1 + self.dfs(tiles[:i] + tiles[i + 1:])
        return res


from collections import Counter
class Solution1(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        cnts = Counter(tiles)
        res = 0
        for c in cnts.keys():    # mistake: for c in cnts: # cnts will be changed during recursion, easy to cause bugs
            res += self.dfs(c, cnts)
        return res

    def dfs(self, c, cnts):
        if not cnts:
            return 0
        cnts[c] -= 1
        if cnts[c] == 0:
            del cnts[c]
        res = 1  # current path itself
        for key in cnts.keys():
            res += self.dfs(key, cnts)
        cnts[c] = cnts.get(c, 0) + 1
        return res


"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""