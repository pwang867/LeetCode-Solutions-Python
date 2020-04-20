class Solution:
    def __init__(self):
        pass

    def find_furthest(self, points, m, n):
        if not (0 <= m <= n <= len(points)):
            raise ValueError("Input index out of bound")
        arr = [[self.dist(point), point[0], point[1]] for point in points]
        self.quick_selection(arr, 0, len(arr)-1, n)
        self.quick_selection(arr, 0, n-1, m)
        return [[x[1], x[2]] for x in arr[m-1:n]]

    def quick_selection(self, arr, left, right, k):
        # arrange top k furthest points in the front of points inplace between left and right
        if left >= right:
            return
        mid = self.partition(arr, left, right)
        if mid - left + 1 == k:
            return
        elif mid - left + 1 > k:
            self.quick_selection(arr, left, mid, k)
        else:
            self.quick_selection(arr, mid+1, right, k-(mid-left+1))

    def partition(self, arr, left, right):
        if left > right:
            return -1
        start, end = left, right-1
        while start <= end:
            if arr[start] <= arr[right]:
                print(start, right,arr)
                start += 1
            elif arr[end] > arr[right]:
                end -= 1
            else:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        arr[end], arr[right] = arr[right], arr[end]
        return end


    def dist(self, point):
        return abs(point[0]) + abs(point[1])


points = [[3,3],[-2,4],[5,-1]]
m = 1
n = 3
Solution().find_furthest(points, m, n)

"""
tasks = ["A","A","A","B","B","B"], n = 2

A, B, idle, A, B, idle, A, B 

A, B, idle , A
B, _, _, B
computer task
interval has same time?
A, B, C, D...


["A","A","A","B","B","B", 'C', 'C', 'D'], n = 2
A B C    A B C     A B  D    A
n + 1
[[A,B C]      [A, B, D],        [A, B, idle],        [A]]

n+1

A: 4
E: 4
B: 3
C: 2
D: 1

return sequence for task: [task]

O(res)

"""

import collections


class Solution:
    def task_scheduler(self, tasks, n):
        if n < 0:
            raise ValueError("n >= 1")
        if n == 0:
            return tasks

        cnts = collections.Counter(tasks)  # {'A': cnt 4}
        max_cnt = max(cnts.values())

        if max_cnt == 1:
            return tasks

        res = [[] for _ in range(max_cnt)]

        # take care highest counts of tasks
        for task, val in cnts.items():
            if val == max_cnt:
                for i in range(len(res)):
                    res[i].append(task)

        # take care of other tasks with smaller freqency
        cur = 0  # round robin over max_cnt-1
        for task, val in cnts.items():
            if val != max_cnt:
                for i in range(val):
                    res[cur].append(task)
                    cur = (cur + 1) % (max_cnt - 1)  # check max_cnt == 1

        # insert "idle", n+1 for each group
        for i in range(len(res) - 1):
            if len(res[i]) < n + 1:
                res[i].extend(["idle"] * (n + 1 - len(res[i])))

        return "".join(map("".join, res))


# tasks = ["A"]
# n = 2
# print(Solution().task_scheduler(tasks, n))


"""
s = "()())()"

s = "()()()"
"(())()"

"(", "("

left_cnt = 0
right_cnt = 1

2^(left_cnt+right_cnt) = 2^1

minimum removal

1. find min removal for "(" and ")", stack O(n)
2. dfs to find it, O(res)

"()("
[(, )](
left_del = 1

"""


class Solution2:
    def get_valid_brackets(self, s):
        left_del, right_del, n = self.get_invalid_cnts(s)
        res = set()
        path = []
        self.dfs(s, 0, left_del, right_del, 0, 0, path, res, n)
        return list(res)

    def dfs(self, s, i, left_del, right_del, left, right, path, res, n):

        if i == len(s):
            # add to res whenever valid
            # if left_del == 0 and right_del == 0 and left == n and right == n:
            res.add("".join(path))
            return

        if s[i] == "(":
            if left + 1 <= n:
                self.dfs(s, i + 1, left_del, right_del, left + 1, right, path + ["("], res, n)
            if left_del > 0:
                self.dfs(s, i + 1, left_del - 1, right_del, left, right, path, res, n)
        else:
            # ["(", ")",
            if left > right:
                self.dfs(s, i + 1, left_del, right_del, left, right + 1, path + [")"], res, n)
            if right_del > 0:
                self.dfs(s, i + 1, left_del, right_del - 1, left, right, path, res, n)

    def get_invalid_cnts(self, s):
        left_cnt, right_cnt = 0, 0
        for i, c in enumerate(s):
            if c == "(":
                left_cnt += 1
            elif c == ")":
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    right_cnt += 1
        return left_cnt, right_cnt, (len(s) - left_cnt - right_cnt) // 2


s = "(()(()"
print(Solution2().get_valid_brackets(s))
