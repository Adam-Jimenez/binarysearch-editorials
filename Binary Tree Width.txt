"""
Binary Tree Width

For each level, we hold the leftmost and the rightmost values inside a dictionary.

To calculate the position,we need to count how many nodes are to the left of the current one:
``` 
        0
    0      1
  0  1   2   3
0 1 2 3 4 5 6 7
```
We can see a pattern emerge: each time we go left, the number of nodes to the left double, and if we go right we double as well, plus the left node.

In the end we return the largest interval.
"""
from collections import defaultdict
class Solution:
    def solve(self, root):
        d=defaultdict(lambda: [1e9,0])
        def dfs(node, pos=0, depth=0):
            if not node: return
            d[depth][0]=min(d[depth][0],pos)
            d[depth][1]=max(d[depth][1],pos)
            dfs(node.left,2*pos,depth+1)
            dfs(node.right,2*pos+1,depth+1)
        dfs(root)
        mx=0
        for interval in d.values():
            l,r=interval
            mx=max(mx,r-l+1)
        return mx
            
