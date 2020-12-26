"""
Second Place

We can iterate over leaves using a generator, storing the nodes according to their depths. Then, we sorted nodes based on depth and take the second largest depth.
"""
from collections import defaultdict
class Solution:
    def solve(self, root):
        depths=defaultdict(list)
        for n,d in it(root):
            depths[d].append(n.val)
        a=sorted(depths.items(),reverse=True)
        return a[1][0]
        
def it(node,depth=0):
    if not node.left and not node.right: yield node,depth
    if node.left: yield from it(node.left, depth+1)
    if node.right: yield from it(node.right, depth+1)
