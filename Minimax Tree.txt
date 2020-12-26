"""
Minimax Tree

Clean way to code it, hope you enjoy ;)                
"""
fn=[min,max]
class Solution:
    def solve(self, node,you=True):
        if not node or not node.left and not node.right: return node
        node.left=self.solve(node.left,not you)
        node.right=self.solve(node.right,not you)
        node.val = fn[you](n.val for n in (node.left, node.right) if n)
        return node
