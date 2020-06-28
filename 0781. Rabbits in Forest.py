# time/space O(n)

import collections


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        res = 0
        d = collections.Counter(answers)
        for num, freq in d.items():
            group_size = num + 1
            n_color = 0
            if freq % group_size == 0:
                n_color = freq // group_size
            else:
                n_color = freq // group_size + 1
            res += n_color * group_size
        return res


"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many 
other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""
