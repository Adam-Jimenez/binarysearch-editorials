"""
Interleaved Linked List

We can pair corresponding elements in l0 and l1 using zip_longest and a generator, consecutively adding the current node to the new linked list.
"""
from itertools import zip_longest
class Solution:
    def solve(self, l0, l1):
        head=prev=LLNode(0)
        for x,y in zip_longest(it(l0),it(l1), fillvalue=None):
            for z in (x,y):
                if z: prev.next = LLNode(z.val); prev=prev.next
        return head.next
def it(node):
    while node:
        yield node
        node=node.next
