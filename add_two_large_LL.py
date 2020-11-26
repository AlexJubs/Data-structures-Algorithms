# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    if (a == None and b == None): return None
    a = reverse_LL(a)
    b = reverse_LL(b)
    c = ListNode(0)
    res = c
    carry = 0
    while (a != None or b != None):
        if (a == None): x = 0
        else: x = a.value
        if (b == None): y = 0
        else: y = b.value
        sum = x+y+carry
        if (sum < 10000):
            c.next = ListNode(sum)
            carry = 0
        elif (sum >= 10000):
            c.next = ListNode(sum-10000)
            carry = 1
        c = c.next
        if (a != None): a = a.next
        if (b != None): b = b.next
        
    if carry == 1: c.next = ListNode(1)
    return reverse_LL(res.next)
    
def reverse_LL(head):
    if (head == None or head.next == None): return head
    pointers = list()
    res = head
    while head != None:
        pointers.append(head)
        head = head.next
    p1 = 0
    p2 = len(pointers)-1
    while (p1 < p2):
        pointers[p1].value, pointers[p2].value = pointers[p2].value, pointers[p1].value
        p1 += 1
        p2 -= 1
    return res
