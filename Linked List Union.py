"""
Linked List Union

The lazy way is the best way, don't let anyone tell you otherwise.
"""
class Solution:
    def solve(self, ll0, ll1):
        s=set(it(ll0))|set(it(ll1))
        head=prev=LLNode(None)
        for x in sorted(s):
            prev.next=LLNode(x)
            prev=prev.next
        return head.next
    
def it(n):
    while n:
        yield n.val
        n=n.next
