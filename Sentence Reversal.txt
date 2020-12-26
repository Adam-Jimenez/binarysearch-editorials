"""
Sentence Reversal

We can retrieve the sentence by joining the list. Then to reverse the words, we split on spaces and reverse the resulting list. The we join the words with spaces and return the result as a list of characters.
"""
class Solution:
    def solve(self, words):
        return list(" ".join("".join(words).split(" ")[::-1]))
