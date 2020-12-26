"""
Atbash Cipher

We create a dictionary mapping a to z, b to y, etc. And then we map the text to this dictionary.
"""
from string import ascii_lowercase
class Solution:
    def solve(self, text):
        d = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))
        return "".join(map(lambda c: d[c], text))
