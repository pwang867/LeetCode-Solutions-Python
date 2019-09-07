class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # find the shared rectangular (x1, y1) -- (x2, y2)
        x1 = max(A, E)
        x2 = min(C, G)
        y1 = max(B, F)
        y2 = min(D, H)
        
        overlap = 0
        if x1 < x2 and y1 < y2:
            overlap = (x2 - x1) * (y2 - y1)
        
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap
    
