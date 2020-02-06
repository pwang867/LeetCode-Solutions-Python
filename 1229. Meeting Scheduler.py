class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] < slots2[j][0]:
                i += 1
            elif slots1[i][0] > slots2[j][1]:
                j += 1
            else:
                end = min(slots1[i][1], slots2[j][1])
                start = max(slots1[i][0], slots2[j][0])
                if end - start >= duration:
                    return [start, start+duration]
                if slots1[i][1] < slots2[j][1]:  # easy to forget !!! dead loop !!!
                    i += 1
                else:
                    j += 1
        return []

slots1 = [[10,50],[60,120],[140,210]]
slots2 =  [[0,15],[60,70]]
duration = 11
print(Solution().minAvailableDuration(slots1, slots2, duration))

