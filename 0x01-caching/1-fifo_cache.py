#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache, following FIFO logic """
        if key and item:
            # Check if cache has reached MAX_ITEMS
            if len(self.cache_data) == self.MAX_ITEMS:
                # Get the oldest key using list indexing for FIFO
                oldest_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]
                
            # Add new item to cache
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)

