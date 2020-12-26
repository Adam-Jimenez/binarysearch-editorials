"""
Hanging Banners

We sort the intervals by their end. When iterating, we keep an upper bound which is the current max end time. If the start of the next interval is before the bound, we have an intersection so we do not need to count an extra time, otherwise this interval is independent and we have to add it to the answer.
"""
class Solution:
    def solve(self, intervals):
        intervals.sort(key=lambda i: i[1])
        last = float('-inf')
        ans = 0
        for s, e in intervals:
            if s <= last:
                continue
            last = e
            ans += 1
        return ans