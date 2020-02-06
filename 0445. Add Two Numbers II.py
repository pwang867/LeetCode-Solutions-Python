# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 2: backtracking
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        len1, len2 = self.getLen(l1), self.getLen(l2)
        if len1 < len2:  # make l1 as the longer list
            l1, l2 = l2, l1
        node = self.addHelper(l1, l2, abs(len1-len2))  # mistake: not len1 - len2
        if not node:
            return 0
        elif node.val < 10:
            return node
        else:
            node.val = node.val%10
            dummy = ListNode(1)
            dummy.next = node
            return dummy
        
    def getLen(self, head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt
    
    def addHelper(self, l1, l2, diff):
        if not l2:
            return l1
        if not l1:
            return None
        
        if diff == 0:
            cur = ListNode(l1.val + l2.val)
            node = self.addHelper(l1.next, l2.next, 0)
        else:
            cur = ListNode(l1.val)
            node = self.addHelper(l1.next, l2, diff - 1)
        
        if node and node.val > 9:
            node.val %= 10
            cur.val += 1
        
        cur.next = node
        return cur
    



# method 1: 
# for example, [4, 9, 9, 9, 12], one pointer stays at 4, 
# which is followed by consecutive 9's, once we see 12, 
# we change 4 to 5, and all 9's to 0's, and 12 to 2
class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # empty
        if not l1:
            return l2
        if not l2:
            return l1
        
        # line up two linked list
        p1 = l1
        p2 = l2
        cnt = 0
        head = ListNode(0)
        while True:
            if p1.next == None:
                cnt += 1
                p1 = l2
                head = l1
            else:
                p1 = p1.next
            if p2.next == None:
                cnt += 1
                p2 = l1
                head = l2
            else:
                p2 = p2.next
            if cnt == 2:
                break
        print "test1", p1.val, p2.val
        
        # Up to now, p1 points to p2 and p2 points to p1
        # make p2 points to the longer linked list
        if head == l2:
            p1, p2 = p2, p1

        # add two linked list
        while p2:
            p2.val = p2.val + p1.val
            p2 = p2.next
            p1 = p1.next
            
        # deal with vals that vals > 9
        copy = ListNode(0)
        copy.next = head
        curr = head
        nine = copy
        while curr:
            if curr.val > 9:
                nine.val += 1
                while nine.next.val == 9:  # change all continuous 9's to 0
                    nine.next.val = 0
                    nine = nine.next
                curr.val = curr.val%10
            if curr.val < 9:
                nine = curr
            curr = curr.next
        
        # check if the added copy is 0 or 1
        if copy.val == 0:
            return copy.next
        else:
            return copy
        
            
