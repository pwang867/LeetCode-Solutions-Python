# we only need to prove that there is no loop of blocks enclosing
# the source and target, so we need to do BFS twice.
# If the BFS depth is larger than len(blocked), then it means the source
# is not in the loop

from collections import deque
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        if not blocked:
            return True
        
        blocked = map(tuple, blocked)
        blocked = set(blocked)
        source, target = tuple(source), tuple(target)
        
        if source in blocked:
            return False
        
        return self.bfs(blocked, source, target) \
                and self.bfs(blocked, target, source)
    
    def bfs(self, blocked, source, target):
        """check if there is a loop of blocks around the source"""
        level = deque([source])
        depth = 0
        visited = {source}
        while level:
            n = len(level)
            for _ in range(n):
                i, j = level.popleft()
                if (i, j) == target:
                    return True
                for v in [(1,0), (-1,0), (0,1), (0,-1)]:
                    p, q = i + v[0], j + v[1]
                    if p >= 0 and q >= 0 and (p, q) not in visited \
                    and (p, q) not in blocked:
                        visited.add((p, q))
                        level.append((p, q))
            depth += 1
            if depth == len(blocked):
                return True
        return False
    
