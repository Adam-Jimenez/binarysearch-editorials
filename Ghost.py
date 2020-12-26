"""
Ghost

Based on Sacha's answer, with a slight modification. We don't have to keep who's turn it is. We can implement something similar to negamax: https://en.wikipedia.org/wiki/Negamax
"""
_end = '.'
def minmax(tr):
    if _end in tr: 
        return True
    return any(not minmax(t) for t in tr.values())
        
class Solution:
    def solve(self, words):
        trie = dict()
        for word in words:
            current_dict = trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = True
        return minmax(trie)
