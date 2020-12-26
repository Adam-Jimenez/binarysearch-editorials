"""
Reverse Words Sequel

Inspired by Alex, but maybe a little clearer? Build a stack with words, then undo the stack, adding the delimiters at the same time.

k is True means the group is delimiters.
"""
from itertools import groupby
class Solution:
    def solve(self, sentence, delimiters):
        words=[]
        ans=""
        for k,g in groupby(sentence, lambda x: x in delimiters):
            if not k:
                words.append("".join(g))
        for k,g in groupby(sentence, lambda x: x in delimiters):
            if k:
                ans+="".join(g)
            else:
                ans+=words.pop()
        return ans
