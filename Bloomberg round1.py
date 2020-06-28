"""
integer, smallest positive

array
{2, 4, -1, 0, 9} -> return 1
{0, -1, -2} -> 1
{2, 3, 4} -> 1
{1, 2} -> 3
minimum positive number missing in the input list

1 2 3 ... n  -> n+1
2 3 n  -> 1 (<= n+1)

{-10, -9, -8}

method 1:
brute force, change to hashset space O(n) = len(arr), for (1, n+1) time O(n)


         i
{0, 2, -1, 4, 9} -> return 1
 1  2      4

           i
 {OO9, 2, 2, 4, 9} -> return 1
  1  2  3
Time : O(n)

5 4 1 2 3  < O(n)  6

method 2: time O(n) two for loops, space O(1) pointer, in place


     i     j
 {1, 4, 2, 4, 9} -> return 1

 [2, 1, 2, 4]
"""


class Bloomberg:
    def min_pos_num(self, arr):  # [2, 1, 2, 4]
        # method 2
        if not arr:
            return 1
        # move arr[i] to arr[arr[i]-1]
        i = 0
        while i < len(arr):  # i = 4
            val = arr[i]  # val= 4
            j = val - 1  # j = 3
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]  # [1, 2, 2, 4]
            else:
                i += 1  # i = 4
        # search missing number
        for i in range(len(arr)):  # [1, 2, 2, 4]
            if arr[i] != i + 1:
                return i + 1  # return 3
        return len(arr) + 1


"""
{ 1, 4, 9, 56, 12, 7, 1}
[(1, 0), (4, 1), (9, 2), ... ]

binary search

9 -> log(n)

        i j j+1
1 2 3 4 5 8  x

int ceil(int val);

50

7

1

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
streaming (card, time, station)
assumption: card, station are all unique
assumption: no missing data
unix epoch time (seconds)

average transit time between pairs of stations.

separate
station1 -> station2:
station2 -> station1:

starts = {card: (start_station, start_time)}
transition_time = end_time - start_time

trips = {(station1, station2): [total_time, total_counts]}

"""

import heapq


class Transportation:
    def __init__(self):
        self.starts = {}  # self.starts = {}
        self.trips = {}  # self.trips = [(s1, s3): [1, 1], (s3, s1): [1, 1]]

    def add_record(self, card, time, station):  # card2  3  s1, time O(1), add extra O(1)
        """
        card: str
        time: int, epoch time
        station: str
        """
        if card not in self.starts:
            # input is a start station
            self.starts[card] = [station, time]  #
        else:  # card2  3  s1
            start_station, start_time = self.starts[card]  # s3, 2
            del self.starts[card]
            transit_time = time - start_time  # 1
            if (start_station, station) not in self.trips:  # (s3, s1)
                self.trips[(start_station, station)] = [0, 0]
            self.trips[(start_station, station)][0] += transit_time
            self.trips[(start_station, station)][1] += 1

    def query_average_transit_time(self, start_station, end_station):  # time O(1)
        # return a float number
        key = (start_station, end_station)
        if key not in self.trips:
            raise ValueError("input data record not found")
        total_time, total_cnt = self.trips[(start_station, end_station)]
        if total_cnt == 0:
            raise ValueError("input data record not found")
        return total_time / total_cnt

    def add_record_for_median(self, card, time, station):  # log(n)
        """
        card: str
        time: int, epoch time
        station: str
        """
        if card not in self.starts:
            # input is a start station
            self.starts[card] = [station, time]  #
        else:  # card2  3  s1
            start_station, start_time = self.starts[card]  # s3, 2
            del self.starts[card]
            transit_time = time - start_time  # 1
            if (start_station, station) not in self.trips:  # (s3, s1)
                self.trips[(start_station, station)] = [[], []]
            max_heap, min_heap = self.trips[(start_station, station)]
            self._add_record_to_heaps(max_heap, min_heap, transit_time)

    def _add_record_to_heaps(self, max_heap, min_heap, transit_time):  # O(log(n))
        if not min_heap or transit_time <= min_heap[0]:
            heapq.heappush(max_heap, -transit_time)
        else:
            heapq.heappush(min_heap, transit_time)
        self._balance_heaps(max_heap, min_heap)

    def _balance_heaps(self, max_heap, min_heap):  # O(log(n))
        # make sure the len of max_heap is equal to or one more than min_heap
        # (1, 0), (0, 0) -> (2, 0), (0, 0), (1, 0), (0, 1)
        if len(max_heap) == len(min_heap) + 2:
            val = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -val)
        elif len(max_heap) + 1 == len(min_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)

    def query_median_transit_time(self, start_station, end_station):  # time O(1)
        # return a float number
        key = (start_station, end_station)
        if key not in self.trips:
            raise ValueError("input data record not found")
        max_heap, min_heap = self.trips[(start_station, end_station)]
        if not max_heap:
            raise ValueError("input data record not found")
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        else:
            return -max_heap[0]


"""
self.strips: {(s1, s3): [heap1, heap2]}
(s1, s3): [1, 2, 3, 4, 5, 4, 5]

max_heap [-1, -2, -3]  min_heap [4, 5, 6]
rule: len(max_heap) = len(min_heap) + (0, 1)
add: O(log(n))
query: O(1)

card  time  station
card1  1  s1
card2  2  s3
card1  2  s3
card2  3  s1

(s1, s3): 1
(s3, s1): 1
"""
