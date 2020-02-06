


# method 1, time O(n), space O(n)
class Solution:
    def numSpecialEquivGroups(self, A):
        NGroup = 0 
        set1 = set(A)
        while set1:
            NGroup += 1
            ref = set1.pop()
            set2 = set()
            for item in set1:
                if self.isSpecialEquiv(ref, item):
                    set2.add(item)
            set1 = set1.difference(set2)
        return NGroup
    
    def isSpecialEquiv(self, str1, str2):
        if len(str1) != len(str2):
            return False
        if not str1:
            return True
        if self.isSpecialEquivHelper(0, str1, str2) \
            and self.isSpecialEquivHelper(1, str1, str2):
            return True
        else:
            return False
    
    def isSpecialEquivHelper(self, k, str1, str2):
        # k=0 for even index, k=1 for odd index
        # check even index
        d = {}
        for i in range(k, len(str1), 2):
            if str1[i] in d:
                d[str1[i]] += 1
            else:
                d[str1[i]] = 1
        for i in range(k, len(str2), 2):
            if str2[i] in d:
                d[str2[i]] -= 1
                if d[str2[i]] < 0:
                    return False
            else:
                return False
        return True


num = Solution().numSpecialEquivGroups( ["aa","bb","ab","ba"])
print(num)
