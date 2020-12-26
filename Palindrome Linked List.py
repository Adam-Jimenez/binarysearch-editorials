"""
Palindrome Linked List

Cheated solution, fill an array with linked list values and check whether it is symmetric.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        a=[*it(node)]
        return a == a[::-1]

def it(node):
    while node:
        yield node.val
        node=node.next