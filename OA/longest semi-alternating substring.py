# sliding window, time O(n), space O(1)

def longest_semi(s):
    max_len = 0
    left = 0
    for right in range(len(s)):
        if right - left + 1 >= 3 and s[right] == s[right-1] == s[right-2]:
            left = right - 1
        max_len = max(max_len, right-left+1)
    return max_len

for s in ["baaabbabbb", 'babba', 'abaaaa']:
    print(longest_semi(s))
    