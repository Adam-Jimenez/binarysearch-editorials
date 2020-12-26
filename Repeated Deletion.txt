"""
Repeated Deletion

EDIT: invalid because we never check for trailing duplicates, view other solution.

https://www.youtube.com/watch?v=3zUUtf7gOe8

Add characters onto a stack. Each time you encounter a new character, check whether the top of the stack contains duplicates, if so, pop them.
"""
class Solution:
    def solve(self, s):
        stk=[]
        for c in s:
            if len(stk) > 1 and c != stk[-1] and stk[-1] == stk[-2]:
                top=stk[-1]
                while stk and top == stk[-1]: stk.pop()
            stk.append(c)
        return "".join(stk)
