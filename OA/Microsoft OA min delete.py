
# method 2, similar to longest increasing subsequence
# time O(n), space O(1)

def min_delete2(s):
    cntA, cntB = 0, 0
    for c in s:
        if c == "A":
            if cntB > 0:
                cntB -= 1
            cntA += 1
        else:
            cntB += 1
    return len(s) - (cntA + cntB)



# method 1, two pointers, time O(n), two pass

def min_delete1(s):
    totalA = s.count('A')
    min_del = len(s)
    cntA, cntB = 0, 0
    for c in s:    # assume current position already has all the 'A'
        if c == "A":
            cntA += 1
        else:
            cntB += 1
        min_del = min(min_del, cntB + totalA - cntA)
    return min_del
    

for s in ["BAAABAB", "BBABAA", "AABBBB"]:
    print(min_delete2(s))
    print(min_delete1(s))

