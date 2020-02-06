# time O(n+m*log(m)), n = len(hand), m = len(d)
from collections import defaultdict
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if not hand:
            return False
        d = defaultdict(int)
        for num in hand:
            d[num] += 1
        if len(d) < W:
            return False
        cards = d.keys()
        cards.sort()
        for i in range(len(cards)-W+1):
            cnt = d[cards[i]]
            if cnt == 0:   # important
                continue
            for j in range(i, i+W):
                if j > i and cards[j] - cards[j-1] != 1:   # easy to forget
                    return False
                d[cards[j]] -= cnt   # mistake: d[cards[j]] -= cnt
                if d[cards[j]] < 0:
                    return False
        for i in range(len(cards)-W+1, len(cards)):
            if d[cards[i]] != 0:
                return False
                
        return True


"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
