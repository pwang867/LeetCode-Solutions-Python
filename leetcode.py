class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        cur = (0, 0)
        visited = {(0, 0)}
        for c in path:
            if c == "N":
                cur = (cur[0], cur[1] + 1)
            elif c == "S":
                cur = (cur[0], cur[1] - 1)
            elif c == "E":
                cur = (cur[0] + 1, cur[1])
            elif c == "W":
                cur = (cur[0] - 1, cur[1])
            if cur in visited:
                return True
            else:
                visited.add(cur)
        return False



class Solution1(object):
    def divide_by_k(self, arr, k):
        counts = [0] * k
        for num in arr:
            counts[num % k] += 1
        for i in range(1, (k+1)//2):
            if counts[i] != counts[k-i]:
                return False
        if k%2 == 0:
            if counts[k//2] % 2 != 0:
                return False
        return True


class Solution(object):
    def divide_by_k(self):