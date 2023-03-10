#!/usr/bin/env python3
"""
More pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range() - returns an index range
    Args: page, page_size
    Returns: tuple
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialization function
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets data from a page
           Uses: index_page function to get indexes used in querying
           Returns: list of objects
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        result: tuple = index_range(page, page_size)
        pages = []

        for i in range(result[0], result[1]):
            try:
                pages.append(self.dataset()[i])
            except IndexError:
                return []

        return pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get_hyper() - returns detailed pagination details
           Args: page, page_size
           Returns: dict with page details
        """
        data = self.get_page(page, page_size)
        if data == []:
            next_page = None
        else:
            next_page = page + 1

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
            }
