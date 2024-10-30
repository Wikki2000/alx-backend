#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache, following LIFO logic """
        if key and item:
            # Check if cache has reached MAX_ITEMS
            if len(self.cache_data) == self.MAX_ITEMS:
                print(f"DISCARD: {key}")

                self.cache_data.popitem() # Remove last item
                
            # Add new item to cache
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)

