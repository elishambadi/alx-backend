#!/usr/bin/env python3
"""
Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Cache class inheriting from BasicCaching implementing FIFO
    Inherits from: BaseCaching
    """
    def __init__(self):
        """Initialize the Cache
        """
        super().__init__()
        self.sequence = []

    def put(self, key, item):
        """
        put() - adds an item to cache
              - follows LIFO policy
        Args: self, key, item
        Return: none
        """
        if (key is not None and item is not None):
            if (key in self.sequence):
                self.sequence.pop(self.sequence.index(key))
            self.cache_data.update({key: item})

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                print("DISCARD: {}".format(self.sequence[0]))
                self.cache_data.pop(self.sequence[0])
                self.sequence.pop(0)
            self.sequence.insert(0, key)

    def get(self, key):
        """
        get() - gets an item from the cache
              - uses item key
        Args: self, key
        Return: item or None
        """
        if (key is not None and self.cache_data.get is not None):
            return self.cache_data.get(key)
        return None
