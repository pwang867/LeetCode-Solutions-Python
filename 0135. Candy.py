
# another O(n) one pass greedy: https://leetcode.com/problems/candy/discuss/135698/Simple-solution-with-one-pass-using-O(1)-space


# greedy, process children from low rating to high rating
# time O(n*log(n)), space O(n)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        
        arr = [(val, i) for i, val in enumerate(ratings)]
        arr.sort()
        candy = [1]*len(ratings)
        
        for val, i in arr:
            if i > 0 and ratings[i-1] < ratings[i]:
                candy[i] = max(candy[i-1]+1, candy[i])
            if i < len(ratings)-1 and ratings[i+1] < ratings[i]:
                candy[i] = max(candy[i+1]+1, candy[i])
        
        return sum(candy)



"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""
