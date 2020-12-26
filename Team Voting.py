"""
Team Voting

To be able to compare candidates in a lexicographic fashion, we can give them an array each of length equal to the number of candidates. A[0] will be the number of first places, A[1] the number of second places, etc.

After building the arrays for each candidates, we can sort the candidates based on their arrays and their associated letters in case of ties.
"""
from collections import defaultdict
class Solution:
    def solve(self, votes):
        cnt=len(votes[0])
        cand=defaultdict(lambda:[0]*cnt)
        for v in votes:
            for i,c in enumerate(v):
                cand[c][i]+=1
        return "".join(sorted(cand.keys(),key=lambda x:(cand[x],-ord(x)),reverse=True))
                
