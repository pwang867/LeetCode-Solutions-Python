'''
Databricks phone interview


binary tree
extra pointer to parent

constant space O(1)

Morris Traversal

    1
   / \
  2   5
 / \
3   4

post order,

three pointers:
1. end: the end of virtual stack
2. left_process: if the left of the end is processed
3. record the last node processed: pre


end: 1->2->3->2->4->2->1->5
left_process: False->True->False->True->False
pre: 3, 4, 2
res: 3, 4, 2


initialize left_process to False

# root's parent is None
while end:
   if left_process is False and left child exists:
        end = node.left
   else:
        # check right
        if right is pre or None:
            process node
            pre = node
            end = end.parent
            left_process = True
        else:
            move end to right
            left_process = False

'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def postorder1(root):
    '''
    post order traversal using constant space
    '''
    end = root  # simulating a stack using a single pointer
    left_process = False   # if the left child of end is processed
    pre = None   # record the last processed node
    
    while end:   # root's parent is None
        if left_process is False and end.left:
            end = end.left
        else:
            # check right
            if end.right is pre or end.right is None: 
                print(end.val)
                pre = end
                end = end.parent
                left_process = True
            else:
                end = end.right
                left_process = False

def postorder(root):
    '''
    post order traversal using constant space
    '''
    p = root     # current pointer
    stack = None # the path from root to p
    pre = None   # record the last processed node
    
    while p or stack:   # root's parent is None
        if p:
            stack = p
            p = p.left
        else:
            # check right
            if stack.right is pre or stack.right is None: 
                print(stack.val)
                pre = stack
                stack = stack.parent
                p = None
            else:
                p = stack.right


root = Node(1)
node2 = Node(2)
root.left = node2
node2.parent = root

node3 = Node(3)
node3.parent = node2
node2.left = node3

node4 = Node(4)
node4.parent = node2
node2.right = node4

node5 = Node(5)
node5.parent = root
root.right = node5

postorder1(root)
