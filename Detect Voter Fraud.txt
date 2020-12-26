"""
Detect Voter Fraud

If the length of the set made out of unique voter ids is the same as the length of the votes, we know each vote has a unique voter.

P.S. use set comprehensions like alex, to avoid converting list to set.
"""
class Solution:
    def solve(self, votes):
        return len(set([x[1] for x in votes]))!=len(votes)
