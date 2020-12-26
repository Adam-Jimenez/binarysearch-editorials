"""
Vanity Phone Numbers

Python's itertools offer the product function, that returns the cartesian product of N collections. 

The cartesian product is all the combinations of one element from each container, which is exactly what we want.
See: https://en.wikipedia.org/wiki/Cartesian_product

So we map every digit to its possible characters and let product generate all the possibilities.
"""
from itertools import product
dct={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9": "wxyz",
}
class Solution:
    def solve(self, digits):
        return ["".join(combination) for combination in product(*[dct[d] for d in digits])]
        
