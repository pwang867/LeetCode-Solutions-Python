# use heap, because most of the pairs are actually not used
# time O(M*N + N*M*logN*logM), space O(M*N)
import heapq
class Solution(object):
    def assignBikes(self, workers, bikes):
        pairs = []  # list of list, pairs[i] means the pairs for worders[i]
        for i, worker in enumerate(workers):
            cur_pairs = []
            for j, bike in enumerate(bikes):
                cur_pairs.append((self.dist(worker, bike), i, j))
            heapq.heapify(cur_pairs)
            pairs.append(cur_pairs)
        
        # candidates saves the shortest dist for each worker
        candidates = [heapq.heappop(cur_pairs) for cur_pairs in pairs]    # a heap
        heapq.heapify(candidates)
        used_bikes = set()
        ids = [-1]*len(workers)  # ids[i] is the bike id assigned to workers[i]
        
        while len(used_bikes) < len(workers):
            dist, iworker, ibike = heapq.heappop(candidates)
            if ibike not in used_bikes and ids[iworker] == -1:
                ids[iworker] = ibike
                used_bikes.add(ibike)
                # worker[i] is done, no need to add next pair from pairs[i]
            else:
                heapq.heappush(candidates, heapq.heappop(pairs[iworker]))
        
        return ids
    
    def dist(self, worker, bike):
        return abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
    

# brute force, time O(n*log(n)), where n is number of pairs
# space is O(n)
class Solution1(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        pairs = [(self.dist(worker, bike), i, j) 
                 for i, worker in enumerate(workers) 
                 for j, bike in enumerate(bikes)]
        
        self.sort(pairs)
        
        used = [False]*len(bikes)
        ids = [-1]*len(workers)  # ids[i] is the bike id assigned to worker i
        cnt = 0
        
        for dist, iworker, ibike in pairs:
            if not used[ibike] and ids[iworker]==-1:
                ids[iworker] = ibike
                used[ibike] = True
                cnt += 1
                if cnt == len(workers):  # early termination
                    # only saves O(n), not effective
                    break
        
        return ids
        
        
    def dist(self, pos1, pos2):
        # Manhattan distance
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    
    def sort(self, pairs):
        return pairs.sort()
