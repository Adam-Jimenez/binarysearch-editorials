"""
Tree Coloring

Swapping adjacent nodes means we can reorder the nodes as we wish, so we just need to count the number of colors to see if they can fit in the ordered version of the tree.

If we would color the tree by hand, the colors would alternate between each level. So if we count the number of nodes of each odd level and each even level, it should equal the frequency of unique colors for it to be solvable.
"""
from collections import defaultdict
class Solution:
    def solve(self, root):
        colors=defaultdict(int)
        prop=defaultdict(int)
        def dfs(node,flag=True):
            if not node:return
            colors[node.val]+=1
            prop[flag]+=1
            dfs(node.left, not flag)
            dfs(node.right, not flag)
        dfs(root)
        return set(colors.values()) == set(prop.values())
        
