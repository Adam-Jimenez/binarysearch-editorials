"""
Range Query on a List

This problem can be used an exercise to learn about segment trees, even if the time complexity is worse than prefix sums. Segment trees are useful for general range queries using any aggregating operator (sum, min, max, product, ...). 

## How it works

The list of numbers becomes the bottom level of the segment tree. Then every pair of neighbors gets combined into a new node in the upper level. Each level will have half the number of nodes as the previous one, so we can say that the height of this tree will be log(n), where n is the number of items in our input.

We can represent this tree using an array where index 1 is the root of the tree, and its children can be accessed the following way: 

|  OOP representation | Array representation  |  
|---|---|
|  node  |   array[i]| 
|  node.left | array[i * 2]  | 
|  node.right | array[i * 2 + 1]
The reason this works is because each level has twice as many nodes as the previous ones, so doubling the index skips a level. 
This same logic is used for a heap, and can be used for any nearly complete tree.

**To build the tree**, we create a new array double the size of our original list of numbers. The first half will be generated nodes, while the second half will be the original numbers sitting on the last level of the tree. We iterate backwards on the first half, combining the children of the current node like mentioned above:
```python
self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
```
Every node contains the sum of all the nodes under it. We can use this fact to query a range of the tree in log(n) time.

**To query a range**, we must figure out the minimal number of nodes to combine to get our answer. For this approach, we start on the index of the original elements of the list by offsetting by half the list:
```
m = self.l + i
n = self.l + j
```
Then the logic goes as follows. 

For the left bound **m**:
- If we are the left child of our parent, we do not need to add the current value as the parent contains both the left and the right child, so we can just go up in the tree.
- If we are the right child of our parent, we cannot use our parent because it includes the left child which isn't in the range query. Therefore, we add the current value to the result, and move to our parent's right neighbor. 

We do the opposite for the right bound **n**:
-  If we are the right child of our parent, we do not need to add the current value as the parent contains both the left and the right child, so we can just go up in the tree.
- If we are the left child of our parent, we cannot use our parent because it includes the right child which isn't in the range query. Therefore, we add the current value to the result, and move to our parent's left neighbor. 

It is possible that we reach the same node with both bounds. Given that they are equal, the node will be either a left child or a right child but never both, therefore it will only be counted once. After that, the bounds will cross and the loop will exit.

This cover the basics of the wonderful segment tree. Its true power comes with additional features such as adding new elements or lazy propagation.
"""
class SegmentTree:
	def __init__(self, nums):
		self.l = len(nums)
		self.tree = [0] * self.l + nums
		for i in range(self.l - 1, 0, -1):
			self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

	def sum_range(self, i, j):
		m = self.l + i
		n = self.l + j
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
		
class RangeSum:
    def __init__(self, nums):
        self.st = SegmentTree(nums)
    def total(self, i, j):
        return self.st.sum_range(i, j-1)
        