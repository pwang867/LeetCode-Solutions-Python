# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# use a flag to indicate whether the component is discontinued or not
# do not forget to check the flag again after the while loop
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        numCom = 0
        flag = False
        
        while head:
            if head.val in G:
                if not flag:
                    flag = True
            else:
                if flag:
                    numCom += 1
                    flag = False
            head = head.next
        
        if flag:  # check again
            numCom += 1
        return numCom
    
