"""
Reverse Graph

One-line solution goes as follows:

We iterate through each value in the graph, then we build an array by iterating through the graph again, and adding the index of the list if the original index is present in the list.

Makes sense?
"""
class Solution:
    def solve(self, graph):
        return [[x for x,l in enumerate(graph) if i in l] for i,_ in enumerate(graph)]