"""
Common Words

We create a set of the lowercase words for each sentence, which will remove duplicates. Then Python offers the & operator on sets to do the intersection, which will keep the words that are in both sets. We return the length of the set that has the words shared by both sentences.

"""
class Solution:
    def solve(self, s0, s1):
        a=set(x.lower() for x in s0.split())
        b=set(x.lower() for x in s1.split())
        return len(a&b)
        # Write your code here
