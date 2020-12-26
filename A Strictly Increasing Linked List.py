"""
A Strictly Increasing Linked List

We can look ahead to validate the constraints.           
"""
class Solution:
    def solve(self, node):
        while node.next:
            if node.val>=node.next.val: return False
            node=node.next
        return True