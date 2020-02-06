nums = [4,3,1,2,4,5,3]
left, cur, right = 0, 0, len(nums)-1

pivot = nums[4]
while cur <= right:
    if nums[cur] < pivot:
        nums[left], nums[cur] = nums[cur], nums[left]
        left += 1
        cur += 1
    elif nums[cur] > pivot:
        nums[right], nums[cur] = nums[cur], nums[right]
        right -= 1
    else:
        cur += 1

print(nums, left, right)
