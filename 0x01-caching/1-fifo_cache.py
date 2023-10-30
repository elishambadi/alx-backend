#!/usr/bin/env python3
"""Caching Module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache Implementation"""

    def __init__(self):
        """
            Initialization Function
        """
        super().__init__()

    def put(self, key, item):
        """
            Put into a FIFO Cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

    def get(self, key):
        return self.cache_data.get(key, None)
