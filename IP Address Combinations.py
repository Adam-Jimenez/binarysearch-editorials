"""
IP Address Combinations

We can make a valid ip address generator by brute forcing all possible chunks of size 1,2 and 3. For each chunk, we check if there is no leading zeroes and if its in the [0,255] range. If so, we recursively try to build chunks from the remainder of the string. If we reach the end, it is a valid ip address.
"""
class Solution:
    def solve(self, ip,cnt=4,prefix=""):
        addr = [a for a in addresses(ip)]
        return addr
        
    
def addresses(ip,cnt=4,prefix=[]):
    if ip=="" and cnt==0:  yield ".".join(prefix)
    if ip=="" or cnt==0: return
    for i in range(1,min(len(ip)+1, 4)):
        cur_prefix=ip[:i]
        if cur_prefix != "0" and cur_prefix != cur_prefix.lstrip("0"): continue
        if 0<=int(cur_prefix)<=255:
            prefix.append(cur_prefix)
            yield from addresses(ip[i:],cnt-1, prefix)
            prefix.pop()
