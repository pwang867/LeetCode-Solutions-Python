"""
Finding all pairs of elements (say, a and b) from elements in an array such that a & b is 0.

input: {1, 2, 6, 9, 3}
output: [6,9],[1,2],[2,9],[1,6]
"""
# wrong solution


# time complexity O(n*min(c, log(n))) where c = log(max_number), n=len(data_set)
# space O(n)
# divide and conquer, we divide using the k-th digit, separate 0 from 1
def pairs(data_set):
    # numbers inside data_set >= 0
    res = []
    if 0 in data_set:
        data_set.remove(0)
        add_res([0], data_set, res)
    
    temp = partition(data_set, 1)
    pairHelper(temp[1], temp[2], 2, res)
    return res

def add_res(nums1, nums2, res):
    for x in nums1:
        for y in nums2:
            res.append([x, y])

def pairHelper(nums1, nums2, bit, res):
    if not nums1 or not nums2:
        return
    # partition using k-th digit(bit=2**k)
    groups1 = partition(nums1, bit)
    groups2 = partition(nums2, bit)
    # save results
    add_res(groups1[0], nums2, res)
    add_res(groups1[1], groups2[0], res)
    add_res(groups1[2], groups2[0], res)
    # recursion
    pairHelper(groups1[1], groups2[2], bit*2, res)
    pairHelper(groups1[2], groups2[1], bit*2, res)

def partition(data_set, bit):
    # ref == 2**k
    # split the data_set into three parts: (< 2**k), k-th digit = 1, k-th digit = 0     
    res = [[],[],[]]
    for num in data_set:
        if num < bit:
            res[0].append(num)
        elif num & bit == bit:
            res[1].append(num)
        else:
            res[2].append(num)
    return res


from time import time
start = time()
#data_set = {1, 2, 6, 9, 3}
#data_set = set(range(100000))
#pairs(data_set)
total = 0
for x in range(10000):
    for y in range(10000):
        total = x + y
print("time elapsed: {} s".format(time()-start))

