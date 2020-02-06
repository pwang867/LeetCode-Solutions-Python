# e = 1 + 1/2! + 1/3! + ... + 1/n! + ...

n = 1000
total = 2
cur = 1.0
for i in range(2, n+1):
    cur = cur/i
    total += cur

print(total)
