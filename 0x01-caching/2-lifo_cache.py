#!/usr/bin/python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache system """

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
                del self.cache_data[self.queue[-1]]
                print(f"DISCARD: {self.queue[-1]}")
                self.queue.pop(-1)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

# test
# my_cache = LIFOCache()
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
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
