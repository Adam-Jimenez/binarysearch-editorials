"""
Zigzag String

We have an array containing each row of our answer, but we need a way to keep track of which row to add our character while iterating over the string.

We can build our own zigzag iterator by chaining an ascending range iterator (range(k)) and a descending range iterator (range(k-2, 0,- 1) and make it repeat indefinitely with cycle().

While iterating over characters in the string, we call next(row_itr) to get the next value in the iterator. We add the character to that row, and add  a space to the other rows for padding.
"""
from itertools import chain, cycle
class Solution:
    def solve(self, s, k):
        rows=["" for _ in range(k)]
        row_itr=cycle(chain(range(k), range(k-2, 0, -1)))
        for c in s:
            row_idx=next(row_itr)
            for j in range(k):
                if j == row_idx:
                    rows[j]+=c
                else:
                    rows[j]+=" "
        return "\n".join(rows)
