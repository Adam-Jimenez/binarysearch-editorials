"""
Bubble Swap

Stolen from alexwice, O(n^2)

We sequentially compute the cost of bringing the correct value to the front of the array (which is equal to its position in the array), in an insertion sort fashion.
"""
class Solution:
    def solve(self, lst0, lst1):
        ans = 0
        for req in lst1:
            i = lst0.index(req)
            lst0.pop(i)
            ans += i
        return ans