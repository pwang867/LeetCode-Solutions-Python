# greedy
# edge case: gas = [2,2,2,2,2,2,4,1,1,1], cost = [1,1,1,1,1,1,1,5,4,3], should not start from i=6
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        best_start = 0
        total = 0
        tank = 0
        for i in range(n):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            # wrong greedy: start from the maximum gas[i]-cost[i]
            # if gas[i] - cost[i] > gas[best_start] - cost[best_start]:  
            #     best_start = i
            if tank < 0:
                best_start = i + 1   # correct greedy
                tank = 0
        if total < 0:
            return -1
        else:
            return best_start


"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""
