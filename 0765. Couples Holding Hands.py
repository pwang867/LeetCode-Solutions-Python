# the seats of the couple don't matter, 
# as long as the couple is sitting together
# paired seats can be saved into a dictionary
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        d = {}
        for i in range(0, len(row), 2):
            d[row[i]] = row[i+1]
            d[row[i+1]] = row[i]
        
        cnt = 0
        s = set(d.keys())
        while s:
            x1 = s.pop()
            y1 = d[x1]
            if y1 != x1^1:
                # when a swap is needed
                # {x1:y1, x2:y2} becomes {x1:x2, y1:y2}
                cnt += 1
                x2 = x1^1
                y2 = d[x2]
                d[y1] = y2
                d[y2] = y1
                s.remove(x2)
            else:
                s.remove(y1)
        
        return cnt
    
