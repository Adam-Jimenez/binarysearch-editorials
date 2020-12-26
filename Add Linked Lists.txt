"""
Add Linked Lists

We can use a generator to easily iterate over the linked lists, and zip_longest to match corresponding values. If one linked list is longer than the other, zip_longest will use the fillvalue (0 in this case, which won't affect the sum).
"""
from itertools import zip_longest
class Solution:
    def solve(self, l0, l1):
        head=pre=LLNode(0)
        carry = 0
        for x,y in zip_longest(it(l0), it(l1), fillvalue=0):
            carry, res = divmod(x+y+carry, 10)
            pre.next = LLNode(res)
            pre=pre.next
        if carry: pre.next = LLNode(carry)
        return head.next
        
def it(node):
    while node:
        yield node.val
        node=node.next