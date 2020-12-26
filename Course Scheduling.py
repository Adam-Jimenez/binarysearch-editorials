"""
Course Scheduling

This problem is about checking if topological sorting is possible, which equates to checking if the graph is a DAG (Directed Acyclic Graph).

To check whether our graph has cycles, we can simply do a depth-first search on every node and check if we ever return on a visited value. 

When we completed the depth-first search on a node, we never need to check it again, hence the checked array.

Relevant reading: https://en.wikipedia.org/wiki/Topological_sorting
"""
class Solution:
    def solve(self, matrix):
        visited=[False for _ in matrix]
        checked=[False for _ in matrix]
        def dfs(i):
            if visited[i]: return False
            if checked[i]: return True
            visited[i]=True
            for j in matrix[i]:
                if not dfs(j):
                    return False
            visited[i]=False
            checked[i]=True
            return True
        for i in range(len(matrix)):
            if not dfs(i):
                return False
        return True