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
    
    
