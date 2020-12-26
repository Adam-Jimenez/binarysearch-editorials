"""
Friend Groups

We are looking for connected component in a graph.
One way to do so is to iterate over every vertices and color all the nodes it can reach using dfs, and increment the color counter.
Color is just a unique identifier that identify our connected components.
"""
class Solution:
    def solve(self, friends):
        colors={}
        def dfs(i,color):
            if i in colors:
                return
            colors[i]=color
            for f in friends[i]:
                dfs(f,color)
        color=0
        for i in range(len(friends)):
            if i not in colors:
                dfs(i, color)
                color+=1
        return color
