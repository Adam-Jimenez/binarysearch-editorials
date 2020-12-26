"""
Acronym

We can build a generator expression that returns the first letter capitalized for each word, and filters "and"s. 
"""
class Solution:
    def solve(self, s):
        return "".join(w[0].upper() for w in s.split() if w != "and")
