"""
String Construction

The solution to this problem is similar to a BFS in some ways: we start with an amount of letters and a number of words. Then we iterate over each word, counting the amount of letters A and B. Then, for each word chain we have in our answer, we try adding the current word if it fits, and if result in a greater word count than the previous occurrence of A/B amount.
"""
class Solution:
    def solve(self, strings, a, b):
        pairs=[]
        for w in strings:
            A = w.count("A")
            B = len(w)-A
            pairs.append((A,B))
        ans={(a,b):0}
        for A,B in pairs:
            cur_ans=dict(ans)
            for (cur_a,cur_b), wc in ans.items():
                if cur_a>=A and cur_b>=B:
                    rem = (cur_a-A, cur_b-B)
                    cur_ans[rem] = max(cur_ans.get(rem,0), wc+1)
            ans=cur_ans
        return max(ans.values())