"""
Parentheses Grouping

Parentheses are balanced when there is an equal number of opening and closing parentheses. So each time the running count is equal to zero, we are balanced and append another group to our answer.
"""
class Solution:
    def solve(self, n):
        a=[[]]
        cnt=0
        for c in n:
            cnt += 1 if c=="(" else -1
            a[-1].append(c)
            if cnt==0:
                a.append([])
        return ["".join(x) for x in a if x]