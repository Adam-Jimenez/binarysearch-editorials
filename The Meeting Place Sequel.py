"""
The Meeting Place Sequel

Find the position of each person (value 2). 

For each person, keep a queue and apply one BFS tick to each person sequentially. When the BFS of someone intersects with the BFS of someone else, you have found the cost it takes to meet up with them. Return the max cost of any pair of person meeting up.
"""
class Solution:
    def solve(self, matrix):
        ppl={}
        sets={}
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v==2: 
                    ppl[(i,j)] = [(i,j)]
                    sets[(i,j)] = set()
                
        if len(ppl)==0: return 0
        cost={src_pos: 0 for src_pos in ppl.keys()}
        done={src_pos: False for src_pos in ppl.keys()}
        while not all(done.values()):
            for src_pos,q in ppl.items():
                if done[src_pos]: continue
                seen=sets[src_pos]
                for i in range(len(q)):
                    ci,cj = q.pop(0)
                    if (ci,cj) in seen: continue
                    seen.add((ci,cj))
                    neighbors = get_neighbors(ci,cj,matrix)
                    for ni,nj in neighbors:
                        q.append((ni,nj))
            for src_pos in ppl.keys():
                if done[src_pos]: continue
                seen=sets[src_pos]
                if all(len(seen&x)>0 for x in sets.values()):
                    done[src_pos]=True
                    continue
                cost[src_pos]+=1
        return max(cost.values())
        
    
def get_neighbors(i,j,matrix):
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    n=[]
    for di,dj in directions:
        ni,nj = i+di, j+dj
        if ni>=0 and nj>=0 and ni<len(matrix) and nj<len(matrix[0]) and matrix[ni][nj] != 1:
            n.append((ni,nj))
    return n
                        
