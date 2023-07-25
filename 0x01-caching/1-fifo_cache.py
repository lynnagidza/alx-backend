#!/usr/bin/python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.queue[0]]
                print(f"DISCARD: {self.queue[0]}")
                self.queue.pop(0)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

# test
# my_cache = FIFOCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# my_cache.put("F", "Mission")
# my_cache.print_cache()
