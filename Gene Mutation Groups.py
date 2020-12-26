"""
Gene Mutation Groups

We can make strongly connected component by iterating over every gene, then every letter removal. Take "ACGT" and "AGGT" for example, then will end up in the same bucket with key (left="A", right="GT") when the second letter is removed.

Then, we can apply a simple DFS to count the connected groups, where every neighbor belong to the same strongly connected components as the current gene. Each time we encounter a gene we haven't explored, we have found a new group, then we mark as seen all genes belonging to the same group.

O(N*L) time, N being the number of genes and L being the length of the genes
O(N) space
"""
from collections import Counter,defaultdict
class Solution:
    def solve(self, genes):
        comp=defaultdict(list)
        for gene in genes:
            for i in range(len(gene)):
                left=gene[:i]
                right=gene[i+1:]
                comp[(left,right)].append(gene)
        seen=set()
        ans=0
        def dfs(gene):
            for i in range(len(gene)):
                left=gene[:i]
                right=gene[i+1:]
                for nei in comp[(left,right)]:
                    if nei not in seen:
                        seen.add(nei)
                        dfs(nei)
        for gene in genes:
            if gene not in seen:
                ans+=1
                seen.add(gene)
                dfs(gene)
        return ans
