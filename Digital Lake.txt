"""
Digital Lake

We can DP on the digits, where we iterate between every digit between 0 and the limit set by n for the current digit.

If we pick a digit smaller than the digit n[i], we can iterate over all 0-9 digits for the rest of the digits.

Then, when our digit is equal to our target d, we add it to the answer by the number of possibilities for the next digits.

One important edge case is when d=0, because we cannot considering leading zeroes e.g. 0001. For this, we check if we have at least one non-zero digit before the current digit to count zeroes.
"""
from functools import lru_cache
class Solution:
    def solve(self, n, d):
        digits = [int(c) for c in str(n)]
        @lru_cache(None)
        def dp(i=0, free=False, leading=False):
            if i == len(digits):
                return 0,1
            ans=0
            possibilities=0
            for digit in range(10):
                if not free and digit > digits[i]: break
                subans, subpos = dp(i+1, free or digit < digits[i], leading | digit != 0)
                possibilities += subpos
                ans+=subans
                if (digit != 0 and digit == d) or (digit == d and leading):
                    ans += subpos
            return ans,possibilities
        return dp()[0]
                
                