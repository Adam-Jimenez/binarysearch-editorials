"""
camelCase

lowercase the first word, capitalize the rest. ez pz
"""
class Solution:
    def solve(self, words):
        s=words.pop(0).lower()
        return s+"".join(w.capitalize() for w in words)
        # Write your code here
        
