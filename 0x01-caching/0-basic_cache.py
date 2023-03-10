#!/usr/bin/env python3
"""
Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Cache class inheriting from BasicCaching
    Inherits from: BaseCaching
    """
    def __init__(self):
        """Initializes cache
        """
        super().__init__()

    def put(self, key, item):
        """Inserts an item into the cache
        """
        if (key is not None and item is not None):
            self.cache_data.update({key: item})

    def get(self, key):
        """Gets an item from the cache
        """
        if (key is not None and self.cache_data.get is not None):
            return self.cache_data.get(key)
        return None
