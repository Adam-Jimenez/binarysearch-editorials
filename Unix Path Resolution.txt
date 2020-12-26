"""
Unix Path Resolution

Same as alexwice's answer but with one less newline, therefore it is better.

"""
class Solution:
    def solve(self, path):
        a=[]
        for x in path:
            if x == "..":
                if a:
                    a.pop()
            elif x != ".":
                a.append(x)
        return a