"""
Interval Carving

If our interval intersects with cut, we check if there is a remainder before and after the cut and add it if so. If there's no intersection we just add the intersection.
"""
class Solution:
    def solve(self, intervals, cut):
        cs,ce=cut
        ans=[]
        for s,e in intervals:
            if max(cs,s)<min(e,ce):
                if s<cs:
                    ans.append([s,cs])
                if e>ce:
                    ans.append([ce,e])
            else:
                ans.append([s,e])
        return ans
