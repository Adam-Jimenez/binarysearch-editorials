"""
Direct Closure

BFS solution: iterate over each node (indexes), and mark all the neighbors it can reach.
"""
class Solution:
    def solve(self, graph):
        ans=[[0 for _ in graph] for _ in graph]
        for i in range(len(graph)):
            q=[i]
            while q:
                node=q.pop(0)
                if ans[i][node]: continue
                ans[i][node]=1
                neighbors=graph[node]
                for n in neighbors:
                    q.append(n)
        return ans
