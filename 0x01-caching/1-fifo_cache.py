#!/usr/bin/python3
"""FIFOCache module

    - Item is append to the end of the cache dict.
    - Once exceed the threshold, the first item is removed.
    - The next item is append again to the end of the cache.
    - It has a one way it (end) and one out (begining).
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching of data by using First in, First out Algorithm
    """

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
