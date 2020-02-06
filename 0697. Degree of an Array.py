# use a dictionary to store the start and end index, 
# and the counts for every num
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}  # {num:[cnt, start, end]}
        
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [1, i, i]
            else:
                temp = d[num]
                temp[0] += 1
                temp[2] = i
        
        candidate = -1
        degree = 0
        
        for num in d:
            if d[num][0] > degree:
                degree = d[num][0]
                candidate = num
            elif d[num][0] == degree:
                if d[num][2]-d[num][1] + 1 < d[candidate][2]-d[candidate][1]+1:
                    candidate = num
        
        return d[candidate][2] - d[candidate][1] + 1
    
