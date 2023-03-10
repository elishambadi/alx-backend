#!/usr/bin/env python3
"""
Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Cache class inheriting from BasicCaching implementing FIFO
    Inherits from: BaseCaching
    """
    def __init__(self):
        """Initialize the Cache
        """
        super().__init__()

    def put(self, key, item):
        """
        put() - adds an item to cache
              - follows FIFO policy
        Args: self, key, item
        Return: none
        """
        if (key is not None and item is not None):
            self.cache_data.update({key: item})
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                print("DISCARD: {}".format(next(iter(self.cache_data))))
                self.cache_data.pop(list(self.cache_data)[0])

    def get(self, key):
        """
        get() - gets an item from cache
              - uses item key
        Args: self, key
        Return: item or None
        """
        if (key is not None and self.cache_data.get is not None):
            return self.cache_data.get(key)
        return None
