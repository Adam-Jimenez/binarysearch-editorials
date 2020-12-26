"""
Linked List Folding

Cheated solution: fill an array with the nodes. Add the value of corresponding node symmetric to the center. Reverse the Linked List and return the center node.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        a=[x for x in it(node)]
        for i in range((len(a)//2)):
            a[i].val += a[len(a)-i-1].val
        for i in range(1, len(a)):
            a[i].next = a[i-1]
        a[0].next=None
        return a[(len(a)-1)//2]
        
def it(node):
    while node:
        yield node
        node=node.next
