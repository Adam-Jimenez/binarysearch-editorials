"""
Palindromic Tree

All values in order should equal values iterated in reverse order.
"""
class Solution:
    def solve(self, root):
        return all(x==y for x,y in zip(in_order(root), reversed_order(root)))
        
def in_order(root):
    if not root: return
    yield from in_order(root.left)
    yield root.val
    yield from in_order(root.right)
    
def reversed_order(root):
    if not root: return
    yield from reversed_order(root.right)
    yield root.val
    yield from reversed_order(root.left)
