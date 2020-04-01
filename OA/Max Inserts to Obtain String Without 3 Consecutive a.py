# Microsoft OA


def max_insert(s):
    cnt = 0
    left = -1
    for right in range(len(s)):
        if s[right] != 'a':
            if right - left - 1 >= 3:
                return -1
            else:
                cnt += 2 - (right-left-1)
            left = right
    tail = s[left+1:]    # easy to forget the last few letters
    if len(tail) >= 3:
        return -1
    else:
        return cnt + 2 - len(tail)
    

for s in ["aabab", 'dog', 'aa', 'baaaa']:
    print(max_insert(s))
    