"""
Largest Anagram Group

We sort the words so anagrams are equal, build a counter and take most frequent.
"""
from collections import Counter
class Solution:
    def solve(self, words):
        return Counter(map(lambda x: "".join(sorted(x)), words)).most_common(1)[0][1]