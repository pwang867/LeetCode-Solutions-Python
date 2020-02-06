class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        cnt = 0
        
        for p in points:
            p = tuple(p)
            # build a dictionary {dist^2: set of points}, 
            # or (dist^2: num of points)
            d = {}
            for q in points:
                q = tuple(q)
                dist = (p[0] - q[0])**2 + (p[1] - q[1])**2
                if dist in d:
                    d[dist].add(q)
                else:
                    d[dist] = {q}
            # iterate the dictionary
            for key, value in d.items():
                if len(value) >= 2:
                    cnt += len(value)*(len(value) - 1)
        
        return cnt
    
