def walk(r, k, val, target, path, visited, glo_visited):
    if (r, k) in visited:
        return False
    if (r, k, target) in glo_visited:
        return False
    if len(path) > 500:
        return False
    if target == 0:
        return True
    if target < 0:
        return False
    glo_visited.add((r, k, target))
    path.append((r, k))
    visited.add((r, k))
    target -= val
    for i, pos in enumerate([(r-1, k-1), (r-1, k), (r, k-1),
    (r, k+1), (r+1, k), (r+1, k+1)]):
        x, y = pos
        if x >= 1 and 1 <= y <= x and (x, y) not in visited:
            if i == 0:
                new_val = val*(k-1)/(r-1)
            elif i == 1:
                new_val = val*(r-k)/(r-1)
            elif i == 2:
                new_val = val*(k-1)/(r-k+1)
            elif i == 3:
                new_val = val*(r-k)/k
            elif i == 4:
                new_val = val*r/(r-k+1)
            else:
                new_val = val*r/k
            if walk(x, y, new_val, target, path, visited, glo_visited):
                return True
    path.pop()
    visited.remove((r, k))
    return False


for N in [10**9]:
    path = []
    walk(1, 1, 1, N, path, set(), set())
    print(path)
