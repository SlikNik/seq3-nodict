#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Nikal Morgan'


class Node:
    def __init__(self, key, value=None):
        """Initializes with a mandatory key and an optional value"""
        self.hash = hash(key)
        self.key = key
        self.value = value
        # Your code here
        return

    def __repr__(self):
        """Return a string representation of the class contents"""
        # Your code here
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Returns comparison of itself to other Node objects"""
        # Your code here
        return self.hash == other.hash and self.key == other.key


# n1 = Node('Mike', 21)
# n2 = Node('Mike', 34)
# n3 = Node('Nick', 56)
# print(n1.__repr__())
# print(n2.__repr__())
# print(n3.__repr__())
# print(f'n1 == n2 ? {n1 == n2}')
# print(f'n2 == n3 ? {n2 == n3}')

class NoDict:
    def __init__(self, num_buckets=10):
        """Create the buckets according to a num_buckets parameter. """
        self.buckets = [[] for _ in range(num_buckets)]
        self.num_buckets = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Accept a new key and value, and store it into the NoDict instance;
        no duplicate keys."""
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.num_buckets]
        for keys in bucket:
            if keys == new_node:
                bucket.remove(keys)
                break
        bucket.append(new_node)

    def get(self, key):
        """Performs a key-lookup from given key.
        If the key is found return its associated value.
        If the key is not found, raise a KeyError exception."""
        get_node = Node(key)
        bucket = self.buckets[get_node.hash % self.num_buckets]
        for keys in bucket:
            if keys == get_node:
                return keys.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Enable square-bracket reading behavior;
        behave more like a regular dictionary."""
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """Setter method that enables square-bracket assignment behavior."""
        self.add(key, value)


my_dict = NoDict()
my_dict['Kevin'] = 23
my_dict['Nikal'] = 26
my_dict['Nicolette'] = 21
print(my_dict)
kevin_age = my_dict['Kevin']
nikal_age = my_dict['Nikal']
nicolette_age = my_dict['Nicolette']
print(kevin_age)
print(nikal_age)
print(nicolette_age)


