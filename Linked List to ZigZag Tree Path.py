"""
Linked List to ZigZag Tree Path

Recursive solution: We set current node as root, and check the next node to see if its smaller and set it as the correct child. Recursively solve for the next nodes.
"""
class Solution:
    def solve(self, node):
        if not node: return None
        root=Tree(node.val)
        if node.next:
            if node.next.val<node.val:
               root.left = self.solve(node.next)
            else:
               root.right = self.solve(node.next)
        return root
