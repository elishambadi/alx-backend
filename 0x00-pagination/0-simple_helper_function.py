#!/usr/bin/env python3

"""Simple pagination helper
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range() - returns an index range
    Args: page, page_size
    Returns: tuple
    """
    return (page_size * (page - 1), page_size * page)
