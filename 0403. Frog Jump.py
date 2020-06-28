# method 2: recursion with memo, time < O(n^2), space O(n)
# improved from method 1: changes stones to a set and make the checking much faster


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return True
        
        self.memo = set()  # to save failed jump paths
        return self.canCrossHelper(set(stones), 0, 0, stones[-1])  # mistake: self.dfs(set(stones), 0, 1, stones[-1])
    
    def canCrossHelper(self, stones, pos, pre_jump, target):
        # pos is the position of the stones, not the index of stones array
        if pos == target:
            return True
        if (pos, pre_jump) in self.memo:
            return False
        
        for step in (pre_jump-1, pre_jump, pre_jump+1):  # here is different from method 1, much faster
            if step > 0 and pos+step in stones and \
            self.canCrossHelper(stones, pos+step, step, target):
                return True
        
        self.memo.add((pos, pre_jump))
        return False
    

# method 1: recursion with memo, time < O(n^2), space O(n)
class Solution2(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.memo = set()  # to save failed jump paths
        return self.canCrossHelper(stones, 0, 0)
    
    def canCrossHelper(self, stones, pos, pre_jump):
        if pos == len(stones) - 1:
            return True
        if (pos, pre_jump) in self.memo:
            return False
        
        for i in range(pos+1, len(stones)):
            to_jump = stones[i] - stones[pos]
            if to_jump > pre_jump + 1:
                self.memo.add((pos, pre_jump))
                return False
            elif to_jump >= pre_jump - 1 and to_jump <= pre_jump + 1 \
                and self.canCrossHelper(stones, i, to_jump):
                    return True
        
        self.memo.add((pos, pre_jump))
        return False


"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able 
to cross the river by landing on the last stone. Initially, the frog is on the first stone and 
assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""

