"""
Remove Duplicates in Linked List

We keep track of seen values with a set. We look ahead of the current node to see if its value is in the set, if so we erase it by modifying the pointer to the next value.

Important to note, we don't continue iterating if we found a duplicate. Imagine:
1->1->1-> 2
If we remove the second one, we don't jump to the third one, we redo the check before jumping to the next node.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        head=node
        seen=set()
        while node.next:
            seen.add(node.val)
            if node.next.val in seen:
                node.next = node.next.next
            else:
                node=node.next
        return head