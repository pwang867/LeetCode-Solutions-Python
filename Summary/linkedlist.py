# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print_node(self):
        node = self
        while node:
            print(node.val)
            node = node.next
    
def list_to_linkedlist(nums):
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next

if __name__ == "__main__":
    print(ListNode(1) > ListNode(0))
    