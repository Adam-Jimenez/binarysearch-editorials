"""
Forest Detection

To validate that we have a "forest", we can use the rule that there should be only one path between every node. One way to validate this is to do BFS from every unexplored node, and each time you visit a neighbor, you remove the edge between them. If you ever fall on a node you already explored, there is more than one path to this node so this is not a tree.
"""
from collections import defaultdict
from collections import deque
class Solution:
    def solve(self, edges):
        adj_list=defaultdict(set)
        nodes=set()
        for s,e in edges:
            adj_list[s].add(e)
            adj_list[e].add(s)
            nodes.add(s)
            nodes.add(e)
        seen=set()
        def bfs(start):
            q=deque([start])
            while q:
                cur=q.popleft()
                for nei in set(adj_list[cur]):
                    if nei in seen: return False
                    seen.add(nei)
                    adj_list[nei].remove(cur)
                    adj_list[cur].remove(nei)
                    q.append(nei)
            return True
        for n in nodes:
            if n not in seen:
                seen.add(n)
                if not bfs(n): 
                    return False
        return True