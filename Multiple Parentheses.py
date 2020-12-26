"""
Multiple Parentheses

We keep track of nesting levels using a dictionary. Each time we meet a "(", we increase the current nesting level (cnt), each time we meet a ")" we decrease it. If we ever go under a nesting level e.g. "())", the reference to the nesting level cannot be used anymore because it is invalid. We return the longest distance between two positions with the same nesting level, where we never go under the nesting level in between those positions.
"""
class Solution:
    def solve(self, s):
        ans=0
        left={}
        cnt=0
        for i,c in enumerate(s):
            if cnt not in left: left[cnt]=i
            d = 1 if c == "(" else -1
            if d == -1 and cnt in left: 
                del left[cnt]
            cnt+=d
            cnt=max(cnt,0)
            if cnt in left:  ans=max(ans, i-left[cnt]+1)
        return ans
