# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        p1 = head
        p2 = head
        while True:
            if p2 == None or p2.next == None: break
            p1 = p1.next
            p2 = p2.next.next
        return p1
    
