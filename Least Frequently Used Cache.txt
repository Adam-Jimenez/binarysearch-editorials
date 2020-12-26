"""
Least Frequently Used Cache

*I recommend looking at the problem **LRU Cache** first, as this problem builds on similar ideas.*

For our LFU Cache class, we keep track of four important properties:

- The capacity.
- A dictionary where each unique frequency maps to a LRU Cache of values (equivalent to a doubly-linked list).
- The minimum frequency. We only need to store one single value because the only case where we evict the least frequent value is when we insert a value not present in our cache and at that point we can replace the minimum frequency with a frequency of 0.
- A dictionary enabling use to lookup each values according to the key.

## Let's look at the first simple step: how to we `get` a value from our LFU Cache?

**Simple!**

We look in our `key_to_node` dictionary. If the key is present, we retrieve the value from the underlying node. 
The more complex part is: **how do we update the frequency of the node?** I think this has nothing to do with retrieving the value, so let's abstract it away in another method and deal with it later.

## How do we `set` a value?

**A little bit harder, but still manageable!**

If the value is already set, we retrieve the node and overwrite its value and frequency. Since we decided earlier to deal with updating frequencies in a different method, we can once again deal with it later.

**What if the value is not present?**

Then this is the case where we possibly have to evict the least frequent value. Let's once again abstract this away in another method and worry with the implementation later. For now, let's just say: 
```python
if len(self.key_to_node) == self.capacity:
    # do the thing!
```
After we have handled our capacity problem, we can freely insert our value. To do that, we create a new linked list node, we insert in our `key_to_node` dictionary and in the appropriate LRU Cache in `self.cache`. Also, this newly inserted node becomes the least frequent element, so we set `self.min_frequency` to zero.

## Nooooo you can't just abstract every hard part of the problem and pretend you solved it!

Fine. Let's implement the methods we ignored until now: `update_frequency(node)` and `evict_least_frequently_used()`

## How do we update the frequency of a node?

***Note**: This part is important. Remember this and you can solve this problem with your eyes closed*

The first step is to remove the node from the LRU cache (doubly-linked list) it currently resides in. When doing so, we have to check if we leave the LRU Cache empty - if it is the case, it is possible that we must increment the minimum frequency. To know if our minimum frequency changes, we look if the LRU cache that we are leaving empty has a key equal to the minimum frequency of the LFU cache. If it is the case, we know that the current node was the least frequent, and we must increment the minimum frequency.

Then we can insert the node to the LRU Cache of the next frequency, and call it a day.

## How do we evict the least frequent node?

We pop the last value off the LRU Cache with a frequency equal to `self.min_frequency`. Thankfully, the min_frequency is overwritten after this method, because evicting the least frequent node leaves the min_frequency invalid for a few lines of code (monkaS).

"""
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class LLNode:
    key: int = -1
    val: int = -1
    freq: int = -1
    prev: LLNode = None
    next: LLNode = None
    
    
class LinkedList:
    def __init__(self):
        """
        Thanks to bunny for this trick!
        We can pad the doubly link list
        with dummy nodes so we don't have
        any edge cases to deal with 
        when inserting/removing nodes
        """
        self.head = LLNode()
        self.tail = LLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert(self, node):
        left, right = self.head, self.head.next
        node.prev, node.next = left, right
        left.next, right.prev = node, node
        self.size += 1
        return node
        
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        node.prev, node.next = None, None
        self.size -= 1
        return node
        
    def pop(self):
        if self.size == 0:
            raise Exception("Cannot pop from empty list")
        return self.remove(self.tail.prev)
        
        
class LRUCache:
    def __init__(self):
        self.list = LinkedList()
        
    def insert(self, node):
        self.list.insert(node)
        
    def remove(self, node):
        self.list.remove(node)
        
    def evict_least_recent(self):
        return self.list.pop()
        
    @property
    def size(self):
        return self.list.size
        
        
class LFUCache:
    def __init__(self, capacity):
        """
        For each frequency, we use a 
        Least Recently Used cache to handle
        with the case where we have multiple entries
        of the same frequency.
        """
        self.cache = defaultdict(LRUCache)
        self.capacity = capacity
        self.min_frequency = 0
        self.key_to_node = {}

    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.update_frequency(node)
        return node.val

    def set(self, key, val):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = val
            self.update_frequency(node)
        else:
            if len(self.key_to_node) == self.capacity:
                self.evict_least_frequent()
            node = LLNode(key=key, val=val, freq=0)
            self.key_to_node[key] = node
            self.cache[node.freq].insert(node)
            self.min_frequency = 0
            
        
    def update_frequency(self, node):
        self.cache[node.freq].remove(node)
        if self.cache[node.freq].size == 0 and node.freq == self.min_frequency:
            self.min_frequency += 1
        node.freq += 1
        self.cache[node.freq].insert(node)
        
    def evict_least_frequent(self):
        node = self.cache[self.min_frequency].evict_least_recent()
        del self.key_to_node[node.key]
        