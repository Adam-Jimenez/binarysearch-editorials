"""
Mindboggling

We build a Trie datastructure with the dictionary and explore the matrix using DFS from each position. 

Read more about tries here: https://en.wikipedia.org/wiki/Trie
"""
from itertools import product
class Trie:
    def __init__(self):
        self.children={}
        self.end=False
    def add_word(self,w):
        self.add_trie_nodes(w,w)
    def add_trie_nodes(self,w,full_word):
        if w=="": 
            self.end=True
            self.word=full_word
        elif w[0] in self.children:
            self.children[w[0]].add_trie_nodes(w[1:],full_word)
        else:
            t=Trie()
            t.add_trie_nodes(w[1:],full_word)
            self.children[w[0]] = t
    def contains(self, character):
        return character in self.children
    def get_child(self, character):
        return self.children[character]
    
    def is_end(self):
        return self.end
        
    def get_word(self):
        return self.word
        
def in_bounds(i,j,matrix):
    return i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0])
    
class Solution:
    def solve(self, matrix, words):
        trie=Trie()
        for word in words:
            trie.add_word(word)
        directions = list(product(range(-1,2),repeat=2))
        found={}
        seen=[[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        def dfs(position,trie_node):
            if trie_node.is_end():
                found[trie_node.get_word()]=True
                return
            i,j=position
            for di,dj in directions:
                ni,nj = i+di, j+dj
                if in_bounds(ni,nj,matrix) and not seen[ni][nj] and trie_node.contains(matrix[ni][nj]):
                    seen[ni][nj]=True
                    dfs((ni,nj), trie_node.get_child(matrix[ni][nj]))
                    seen[ni][nj]=False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs((i,j), trie)
        return sum(found.values())
                    
                
