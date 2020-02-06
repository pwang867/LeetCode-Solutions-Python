class SnapshotArray(object):

    def __init__(self, length):   # save changes by set() only, don't have to copy array for every snap
        """
        :type length: int
        """
        self.snap_id = -1
        self.nums = [[[-1, 0]] for i in range(length)]
        

    def set(self, index, val):  # O(1)
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.snap_id == self.nums[index][-1][0]:
            self.nums[index][-1][1] = val
        else:
            self.nums[index].append([self.snap_id, val])
        

    def snap(self):  # O(1)
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id
        

    def get(self, index, snap_id):  # binary search, O(log(n)), n is the counts we set value for index
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # find the first id < snap_id
        arr = self.nums[index]
        left, right = 0, len(arr)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if arr[mid][0] < snap_id:
                left = mid
            else:
                right = mid
        if arr[right][0] < snap_id:
            return arr[right][1]
        else:
            return arr[left][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""
