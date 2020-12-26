"""
Back to Front Linked List

Lazy solution: stick everything in a list, then pop back, pop front, ... and reorder shit.
"""
class Solution:
    def solve(self, node):
        a=[*it(node)]
        ans=[]
        while a:
            ans.append(a.pop())
            if a: ans.append(a.pop(0))
        for i in range(len(ans)-1):
            ans[i].next=ans[i+1]
        ans[-1].next=None
        return ans[0]
        

def it(node):
    while node:
        yield node
        node=node.next