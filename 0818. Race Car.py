# time/space O(target*num_of_speed) = O(target*log(target))


import collections

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = collections.deque([(0, 1)])  # (pos, speed)
        visited = {(0, 1)}
        level = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos == target:
                    return level
                for pair in [(pos + speed, 2 * speed), (pos, -speed / abs(speed))]:
                    if pair not in visited and 0 <= pair[0] < target * 2:
                        visited.add(pair)
                        queue.append(pair)
            level += 1
        return level


"""
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input:
target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input:
target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
"""