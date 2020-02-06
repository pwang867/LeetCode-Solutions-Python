from collections import defaultdict
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        debts = defaultdict(int)
        for x, y, z in transactions:
            debts[x] += z
            debts[y] -= z
        positives, negatives = [], []
        for key, val in debts.items():
            if val > 0:
                positives.append(val)
            elif val < 0:
                negatives.append(val)
        
        self.res = float('inf')
        self.dfs(positives, negatives, 0)
        return self.res
    
    def dfs(self, positives, negatives, ntransfer):
        if ntransfer > self.res:  # early termination 1
            return
        if not positives:
            self.res = min(self.res, ntransfer)
            return
        
        positive = positives.pop()
        if -positive in negatives:   # early termination 2, [5 and -5 should cancel]
            negatives.remove(-positive)
            self.dfs(positives, negatives, ntransfer+1)
            return
        
        for i, negative in enumerate(negatives):
            total = positive + negative
            if total > 0:
                self.dfs(positives+[total], negatives[:i]+negatives[i+1:], ntransfer+1)
            elif total < 0:
                self.dfs(positives+[], negatives[:i]+[total]+negatives[i+1:], ntransfer+1)
            else:
                self.dfs(positives+[], negatives[:i]+negatives[i+1:], ntransfer+1)


"""
A group of friends went on holiday and sometimes 
lent each other money. For example, Alice paid for Bill's lunch for $10. 
Then later Chris gave Alice $5 for a taxi ride. 
We can model each transaction as a tuple (x, y, z) 
which means person x gave person y $z. 
Assuming Alice, Bill, and Chris are person 0, 1, and 2 
respectively (0, 1, 2 are the person's ID), 
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, 
return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). 
Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 
or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 
pays person #0 and #2 $5 each.
"""

