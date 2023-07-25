# Caching
## Description
Caching is the ability to store data in a temporary storage area called a cache. Cached data is stored in a cache, which can exist in a variety of locations on the local machine or on the network. When a cache has been compromised, it is refreshed with the most recent or most frequently accessed data.

## Tasks
### 0. Basic dictionary
Create a class BasicCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* This caching system doesn’t have limit
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.
    
### 1. FIFO caching
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
  * If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    * you must discard the first item put in cache (FIFO algorithm)
    * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.

### 2. LIFO Caching
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
  * If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    * you must discard the last item put in cache (LIFO algorithm)
    * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.

### 3. LRU Caching
Create a class LRUCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
  * If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    * you must discard the least recently used item (LRU algorithm)
    * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.

### 4. MRU Caching
Create a class MRUCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
  * If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    * you must discard the most recently used item (MRU algorithm)
    * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.

### 5. LFU Caching
Create a class LFUCache that inherits from BaseCaching and is a caching system:

* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
* def put(self, key, item):
  * Must assign to the dictionary self.cache_data the item value for the key key.
  * If key or item is None, this method should not do anything.
  * If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    * you must discard the least frequently used item (LFU algorithm)
    * you must print DISCARD: with the key discarded and following by a new line
* def get(self, key):
    * Must return the value in self.cache_data linked to key.
    * If key is None or if the key doesn’t exist in self.cache_data, return None.


## Resources
* [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
* [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
* [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
* [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
* [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)


## License
MIT. See [LICENSE](./LICENSE) for more details.