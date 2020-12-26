"""
Distinct Subsequences

Let's forget the constraint that our subsequences must be unique for a bit. For every character in our subsequence, we double the number of possible subsequences, because we can either use a character or not use it.

The problem is that we have overlap between subsequences when we have duplicate characters. Let's take for example, "aca".

First we start with empty string, "". It counts as one possibility.
For the first character "a", we can either take it or not, so our possibilities become "" or "a", 2 possibilites.
For the character "c", we can either take it or not, so our possibilities become "", "a", "c", "ac", 4 possibilites.
For the last character "a", we can either take it or not, so our possibilities become "", "a", "c", "ac", "a", "aa", "ca", "aca", 8 possibilites.

But we notice the overlap between the two "a" possibilities. The trick is to remember the last time we seen the character, and subtract the number of possibilities when we saw that character, as to get rid of the overlapping possibilities.

We subtract one at the end to remove the initial empty subsequence.
"""
MOD = 10**9+7
class Solution:
    def solve(self, s):
        last = {}
        a = [1]
        for i,c in enumerate(s):
            prev = a[-1] * 2
            if c in last:
                prev -= a[last[c]]
            a.append(prev % MOD)
            last[c] = i
        return a[-1]-1