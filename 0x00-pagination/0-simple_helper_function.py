#!/usr/bin/env python3

"""Simple pagination helper
"""


def index_range(page, page_size):
    return (page_size * (page - 1), page_size * page)
