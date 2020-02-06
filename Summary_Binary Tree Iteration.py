def preorder(root):
    res = []
    
    stack = []
    p = root
    while stack or p:
        if p:
            # process p first
            res.append(p.val)
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            p = p.right
    
    return res

def inorder(root):
    res = []
    
    stack = []
    p = root
    while stack or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            # process p 
            res.append(p.val)
            p = p.right
    
    return res

def postorder(root):
    res = []
    
    stack = []
    p = root
    pre = None  # last processed node
    while stack or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack[-1]  # a node in stack will be peeked twice
            p = p.right
            
            # process stack top node in the second visit
            if p is None or p is pre:  
                p = stack.pop()
                res.append(p.val)
                pre = p
                p = None
    
    return res

def levelorder(self, root):
    if not root:
        return []
    
    res = []
    
    level = [root]  # or use deque()
    while level:
        vals = [node.val for node in level]
        res.append(vals)
        level = [child for node in level \
                 for child in [node.left, node.right] if child]

    return res
