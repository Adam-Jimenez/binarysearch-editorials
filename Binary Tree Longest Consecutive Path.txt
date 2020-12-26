"""
Binary Tree Longest Consecutive Path

My solution is kinda fucked, but I transformed the tree into a undirected graph so it was possible to explore nodes in all directions.
"""
from collections import defaultdict
class Solution:
    def solve(self, root):
        adj_list=defaultdict(list)
        def dfs(node):
            for c in (node.left,node.right):
                if not c: continue
                adj_list[node].append(c)
                adj_list[c].append(node)
                dfs(c)
        dfs(root)
        seen=set()
        def longest(node,diff=None):
            seen.add(node)
            l=0
            for nei in adj_list[node]:
                if nei in seen: continue
                if diff is None:
                    if abs(node.val-nei.val)==1:
                        l=max(l,1+longest(nei,nei.val-node.val))
                elif nei.val-node.val == diff:
                    l=max(l,1+longest(nei,nei.val-node.val))
            seen.remove(node)
            return l
        ans=0
        for node in adj_list:
            ans=max(ans, longest(node))
        return ans+1