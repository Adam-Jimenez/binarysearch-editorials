"""
Range Query on a List - Mutable

I suggest doing the immutable version of this problem first, and look at my segment tree solution for it. 

We can reuse the code, but this time we have an addition: the update function. When we modify a value, we invalidate all the ancestors of that node. As we have seen before, we can get the parent of the node by dividing its index by two. So while we haven't reached the root, we add the difference of our new value to the node and go to the parent. 


"""
class MutableRangeSum:
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def total(self, i, j):
        m = self.l + i
        n = self.l + j - 1
        ans = 0
        while m <= n:
            if m % 2 == 1:
                ans += self.tree[m]
                m += 1
            m //= 2
            
            if n % 2 == 0:
                ans += self.tree[n]
                n -= 1
            n //= 2
        return ans
            

    def update(self, idx, val):
        m = self.l + idx
        diff = val - self.tree[m]
        while m:
            self.tree[m] += diff