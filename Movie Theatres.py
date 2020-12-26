"""
Movie Theatres

We iterate chronogically through events (start of movie or end of movie). If the event type is start of movie, we increment the counter of movies running simultnaneously by one, otherwise a movie has ended and we decrement it.

We keep track of the maximum number of movies and return it.
"""
class Solution:
    def solve(self, intervals):
        mx=cnt=0
        a=[]
        a+=list(map(lambda x: (x[0], 1), intervals))
        a+=list(map(lambda x: (x[1], -1), intervals))
        a.sort()
        for _,inc in a:
            cnt += inc
            mx=max(mx,cnt)
        return mx