# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        counter = 0
        res = 0
        num = list()
        while head != None:
            if head.val == 1: num.append(counter)
            head = head.next
            counter = counter+1
        counter = counter-1
        for x in num:
            res = res + 2**(counter-x)
        return res
