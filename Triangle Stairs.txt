"""
Triangle Stairs

"*"*i to get the correct numbers of stars,
rjust(n, " ") to always fill right with spaces!
"""
class Solution:
    def solve(self, n):
        return "\n".join([("*"*i).rjust(n," ") for i in range(1,n+1)])
