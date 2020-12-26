"""
TV Shows

It's like taking the k largest numbers out of an array, but first you need to combine the numbers belonging to the same title. We can do so using a dictionary.
"""
from collections import defaultdict
class Solution:
    def solve(self, shows, durations, k):
        d=defaultdict(int)
        for t,dur in zip(shows, durations):
            d[t] += dur
        a = sorted(d.values(), reverse=True)
        return sum(a[:k])
