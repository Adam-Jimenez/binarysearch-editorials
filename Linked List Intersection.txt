"""
Linked List Intersection

I didn't read the problem so I didn't know the linked lists were already sorted, so I just shoved everything into a set and made a new linked list.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        s=list(sorted(set(map(val, it(l0)))&set(map(val, it(l1)))))
        head=prev=LLNode(None)
        for v in s:
            prev.next=LLNode(v)
            prev=prev.next
        return head.next
        
def val(n):
    return n.val
    
def it(n):
    while n:
        yield n
        n=n.next
