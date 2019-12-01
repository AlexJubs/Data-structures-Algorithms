# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, L1, L2):
        L3 = ListNode(-1)
        res = L3
        while (L1 != None or L2 != None):
            if L2 == None:
                L3.next = L1
                L3 = L3.next
                L1 = L1.next
            elif L1 == None:
                L3.next = L2
                L3 = L3.next
                L2 = L2.next
            elif L2.val <= L1.val:
                L3.next = L2
                L3 = L3.next
                L2 = L2.next
            else:
                L3.next = L1
                L3 = L3.next
                L1 = L1.next
        return res.next
        
    def sortList(self, head: ListNode) -> ListNode:
        if head == None: return None
        if head.next == None: return head
        p1 = head
        p2 = head
        p1_prev = p1
        while True:
            if p2 == None or p2.next == None: break
            p1_prev = p1
            p1 = p1.next
            p2 = p2.next.next
        p2 = head
        p1_prev.next = None
        return self.merge(self.sortList(p1), self.sortList(p2))
