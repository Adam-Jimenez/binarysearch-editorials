"""
Cell Fusion

We can simulate the process using a heap, a data structure specialized in accessing the max values of a collections quickly.
"""
from heapq import heapify, heappop, heappush
class Solution:
    def solve(self, cells):
        cells=[-x for x in cells]
        heapify(cells)
        while len(cells)>1:
            a,b = -heappop(cells), -heappop(cells)
            if a!=b:
                heappush(cells, -((a+b)//3))
        return -cells[0] if cells else -1
