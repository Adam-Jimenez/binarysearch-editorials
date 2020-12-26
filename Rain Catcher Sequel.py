"""
Rain Catcher Sequel

This approach to the problem is going in reverse - instead of starting from a square a finding the path of least height to the edge, we start from the edge and use a min heap to continually process the lowest square of ground.

When we process the square of least height, we add its neighbors to the heap. We also check if their height is smaller than the current square (the smallest possible neighbor to the square). If so, we add the difference to the answer. The new value in the heap will be the max of the two values.

Since the amount of water of a square is constrained by the path with the smallest maximal height - processing the paths starting from the edge with the smallest maximal height first will converge towards a correct answer.

Basically, this is dijkstra's algorithm with multiple starting points (the edge), and the key being the maximum along the path.
"""
from heapq import heappop, heapify, heappush
class Solution:
    def solve(self, matrix):
        if len(matrix)<3 or len(matrix[0])<3: return 0
        def get_neighbors(i,j):
            for di,dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni,nj = i+di, j+dj
                if ni>=0 and nj>=0 and ni < len(matrix) and nj<len(matrix[0]):
                    yield (ni,nj)
                    
        hp=[]
        seen=set()
        ans=0
        for i in range(len(matrix)):
            key = (matrix[i][0], i, 0)
            hp.append(key)
            key = (matrix[i][-1], i, len(matrix[0])-1)
            hp.append(key)
            seen.add((i,0))
            seen.add((i,len(matrix[0])-1))
        for j in range(1,len(matrix[0])-1):
            key = (matrix[0][j], 0, j)
            hp.append(key)
            key = (matrix[-1][j], len(matrix)-1, j)
            hp.append(key)
            seen.add((0,j))
            seen.add((len(matrix)-1,j))
        heapify(hp)
        while hp:
            cur_level, i, j = heappop(hp)
            for ni,nj in get_neighbors(i,j):
                if (ni,nj) in seen: continue
                seen.add((ni,nj))
                nei_level = matrix[ni][nj]
                if nei_level < cur_level:
                    ans += cur_level - nei_level
                heappush(hp,(max(nei_level, cur_level), ni, nj))
        return ans
                
