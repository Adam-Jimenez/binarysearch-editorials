"""
Vowels and Consonants Sort

I create two sorted arrays, one with vowels, other with consonant, and return the joined result.
"""
class Solution:
    def solve(self, s):
        return "".join(sorted(filter(vowels,s))+sorted(filter(consonant, s)))
def consonant(c):
    return not vowels(c)
def vowels(c):
    return c in "aeoui"