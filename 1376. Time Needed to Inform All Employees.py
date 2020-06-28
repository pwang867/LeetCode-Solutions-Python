# method 2, BFS traversal, time/space O(n)

import collections


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # build Tree
        tree = collections.defaultdict(list)
        for child_id, parent_id in enumerate(manager):
            tree[parent_id].append(child_id)
        # BFS
        queue = collections.deque([(tree[-1][0], 0)])
        max_time = 0
        while queue:
            id, time = queue.popleft()
            max_time = max(max_time, time)
            for child_id in tree[id]:
                queue.append((child_id, time + informTime[id]))
        return max_time


# method 1, build a manager tree first, then DFS


class TreeNode:
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.children = []


class Solution1(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        root = self.build_tree(headID, manager, informTime)
        return self.get_max_time(root)

    def build_tree(self, headID, manager, informTime):
        nodes = {}
        for id, time in enumerate(informTime):
            nodes[id] = TreeNode(id, time)
        root = nodes[headID]
        for child_id, manager_id in enumerate(manager):
            if manager_id == -1:
                continue
            else:
                nodes[manager_id].children.append(nodes[child_id])
        return root

    def get_max_time(self, root):
        if not root or (not root.children):
            return 0
        times = [self.get_max_time(child) for child in root.children]
        return max(times) + root.time


# method 3, O(1) space, but O(n^2) time, TLE


class Solution3(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """

        def get_time_for(id):
            time = 0
            while manager[id] != -1:
                manager_id = manager[id]
                time += informTime[manager_id]
                id = manager_id
            return time

        max_time = 0
        for id in range(n):
            cur_time = get_time_for(id)
            max_time = max(max_time, cur_time)
        return max_time


"""
A company has n employees with a unique ID for each employee from 0 to n - 1. 
The head of the company has is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] 
is the direct manager of the i-th employee, manager[headID] = -1. 
Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. 
He will inform his direct subordinates and they will inform their subordinates and so on until all employees 
know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After informTime[i] minutes, 
all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company 
and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
Example 3:


Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.
Example 4:

Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.
Example 5:

Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076
 

Constraints:

1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
