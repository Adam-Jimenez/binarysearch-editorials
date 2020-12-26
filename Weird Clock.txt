"""
Weird Clock

We build a set of valid characters from the initial string, then increment one minute until we reach a time with characters subset of the initial string.
"""
from datetime import datetime, timedelta
class Solution:
    def solve(self, s):
        time=datetime.strptime(s,"%H:%M")
        digits=set(s)
        while True:
            time+=timedelta(minutes=1)
            s2=time.strftime("%H:%M")
            if len(set(s2)-digits)==0: return s2