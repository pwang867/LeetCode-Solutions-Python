import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:
            return 0
        events.sort()
        print(events)
        heap = []
        time = events[0][0]
        cnt = 0
        i = 0
        while i < len(events):
            if not heap:
                time = events[i][0]
            print("\n\n", heap, cnt, time)
            start, end = events[i]
            while i < len(events) and events[i][0] == start:
                heapq.heappush(heap, events[i][1])
                i += 1
            print(heap)
            while heap and (i >= len(events) or (time < events[i][0])):
                end = heapq.heappop(heap)
                if end >= time:
                    cnt += 1
                    time += 1
        return cnt


events = [[25,26],[19,19],[9,13],[16,17],[17,18],[20,21],[22,25],[11,12],
          [19,23],[7,9],[1,1],[21,23],[14,14],[4,7],[16,16],[24,28],[16,18],
          [4,5],[18,20],[16,16],[25,26]]

print(Solution().maxEvents(events))