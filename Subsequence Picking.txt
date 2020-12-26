"""
Subsequence Picking

Time complexity: O(n^2) I think, because we build a list of dictionary that have at most n elements.

Inspired by https://leetcode.com/problems/distinct-subsequences-ii/, modified to keep track of the count of subsequences of given length.

We want to minimize the cost of picking k subsequences, where the cost of picking a subsequence is given by the length of the string minus the length of the subsequence. Therefore, we want to pick the longest k subsequences. We need to find out how many subsequences of any given length exists to solve this.

Let's start by ignoring the constraint that says that subsequences must be distinct, how do we find the number of subsequences of different lengths then? Well, we can do this is a dynamic programming fashion, where we start with an empty string as the base case, and then iterate over every character, and counting how many subsequences result from adding the character to all existing subsequences, and not adding it.

This works, as long as there are no duplicates characters. Let's take "aa" for example. At first, we start with the empty string:

"" : {0: 1} (There is one subsequence of length 0)
"a": {0: 1, 1: 1} (We copy the previous state for the case where we don't pick the current character, and add to key+1 for the case where we pick a)
"aa": {0:1, 1: 2, 2: 1} (Here, we count the subsequence "a" twice, we have ["", "a", "a", "aa"])

To avoid duplicates, we can keep track of the last time we saw the current character, and subtract whatever the state was at that point to the current state, so we don't double count subsequences.

Most of the work is done, we just have to pick the k largest subsequences, which will be left as an exercice to the reader, or just look at the code :)

"""
class Solution:
    def solve(self, S, k):
        dp = [{0:1}]
        last = {}
        for i, x in enumerate(S):
            new=dict(dp[-1])
            for key,v in dp[-1].items():
                if x in last and key in dp[last[x]]:
                    new[key+1]=new.get(key+1,0)-dp[last[x]][key]
                new[key+1]=new.get(key+1,0)+v
            dp.append(new)
            last[x] = i
        tot_cost=0
        for sslen,amount in sorted(dp[-1].items(), reverse=True):
            cost=len(S) - sslen
            count=min(amount,k)
            tot_cost += count*cost
            k-=count
            if k == 0: break
        return tot_cost if k == 0 else -1