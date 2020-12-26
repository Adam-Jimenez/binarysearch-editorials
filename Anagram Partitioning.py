"""
Anagram Partitioning

Recursive solution: each time the frequency of the characters in each character is matched, we do a recursive call and check if the rest of the string is solvable.
"""
from collections import Counter
class Solution:
    def solve(self, a, b):
        def bt(i=0):
            if i == len(a): return True, []
            cnta = Counter()
            cntb = Counter()
            for j in range(i, len(a)):
                cnta[a[j]]+=1
                cntb[b[j]]+=1
                if cnta == cntb:
                    solved, indexes = bt(j+1)
                    if solved:
                        indexes.append(i)
                        return solved, indexes
            return False, []
        solved, rev_idx = bt()
        if not solved: return []
        else: return rev_idx[::-1]
