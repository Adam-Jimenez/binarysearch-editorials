"""
Reverse a Linked List

The trick is to keep a reference to the previous node and set it as next after saving the next node in the list.
"""
class Solution:
    def solve(self, node):
        prev=None
        cur=node
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
