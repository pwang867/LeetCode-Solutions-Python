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
    

"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
