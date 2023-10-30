#!/usr/bin/env python3
"""Caching Module"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic Cache Class"""
    def put(self, key, item):
        """Puts an item into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache"""
        return self.cache_data.get(key, None)
