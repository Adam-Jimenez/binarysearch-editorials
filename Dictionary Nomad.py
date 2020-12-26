"""
Dictionary Nomad

The challenge in this problem is to efficiently build the graph representing the valid transitions between words. One way is to group words by strongly connected components, where every word in the same bucket share all letters except one, and then we can retrieve the neighbors of a word by retrieving all the strongly connected components they belong to. 

When we have a way to get neighbors of a word, we can apply the classic BFS approach to find the shortest path in a non-weighted graph.
"""
from collections import defaultdict,deque
class Solution:
    def solve(self, dictionary, start, end):
        components=defaultdict(list)
        neighbors=defaultdict(set)
        l = len(dictionary[0])
        for omit in range(l):
            for w in dictionary:
                key=(omit,w[:omit],w[omit+1:])
                components[key].append(w)
        def get_neighbors(word):
            for omit in range(len(word)):
                key=(omit,word[:omit],word[omit+1:])
                if key in seen_components: continue
                for nxt in components[key]:
                    if nxt not in seen and nxt != word:
                        yield nxt
                seen_components.add(key)
        q=deque([start])
        seen=set([start])
        seen_components=set()
        ans=0
        while q:
            ans+=1
            for _ in range(len(q)):
                node=q.popleft()
                if node == end: return ans
                for nxt in get_neighbors(node):
                    seen.add(nxt)
                    q.append(nxt)
        return -1