# method 2, use an arry of length 300
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = [0]*300
        self.times  = [0]*300
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        i = timestamp%300
        if self.times[i] != timestamp:
            self.counts[i] = 1
            self.times[i] = timestamp
        else:
            self.counts[i] += 1
        
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for i, time in enumerate(self.times):
            if self.times[i] > timestamp - 300:
                res += self.counts[i]
        return res


# method 1: use dictionary
class HitCounter1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = {}
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.counts[timestamp] = self.counts.get(timestamp, 0) + 1
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for time in range(timestamp, timestamp-300, -1):
            res += self.counts.get(time, 0)
        return res




# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)



"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""
