#!/usr/bin/env python3
"""Pagination Functions"""


def index_range(page, page_size):
    """
    Returns an index range of items for pagination.
    Args: page: int, page_size: int
    Returns: tuple
    """
    if page <= 0 or page_size <= 0:
        return None

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
