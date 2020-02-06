"""
problem: Count pairs in a sorted array whose sum is less than x

https://www.geeksforgeeks.org/count-pairs-array-whose-sum-less-x/
"""

# time O(n*log(n)), space O(1)
def sum_less_than_k(nums, k):
    cnt = 0
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[right] + nums[left] >= k:
            right -= 1
        else:
            cnt = right - left  # 比当前right小的跟当前的left结合全满足 < k
            left += 1
    return cnt


print sum_less_than_k([1,2,3,4], 2)
print sum_less_than_k([1,2,3,4], 4)
print sum_less_than_k([1,2,3,4], 5)

