"""
Kth Last Node of a Linked List

Cheated solution, populate array with linked list values and take kth last element.
"""
class Solution:
    def solve(self, node, k):
        A=[]
        while node:
            A.append(node.val)
            node=node.next
        return A[len(A)-1-k]
