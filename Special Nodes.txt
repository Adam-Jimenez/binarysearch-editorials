"""
Special Nodes

We generate a set of colors for every subtree, and return: (the set of colors, if the subtree contains all uniques and the number of uniquely colored subtrees). For a subtree to be uniquely colored, all its children must be uniquely colored and the color of the root node must not be in the set of colors in the child nodes.
"""
class Solution:
    def solve(self, tree, color):
        seen=set()
        def dfs(node):
            seen.add(node)
            colors=set()
            unique=True
            ans=0
            for nei in tree[node]:
                if nei in seen: continue
                cols,uniq_count,subtree_unique=dfs(nei)
                ans+=uniq_count
                if not unique: continue
                unique &= subtree_unique
                if len(cols&colors)!=0: unique=False
                colors |= cols
            if color[node] in colors:
                unique=False
            else:
                colors.add(color[node])
            if unique: ans+=1
            seen.remove(node)
            return colors,ans,unique
        _,a,_= dfs(0)
        return a
