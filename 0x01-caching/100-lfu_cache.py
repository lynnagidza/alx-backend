#!/usr/bin/python3
""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            key_patch = False
            if key in self.cache_data:
                self.queue.remove(key)
                key_patch = True
            elif len(self.cache_data) >= self.MAX_ITEMS:
                for k, val in self.count.items():
                    minimum = min(self.count.values())
                    i = self.queue.index(k)
                    if val == minimum:
                        del self.cache_data[self.queue[i]]
                        del self.count[self.queue[i]]
                        print(f"DISCARD: {self.queue[i]}")
                        self.queue.pop(i)
                        break
            self.queue.append(key)
            self.cache_data[key] = item
            if key_patch:
                self.count[key] += 1
            else:
                self.count[key] = 0

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None

# test
# my_cache = LFUCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# print(my_cache.get("B"))
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
# my_cache.put("L", "L")
# my_cache.print_cache()
# my_cache.put("M", "M")
# my_cache.print_cache()
