# method 2, if ages[i] can only be inter.Counter(ages), and then iterate all of them
# time will be O(120*120), space is O(120)


import collections
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        d = collections.Counter(ages)
        
        cnt = 0
        for a, counta in d.items():
            for b, countb in d.items():
                if 0.5*a+7 < b <= a:  # we can actually get a > 14
                    if b == a:  # even if b==a, b > 0.5*a + 7 might still fail
                        cnt += counta*(counta-1)
                    else:
                        cnt += counta*countb
        return cnt
    

# method 1, general method if age could be floating point, 
# time n*log(n), space O(n)


class Solution1(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        cnt = 0
        for i, age in enumerate(ages):
            left = self.search(ages, 0.5*age+7)
            right = self.search(ages, age)
            cnt += max(right - left - 1, 0)
        return cnt
        
    
    def search(self, ages, target):
        # search the last index i such that ages[i] <= target
        left, right = 0, len(ages)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if ages[mid] <= target:
                left = mid
            else:
                right = mid
        if ages[right] <= target:
            return right
        elif ages[left] <= target:
            return left
        else:
            return -1


"""
Some people will make friend requests. 
The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) 
if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  
Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
"""
