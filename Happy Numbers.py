"""
Happy Numbers

Constant space solution using two variables to detect cycles. If there is a cycle, the fast variable will catch up to the slow one, and the loop will exit. 
"""
class Solution:
    def solve(self, n):
        slow=fast=n
        fast=f(fast)
        while slow!=fast:
            slow=f(slow)
            fast=f(f(fast))
            if fast == 1: return True
        return False

def f(n):
    return sum(int(x) ** 2 for x in str(n))
