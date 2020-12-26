"""
Rotate by 90 Degrees Counter-Clockwise

Why are you guys trying to hard, its just one line of code lmao
"""
class Solution:
    def solve(self, matrix):
        return [list(x) for x in zip(*map(reversed,matrix))]
