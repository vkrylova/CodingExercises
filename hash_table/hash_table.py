class HashEntry:
    """
     Represents a single entry in a hash table.

    Attributes:
        key: The key of the entry.
        value: The value associated with the key.
        nxt: Reference to the next entry in case of collision (linked list).
    """
    def __init__(self, key, data):
        self.key = key  # key of the entry
        self.value = data  # data to be stored
        self.nxt = None  # reference to new entry

    def __str__(self):
        return str(f"{self.key}, {self.value}")


class HashTable:
    """
    Simple hash table implementation using separate chaining for collisions.

    Attributes:
        slots (int): Number of buckets (initially 10).
        size (int): Current number of elements.
        bucket (list): Array of HashEntry objects (or None).
        threshold (float): Load factor threshold to trigger resizing.
    """

    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    def get_size(self):
        """Return the number of elements currently in the hash table."""
        return self.size

    def is_empty(self):
        """Return True if the hash table has no elements."""
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        """"Compute the bucket index for a given key."""
        hash_code = hash(key)  # hash is a built-in function in Python
        return hash_code % self.slots

    def resize(self):
        """Double the number of slots and rehash all existing entries."""
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for item in self.bucket:
            head = item
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key == head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        """Insert or update the value for a given key."""
        # Find the node with the given key
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            print(key, "-", value, "inserted at index:", b_index)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    print(key, "-", value, "inserted at index:", b_index)
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        """Return the value associated with the key, or None if not found."""
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None

    def delete(self, key):
        """Remove the entry with the specified key from the table.

        Returns:
            True if the key was found and deleted, None if key not found.
        """
        b_index = self.get_index(key)
        head = self.bucket[b_index]

        if head is None:
            return None

        # Key is in the first node
        if head.key == key:
            self.bucket[b_index] = head.nxt
            self.size -= 1
            return True

        # Key is in the chain
        prev = head
        head = head.nxt
        while head:
            if head.key == key:
                prev.nxt = head.nxt
                self.size -= 1
                return True
            prev = head
            head = head.nxt

        # Key not found
        return None