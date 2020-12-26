"""
Linked List Delete Last Occurrence of Value

A neat single-pass trick to solving this problem is keeping a reference to the last seen target. We start before the list and always check if the next value is the target, so we have a reference to the previous node. This way, we can easily update the references.
"""
class Solution:
    def solve(self, node, target):
        front=cur=LLNode(None,node)
        ref=None
        while cur.next:
            if cur.next.val==target: ref=cur
            cur=cur.next
        if ref:
            ref.next=ref.next.next
        return front.next
