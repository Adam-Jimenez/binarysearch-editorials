"""
Uber Pool

Heap-based solution, O(n log n)

Given that the trips are already sorted by start, we can iterate through the trips and add their capacity to a counter. 

We add the end of each trip to a heap. For each following trip, we will check if we have to drop off anyone by checking the top of the min-heap and looking if the end of the trip is less or equal than the start of the current.
"""
from heapq import heappop, heappush
class Solution:
    def solve(self, trips, capacity):
        cnt=0
        dropoff=[]
        for start,end,num in trips:
            while dropoff and dropoff[0][0] <= start:
                cnt-=dropoff[0][1]
                heappop(dropoff)
            cnt+=num
            if cnt > capacity:
                return False
            heappush(dropoff, (end,num))
        return True
