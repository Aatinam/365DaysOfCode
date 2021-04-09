#Day 19 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/lru-cache/

#Problem Statement : Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#Implement the LRUCache class:
#LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#int get(int key) Return the value of the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. 
#Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
#evict the least recently used key.

from collections import OrderedDict
class LRUCacheSolOne:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity;
        self.dict = OrderedDict();
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1;
        self.dict.move_to_end(key);
        return self.dict[key];
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dict[key] = value;
        self.dict.move_to_end(key);
        if len(self.dict) > self.capacity:
            self.dict.popitem(last = False);

# If immutable objects are objects whose value can't change once created, a mutable object is an object whose
# value can change once created. Mutable objects are often objects that can store a collection of data. Lists (Python type list ) 
# and dictionaries (Python type dict ) are examples of mutable objects.
# str, int, tuple are some of the builtin immutable types => copy by value
# dict, lists -> mutable -> copy by reference 


            


