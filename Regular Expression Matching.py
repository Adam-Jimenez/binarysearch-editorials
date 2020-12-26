"""
Regular Expression Matching

Based on https://nickdrane.com/build-your-own-regex/

Recursive solution where we process one character from the pattern at the time, except if a star is involved.

To compare characters, we have the match_one function, that checks equality or if pattern is a "."
For stars, we have a match_star function, that tries to match all possibilities. If none match, we just ignore the star.
"""
class Solution:
    def solve(self, pattern, s):
        return match(pattern,s)
        
def match(pattern, s):
    if not pattern and not s: return True
    if not pattern or not s: return False
    if len(pattern)>1 and pattern[1] == "*":
        return match_star(pattern, s)
    return match_one(pattern[0], s[0]) and match(pattern[1:], s[1:])
    
def match_star(pattern, text):
    i=0
    while i<len(text) and match_one(pattern[0], text[i]):
        if match(pattern[2:], text[i+1:]): return True
        i+=1
    return match(pattern[2:], text)
    
def match_one(pattern,text):
    return pattern == "." or pattern == text
        
