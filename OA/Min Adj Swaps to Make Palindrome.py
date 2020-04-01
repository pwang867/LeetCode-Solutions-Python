# cook your code here
from collections import defaultdict



# greedy approach, always choose one side to find the corresonding matched symbol
# time O(n^2), space O(1)


def is_palindrome(s):
    dict_s = defaultdict(int)
    for ch in s:
        dict_s[ch]+=1
    odd = 0
    for key in dict_s:
        if dict_s[key]%2 ==1:
            odd+=1
    return odd <=1

def min_swaps(s):
    if not s or len(s) == 1:
        return 0
    
    if not is_palindrome(s):
        return -1
    s_list = list(s)
    start = 0
    end = len(s)-1
    min_swaps = 0
    while start < end:
        if s_list[start] != s_list[end]:
            p2 = end
            while s_list[start] != s_list[p2]:
                p2 -=1
            if start == p2:
                s_list[p2], s_list[p2+1] = s_list[p2+1],s_list[p2]
                min_swaps+=1
            else:
                while p2 < end:
                    s_list[p2], s_list[p2+1] = s_list[p2+1],s_list[p2]
                    p2 +=1
                    min_swaps+=1
        else:
            start +=1
            end -=1
    return min_swaps

sss = "dmama"
swaps = min_swaps(sss.strip())
if swaps == -1:
    print("Impossible")
else:
    print(swaps)
