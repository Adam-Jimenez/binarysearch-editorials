"""
Copy Paste

When n is less or equal to 2, copy-pasting is not worth it.

Otherwise, we have check the parity of n. If the number of operations left is odd, we have to add another character because we need an equal number of copy actions and paste actions. Then, we compute the number of times we double with n//2, the number of copy and paste.
"""
class Solution:
    def solve(self, n):
        if n<=2: return n
        n-=2
        return (2+(n&1))*(2**(n//2))%(10**9+7)
        
