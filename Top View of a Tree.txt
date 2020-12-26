"""
Top View of a Tree

We perform a regular BFS, with the position of the nodes relative to root. We overwrite the value if it hasn't been seen to emulate the projection.

"""
class Solution:
    def solve(self, root):
        top={}
        q=[(root, 0)]
        while q:
            node,pos = q.pop(0)
            if pos not in top: top[pos]=node.val
            if node.left: q.append((node.left,pos-1))
            if node.right: q.append((node.right,pos+1))
        return [v for _,v in sorted(top.items())]
