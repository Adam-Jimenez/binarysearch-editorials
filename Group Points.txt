"""
Group Points

Similar to BFS in some ways:

For every point, we iterate over every point and if its within k distance, we add it to a queue. Then, we repeat the same process for every point in the queue, until the queue is exhausted. At that point, we have a disjoint group.

"""
from collections import deque

class Solution:
    def solve(self, points, k):
        groups=[]
        seen=set()
        for i in range(len(points)):
            if i in seen: continue
            group=[]
            q=deque([i])
            seen.add(i)
            while q:
                cur=q.popleft()
                group.append(cur)
                px,py = points[cur]
                for j in range(len(points)):
                    if j in seen: continue
                    nx,ny = points[j]
                    if (((px-nx)**2 + (py-ny)**2)**0.5) <= k:
                        seen.add(j)
                        q.append(j)
            groups.append(group)
        return len(groups)
