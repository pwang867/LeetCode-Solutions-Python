'''

Suppose we have some input data describing a graph of relationships 
between parents and children over multiple generations. 
The data is formatted as a list of (parent, child) pairs,
 where each individual is assigned a unique integer identifier.

For example, in this diagram, the earliest ancestor of 6 is 14, 
and the earliest ancestor of 15 is 2. 

         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11

Write a function that, for a given individual in our dataset, 
returns their earliest known ancestor -- the one at the farthest distance 
from the input individual. If there is more than one ancestor tied for "earliest", 
return any one of them. If the input individual has no parents, 
the function should return null (or -1).

Sample input and output:

parentChildPairs3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

findEarliestAncestor(parentChildPairs3, 8) => 14
findEarliestAncestor(parentChildPairs3, 7) => 14
findEarliestAncestor(parentChildPairs3, 6) => 14
findEarliestAncestor(parentChildPairs3, 15) => 2
findEarliestAncestor(parentChildPairs3, 14) => null or -1
findEarliestAncestor(parentChildPairs3, 11) => 14

Additional example:

  14
  |
  2      4    1
  |    / | \ /
  3   5  8  9
 / \ / \     \
15  6   7    11

parentChildPairs4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]

findEarliestAncestor(parentChildPairs4, 8) => 4
findEarliestAncestor(parentChildPairs4, 7) => 4
findEarliestAncestor(parentChildPairs4, 6) => 14
findEarliestAncestor(parentChildPairs4, 15) => 14
findEarliestAncestor(parentChildPairs4, 14) => null or -1
findEarliestAncestor(parentChildPairs4, 11) => 4 or 1

n: number of pairs in the input

'''



from collections import defaultdict, deque

def findNodesWithZeroAndOneParents(parentChildPairs):
    parents = defaultdict(list)
    for u, v in parentChildPairs:
        parents[v].append(u)
        if u not in parents:
            parents[u] = []
    res = [[], []]   # zero, one
    for u, parent_list in parents.items():
        if len(parent_list) == 0:
            res[0].append(u)
        elif len(parent_list) == 1:
            res[1].append(u)
    return res





# print(findNodesWithZeroAndOneParents(parent_child_pairs))

def get_ancestor(parents, u):
    # a helper function using BFS
    res = set()
    queue = deque([u])
    while queue:
        node = queue.popleft()
        res.add(node)
        for v in parents[node]:
            queue.append(v)
    res.remove(u)
    return res


def hasCommonAncestor(parentChildPairs, node1, node2):
    parents = defaultdict(list)
    for u, v in parentChildPairs:
        parents[v].append(u)
        if u not in parents:
            parents[u] = []
    ancestors_u = get_ancestor(parents, node1)
    ancestors_v = get_ancestor(parents, node2)
    common_ancestors = ancestors_u & ancestors_v
    if common_ancestors:
        return True
    else:
        return False


parent_child_pairs_3 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

parent_child_pairs_4 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]


def findEarliestAncestor(parentChildPairs, target):
    parents = defaultdict(list)
    for u, v in parentChildPairs:
        parents[v].append(u)
        if u not in parents:
            parents[u] = []
    # using BFS
    if not parents[target]:
        return -1
    res = -1
    queue = deque([target])
    while queue:
        node = queue.popleft()
        res = node
        for v in parents[node]:
            queue.append(v)
    return res


for test_node in [8, 7, 6, 15, 14, 11]: # [8, 7, 6, 15, 14, 11]
    print(findEarliestAncestor(parent_child_pairs_4, test_node))


