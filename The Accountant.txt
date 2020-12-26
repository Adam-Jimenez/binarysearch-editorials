"""
The Accountant

Undercover base conversion problem. We divide repeatedly by 26 to find the character, subtract one because it is 1-based.
"""
class Solution:
    def solve(self, n):
        ans=""
        while n:
            n,rem = divmod(n-1,26)
            ans+=chr(rem+ord("A"))
        return ans[::-1]
