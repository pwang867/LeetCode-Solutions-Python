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
