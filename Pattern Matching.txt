"""
Pattern Matching

We recursively iterate over each letter in the pattern. If it doesn't exist in the mappings, we try every possible prefix of the string as a mapping.

Otherwise, we compare the mapping to the string, seeing if it matches the start. 
"""
class Solution:
    def solve(self, s, p):
        uniq=set(p)
        def parse(s,p, mappings=dict()):
            if not s and not p and len(mappings) == len(uniq): return True
            if not s or not p: return False
            c=p[0]
            if c not in mappings:
                for i in range(len(s)):
                    mappings[c] = s[:i+1]
                    if parse(s[i+1:],p[1:],mappings): return True
                    del mappings[c]
                return False
            else:
                mapp = mappings[c]
                if len(mapp)>len(s): return False
                for i in range(len(mapp)):
                    if mapp[i] != s[i]: return False
                return parse(s[len(mapp)+1:], p[1:], mappings)
        return parse(s,p)