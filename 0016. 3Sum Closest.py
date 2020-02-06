# edge case: [-10,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3], target=8
class Solution1(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # check input
        if len(nums) < 3:
            raise ValueError
        
        # sort
        nums.sort()
        
        # iteration
        # skip consecutive same numbers
        # stop when smallest triple is > target/3
        res = float("inf")
        diff = float("inf")
        for i in range(len(nums)-2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # early termination
            if nums[i] > target/3.0: # mistake, directly return: return res 
                if nums[i]+nums[i+1]+nums[i+2] - target < diff:
                    return nums[i]+nums[i+1]+nums[i+2]    
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                # update res
                if abs(_sum - target) < diff:
                    diff = abs(_sum - target)
                    res = _sum
                    
                # # skipping duplicates is tricky here, though you don't have to
                #  edge case: [-1,0,1,1,55], target=3
                while left + 2 < right and nums[left] == nums[left + 2]:  # +2
                    left += 1  # +1
                while left + 2 < right and nums[right] == nums[right - 2]:
                    right -= 1
                
                # move pointer regularly
                if _sum == target:
                    return target
                elif _sum > target:
                    right -= 1
                else:
                    left += 1
        
        return res
    

# simplified version 
# edge case: [-10,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3], target=8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # check input
        if len(nums) < 3:
            return None
        
        nums.sort()
        
        res = float("inf")
        diff = float("inf")
        for i in range(len(nums)-2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                # update res
                if abs(_sum - target) < diff:
                    diff = abs(_sum - target)
                    res = _sum
                # move pointer regularly
                if _sum == target:
                    return target
                elif _sum > target:
                    right -= 1
                else:
                    left += 1
        
        return res

