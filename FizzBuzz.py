"""
FizzBuzz

Sexy one-liner. You can multiply by booleans! Isn't that nice. Pull this bad boy out during an interview and you'll make them soak.
"""
class Solution:
    def solve(self, n):
        return [("Fizz"*(n%3==0)+"Buzz"*(n%5==0)) or str(n) for n in range(1,n+1)]
