# Microsoft OA, Max Possible Value

def maxPossibleValue(x):
    if x == 0:
        return 50
    sign = 1 if x > 0 else -1
    x = abs(x)
    s = map(int, list(str(x)))
    for i in range(len(s)):
        if s[i]*sign < 5*sign:
            s = s[:i] + [5] + s[i:]
            break
    else:
        s.append(5)
    res = 0
    for x in s:
        res = res*10 + x
    return res*sign


for x in [268, 670, 0, -999]:
    print(maxPossibleValue(x))

