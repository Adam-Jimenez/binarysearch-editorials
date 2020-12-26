"""
Finding Binary Search in a String

We can store the positions for each character in the input string in a dictionary.

Then, we can treat this as a graph traversal problem, where the next possible nodes are the next character in the string "binarysearch", where the position of the character comes after the current one and respects the constant difference constraint.
"""
from collections import defaultdict
class Solution:
    def solve(self, s):
        chrs=defaultdict(list)
        for i,c in enumerate(s):
            chrs[c].append(i)
        target="binarysearch"
        def dfs(i=0, last=None, diff=None):
            if i == len(target): 
                return True
            c=target[i]
            for pos in chrs[c]:
                if last and pos < last: continue
                if not diff or pos-last==diff:
                    if dfs(i+1, pos, pos-last if last else None): 
                        return True
            return False
        return dfs()