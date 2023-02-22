#!/usr/bin/env python3
"""
Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Cache class inheriting from BasicCaching implementing FIFO
    Inherits from: BaseCaching
    """
    MAX_INT = 2147483647

    def __init__(self):
        """Initialize the Cache
        """
        super().__init__()
        self.sequence = []
        self.frequency = {}

    def put(self, key, item):
        """
        put() - adds an item to cache
              - follows LFU policy with LRU to resolve conflicts
        Args: self, key, item
        Return: none
        """
        #  print("\nPutting some data...")
        held_key = ""
        if (key is not None and item is not None):
            if (key in self.sequence):
                n = self.frequency.get(key) + 1
                self.frequency.update({key: n})
                held_key = self.sequence.pop(self.sequence.index(key))

            self.cache_data.update({key: item})

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                """Implement LFU checks here
                """
                lowest: int = LFUCache.MAX_INT
                lowest_list = []
                for k, v in self.frequency.items():
                    if (v <= lowest):
                        if (lowest == v):
                            lowest_list.append(k)
                        else:
                            lowest_list.clear()
                            lowest_list.append(k)
                            lowest = v
                #  print("Low list: {}".format(lowest_list))
                #  print("Sequence: {}".format(self.sequence))

                for i in range(len(self.sequence) - 1, -1, -1):
                    if (self.sequence[i] in lowest_list):
                        print("DISCARD: {}".format(self.sequence[i]))
                        self.cache_data.pop(self.sequence[i])
                        self.frequency.pop(self.sequence[i])
                        self.sequence.pop(i)
                        break

            if (key not in self.sequence and key != held_key):
                self.frequency.update({key: 1})
            self.sequence.insert(0, key)
            #  print("Put {}. Sequence: {}".format(key, self.sequence))

    def get(self, key):
        """
        get() - gets an item from the cache
              - uses item key
        Args: self, key
        Return: item or None
        """
        if (key is not None and self.cache_data.get(key) is not None):
            if (key in self.sequence):
                n = self.frequency.get(key) + 1
                self.frequency.update({key: n})
                self.sequence.pop(self.sequence.index(key))
            self.sequence.insert(0, key)
            #  print("Got {}. Sequence: {}".format(key, self.sequence))
            #  print("Frequency: {}".format(self.frequency))
            return self.cache_data.get(key)
        return None
