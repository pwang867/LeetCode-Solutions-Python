# Kuhn-Munkres Algorithm for Optimal Matching of Weighted Bipartite Graph
# time O(n^4), can be optimized to O(n^3)


class Solution(object):
    # m = len(workers), n = len(bikes)
    def __init__(self):
        self.dist = []   # m*n
        self.costW = []  # m
        self.costB = []  # n
        self.match = []  # n, i=match[j] means j-th bike is assigned to i-th worker

    def initDist(self, workers, bikes):
        self.dist = [[abs(worker[0]-bike[0]) + abs(worker[1]-bike[1]) 
                        for bike in bikes] for worker in workers]
    
    def initCost(self, workers, bikes):
        self.costW = [min(self.dist[i]) for i in range(len(workers))]
        self.costB = [0]*len(bikes)
    
    def augment(self, i, visW, visB):  
        """ to assign a bike for worker i """
        visW[i] = True
        for j in range(len(self.dist[0])):
            if visB[j] or self.costW[i] + self.costB[j] < self.dist[i][j]:
                continue
            visB[j] = True
            if self.match[j] < 0 or self.augment(self.match[j], visW, visB):
                self.match[j] = i
                return True
        return False
    
    def update(self, visW, visB):
        delta = float('inf')
        for i in range(len(visW)):
            if visW[i]:
                for j in range(len(visB)):
                    if not visB[j]:
                        delta = min(delta, self.dist[i][j]-self.costW[i]-self.costB[j])
        for i in range(len(visW)):
            if visW[i]:
                self.costW[i] += delta
        for j in range(len(visB)):
            if visB[j]:
                self.costB[j] -= delta
    
    def assignBikes(self, workers, bikes):
        self.initDist(workers, bikes)
        self.initCost(workers, bikes)
        self.match = [-1]*len(bikes)
        print(self.dist)
        # search optimal assignment
        for i, worker in enumerate(workers):
            while True:
                visW = [False]*len(workers)
                visB = [False]*len(bikes)
                if self.augment(i, visW, visB):  # solution found
                    break
                else:
                    self.update(visW, visB)
            print(i, self.match)
        
        # get optimal result
        ans = 0
        for j in range(len(bikes)):
            if self.match[j] >= 0:
                ans += self.dist[self.match[j]][j]
        return ans


if __name__ == "__main__":
    workers = [[0,0],[1,1],[2,0], [10,0],[11,1],[12,0]]
    bikes = [[12,0],[2,2],[2,1], [10,0],[11,1],[1,0]]
    print(Solution().assignBikes(workers, bikes))
