# greedy, time O(n), space O(1)

def minMove(s):
    cnt = 0
    i = 0
    while i < len(s):
        m = 1
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i+1]:
                m += 1
                i += 1
            else:
                break
        cnt += m//3
        i += 1
    return cnt

print(minMove("baaabbaabbba"))

