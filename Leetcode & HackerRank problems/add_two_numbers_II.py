# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        A = []
        B = []
        while l1 != None:
            A.append(l1.val)
            l1 = l1.next
        while l2 != None:
            B.append(l2.val)
            l2 = l2.next
        A = A[::-1]
        B = B[::-1]
        C = []
        p = 0
        for i in range(max(len(A),len(B))):
            if i >= len(A): x = 0
            else: x = A[i]
            if i >= len(B): y = 0
            else: y = B[i]
            
            z = x+y+p
            if (p != 0): p = p-1
            if (z > 9):
                z = z-10
                p = p+1
            C.append(z)
        if p == 1: C.append(1)
        C = C[::-1]
        L3 = ListNode(-1)
        res = L3
        for x in C:
            L3.next = ListNode(x)
            L3 = L3.next
        return res.next        