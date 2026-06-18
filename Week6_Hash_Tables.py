##############################################################################################
#1.Implement a hash table from scratch with put, get, delete, and resize methods. Use separate chaining for collision handling. Test with 20+ entries.\
class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor_threshold = 0.75

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Insert new key
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.load_factor_threshold:
            self.resize()

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        old_size = self.size
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
        self.size = old_size

    def __len__(self):
        return self.size

    def __str__(self):
        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"

Testing with 20+ Entries

ht = HashTable()
for i in range(25):
    ht.put(f"user_{i}", i * 100)

print("Size:", len(ht))
print("Capacity:", ht.capacity)

print("\nSample Lookups")
print(ht.get("user_0"))
print(ht.get("user_10"))
print(ht.get("user_24"))

print("\nDelete Entries")
ht.delete("user_5")
ht.delete("user_10")

print("Size after deletes:", len(ht))

print("\nVerify Remaining")
print(ht.get("user_24"))

try:
    print(ht.get("user_10"))
except KeyError as e:
    print(e)

##############################################################################################

#2.Explain what happens during a hash collision. Compare separate chaining vs open addressing (linear probing). Which does Python's dict use?
A hash collision occurs when two different keys produce the same hash table index.
15 % 10 = 5
25 % 10 = 5
Both keys map to index 5.
The hash table must have a strategy to store and retrieve both values correctly

Separate Chaining:-
    In separate chaining, each bucket stores a collection (usually a linked list, dynamic array, or tree) of entries.
      Insert
        Compute hash.
        Find bucket.
        Append key-value pair to that bucket's chain.
      Search
        Compute hash.
        Go to bucket.
        Scan the chain until the key is found.

Open Addressing (Linear Probing):-
    Instead of storing a list at each bucket, every element is stored directly in the table.When a collision occurs, search for another empty slot.

##############################################################################################
#3.Write a function that groups anagrams together from a list of strings. 
Example: ['eat','tea','tan','ate','nat','bat'] → [['eat','tea','ate'],['tan','nat'],['bat']].

from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

##############################################################################################
#4.Find the longest consecutive sequence in an unsorted array.

def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

##############################################################################################

#5.Given an array of integers, return the top k most frequent elements using a bucket sort approach (not heap). Explain why this is O(n).
	
def top_k_frequent(nums, k):
    # Step 1: Count frequencies
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Create buckets
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    # Step 3: Collect top k frequencies
    result = []

    for count in range(len(buckets) - 1, 0, -1):
        for num in buckets[count]:
            result.append(num)

            if len(result) == k:
                return result

    return result

##############################################################################################
#6.Write a function that finds all pairs in an array that sum to a given target. Handle duplicate pairs. Return unique pairs only.
	
def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            # Store pair in sorted order to avoid duplicates
            pairs.add(tuple(sorted((num, complement))))

        seen.add(num)

    return [list(pair) for pair in pairs]
    
    
##############################################################################################
#7.Implement an LRU Cache with O(1) get and put operations. Hint: combine a hash map with a doubly linked list.

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move to front (most recently used)
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_front(node)
            return
        if len(self.cache) == self.capacity:
            # Remove LRU node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_front(new_node)

##############################################################################################

#8.Given a sudoku board (9×9), write a function to check if it is valid using hash sets for rows, columns, and 3×3 boxes
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = board[r][c]

            if value == ".":
                continue

            # Box index:
            # 0 1 2
            # 3 4 5
            # 6 7 8
            box = (r // 3) * 3 + (c // 3)

            if value in rows[r]:
                return False

            if value in cols[c]:
                return False

            if value in boxes[box]:
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    return True

	