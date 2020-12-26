"""
Pattern to Word Bijection

Bijection means that for every element in group a, there is only one element in group b and vice-versa.

So, the number of elements in group a must equal the number of elements in group b which must equal the unique number of edges between the two groups.
"""
class Solution:
    def solve(self, s, p):
        words = s.split()
        return len(set(words)) == len(set(p)) == len(set(zip(words, p)))