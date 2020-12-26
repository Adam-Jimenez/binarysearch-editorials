"""
DDoS Protection

We keep track of a global queue and a queue per user. We process requests ordered by timestamp, for each request we remove all the ones earlier than 60 seconds. If any queue is larger than u or g, we skip the current request.
"""
from collections import defaultdict
class Solution:
    def solve(self, requests, u, g):
        requests.sort()
        requests.sort(key=lambda x: x[1])
        user_qs=defaultdict(list)
        global_q=[]
        ans=0
        for req in requests:
            user_id, time = req
            lim = time-60
            user_q=user_qs[user_id]
            while global_q and global_q[0]<=lim:
                global_q.pop(0)
            while user_q and user_q[0]<=lim:
                user_q.pop(0)
            if len(global_q)<g and len(user_q)<u:
                ans+=1
                user_q.append(time)
                global_q.append(time)
        return ans
                
