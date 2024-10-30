#!/usr/bin/python3
"""BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cache data in a dictionary
    """

    def put(self, key, item):
        """
        Put an item in a dict with corresponding key.

        :key - The key to store the item in dict.
        :item - the item to be store in dict.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the dict with it right key.

        :key - The key of item to be retrieved.
        """
        return self.cache_data.get(key)
