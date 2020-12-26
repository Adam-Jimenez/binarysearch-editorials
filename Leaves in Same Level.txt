"""
Leaves in Same Level

We can use a generator to generate all the leaves depth, and check if there is only one unique depth using a set.
"""
class Solution:
    def solve(self, root):
        return len({x for x in leaves_depth(root)})==1

def leaves_depth(node,depth=0):
    if not node.left and not node.right: yield depth
    if node.left: yield from leaves_depth(node.left,depth+1)
    if node.right: yield from leaves_depth(node.right,depth+1)
