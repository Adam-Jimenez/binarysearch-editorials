"""
Balanced Brackets

Two constraints apply for balanced brackets:

1. Same number of opening and closing brackets,
2. You never close more brackets than you open.
"""
class Solution:
    def solve(self, s):
        cnt=0
        for c in s:
            cnt += 1 if c == "(" else -1
            if cnt<0: return False
        return cnt==0
