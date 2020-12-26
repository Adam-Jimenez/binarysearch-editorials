"""
High Five

You don't need to think if you try all possibilities :D it's O(n) anyways. 

Just try all possible insertions, note that you can't start at index 0 if its negative because it will put a digit in front of the negative sign.
"""
class Solution:
    def solve(self, n):
        s=str(n)
        return max(int(s[:i]+"5"+s[i:]) for i in range(n<0,len(s)+1))