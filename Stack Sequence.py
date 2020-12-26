"""
Stack Sequence

We can replay the pushes, and whenever we can pop the value at the start of pops, we do it cause why not.

"""
class Solution:
    def solve(self, pushes, pops):
        s=[]
        for p in pushes:
            s.append(p)
            while s and pops and s[-1] == pops[0]:
                s.pop()
                pops.pop(0)
        return s == pops == []
