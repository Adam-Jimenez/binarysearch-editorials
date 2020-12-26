"""
Collision Detection

We can use the "ray-tracing" strategy, described here: http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html

From our point (x,y), we trace a line to the left and count the number of segment it intersects. If the number is odd, we must be inside the polygon.

To compute this, we check every segment that includes the y position of our point, and check if it is to the left our of point. To find the x position of the slope at position y,  we need to compute the slope of the segment.

Video explanation: https://www.youtube.com/watch?v=yeOIE1oyV0U
"""
class Solution:
    def solve(self, polygon, x, y):
        ans=False
        for i in range(len(polygon)):
            x0,y0 = polygon[i]
            x1,y1 = polygon[(i+1)%len(polygon)]
            if not min(y0,y1) < y <= max(y0,y1): continue
            if x < min(x0,x1): continue
            cur_x = x0 if x0==x1 else x0+(y-y0)*(x1-x0)/(y1-y0)
            ans^= x>cur_x
        return ans