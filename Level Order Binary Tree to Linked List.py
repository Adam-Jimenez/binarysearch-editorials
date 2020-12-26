"""
Level Order Binary Tree to Linked List

Breadth-first search, adding a node at the end of the linked list at each iteration.
"""
class Solution:
    def solve(self, root):
        q=[root]
        head=prev=None
        while q:
            node=q.pop(0)
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            if not head:
                head=prev=LLNode(node.val)
            else:
                prev.next=LLNode(node.val)
                prev=prev.next
        return head
