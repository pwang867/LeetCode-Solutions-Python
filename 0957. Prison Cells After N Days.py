# There must be a cycle, so use a while loop to find the cycle
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        day = 0
        period = 0
        start = 0  # cycle start day, cycle doesn't always start from day 0
        appeared_states = {}
        
        while True:
            if N == day:  # early termination
                return cells
            key = tuple(cells)  # list can not be used as dictionary keys, but tuple can
            if key in appeared_states:
                start = appeared_states[key]  
                period = day - start
                break
            appeared_states[key] = day
            cells = self.states_next_day(cells)
            day += 1
            
        if (N-(start-1))%period != 0:
            N = start - 1 + (N-(start-1))%period 
        else:
            N = start - 1 + period  # easy for mistake
        
        for key, value in appeared_states.items():
            if value == N:
                return list(key)
    
    def states_next_day(self, cells):
        new_cells = [0]*len(cells)
        for i in range(1, len(cells)-1):
            new_cells[i] = int(not (cells[i-1] ^ cells[i+1]))  # use XOR
        return new_cells
    
    
"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""
