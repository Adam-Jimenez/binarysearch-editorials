"""
Decimal Number

Inspired by alex's solution.

This solution is based on grade-school division. The way we detect recurring digits is if we have a cycle while doing our division. Let's take 1/3 for example:

1 | 3
Since our numerator (1) is smaller than our denominator (3), we shift the decimal place and multiply the numerator by 10.
10 | 3 = 0.
3 can fix 3 times in ten, so we subtract 3*3 from 10 and add 3 to the decimal places:
1 | 3 = 0.3
1 has already been seen, so we are in a cycle. Everything between the last occurrence of 1 and now will be repeated forever.
"""
class Solution:
    def solve(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        intpart, r = divmod(numerator, denominator)
        ans = [sign + str(intpart)]
        if r: ans.append(".")
        
        seen = {}
        t = 0
        while r and r not in seen:
            seen[r] = t
            t += 1
            n, r = divmod(10 * r, denominator)
            ans.append(str(n))
        
        if r:
            ans.insert(seen[r] + 2, '(')
            ans.append(')')
        return "".join(ans)