"""
Level Order Alternating

We can simply do breadth-first search, and track when to reverse the values with a boolean.
"""
class Solution:
    def solve(self, root):
        ans=[root.val]
        q=[root]
        level=[]
        reverse=True
        while q:
            while q:
                node=q.pop(0)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            ans += values(level) if not reverse else values(level[::-1])
            q=level
            level=[]
            reverse = not reverse
        return ans
            
def values(arr):
    return list(map(lambda x:x.val, arr))