"""
Column Flips to Maximum Number of Equal Rows

The only rows that can all be ones or zeroes are the rows that are either exactly the same or the inverse of each other. So, we can put rows into buckets, identified to the values relative to the first value. That way, rows that are identical or the inverse will go into the same bucket. 

Example:
0101 -> will go into bucket {0,2}, because those are the indices of the values equal to the first value
1010 -> will go into bucket {0,2}, because those are the indices of the values equal to the first value
1100 -> will go into bucket {0,1}
0011 -> will go into bucket {0,1}

The answer is the size of the largest bucket of rows. In the example, we have two buckets of size two, so the answer is two.

O(nm) time, O(nm) space
"""
from collections import Counter
class Solution:
    def solve(self, matrix):
        c=Counter()
        for row in matrix:
            s=set()
            for i,v in enumerate(row):
                if v==row[0]:
                    s.add(i)
            c[frozenset(s)]+=1
        return max(c.values())
