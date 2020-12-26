"""
Inorder Traversal

Oh baby generators are so sexy. ~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class Solution:
    def solve(self, root):
        return list(it(root))
        
def it(node):
    if not node: return
    yield from it(node.left)
    yield node.val
    yield from it(node.right)
