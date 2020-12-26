"""
K Unique String

We find the unique numbers and their frequencies using a Counter. If we have more than k distinct numbers, we need to change the least frequent numbers to obtain the minimum number of changes.

We can obtain the least frequent values from a counter by reversing the result of most_common(), or just removing the value from the end.
"""
from collections import Counter
class Solution:
    def solve(self, s, k):
        counter=Counter(s)
        L = len(counter)
        if L<=k: return 0
        return sum(cnt for _,cnt in counter.most_common()[-(L-k):])
