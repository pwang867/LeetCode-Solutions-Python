class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 0:
            return [0, 0]
        
        max_W = int(pow(area, 0.5))
        
        for W in range(max_W, 0, -1):
            if area%W == 0:
                return [area/W, W]
        
