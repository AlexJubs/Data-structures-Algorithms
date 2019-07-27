# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
keep 2 hashsets, 1 for headA (sA) and 1 for headB (sB). as we traverse, we add to these hashsets. every time we move the pointers up, we check if p1 is in sB and if p2 is in sA. if both p1 and p2 are null at the end of the traversal, then we return NULL
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if (headA == None or headB == None): return None
        p1, p2 = headA, headB
        A, B = set(), set()
        while (p1 != None or p2 != None):
            if (p1 == p2): return p1
            if (p1 in B): return p1
            if (p2 != None):
                if (p2 in A): return p2
                B.add(p2)
                p2 = p2.next
                
            if (p1 != None):
                if (p1 in B): return p1
                A.add(p1)
                p1 = p1.next
        return None