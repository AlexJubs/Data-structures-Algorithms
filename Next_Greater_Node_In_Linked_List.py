# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None: return None
        if head.next == None: return [0]
        res = list()
        stk = list()
        index = 0
        
        while head != None:
            res.append(0)
            
            while stk != [] and stk[-1][0] < head.val:
                res[stk.pop()[1]] = head.val
            
            stk.append((head.val, index))
            index = index+1
            head = head.next
        
        return res
